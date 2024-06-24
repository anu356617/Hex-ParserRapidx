resource "kubernetes_deployment" "deploy_service_bus" {
  metadata {
    name = "deploy-service-bus"
  }
  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "deploy-service-bus"
      }
    }

    template {
      metadata {
        labels = {
          app = "deploy-service-bus"
        }
      }

      spec {
        container {
          name  = "deploy-service-bus"
          image = "nginx:latest"  # Replace with your actual image
          port {
            container_port = 5671
            protocol       = "TCP"
          }
          env {
            name  = "CONNECTION_STRING"
            value = "Endpoint=sb://keda-order-processor.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=JZCymAew/wONdVcvPcrahVpjV21XeKUtX+ASbO8ATYY="
          }
          volume_mount {
            mount_path = "/mnt/azure"
            name       = "azure-storage"
          }
        }

        volume {
          name = "azure-storage"
          persistent_volume_claim {
            claim_name = kubernetes_persistent_volume_claim.azure_file_pvc.metadata[0].name
          }
        }
      }
    }
  }
}
