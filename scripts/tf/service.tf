resource "kubernetes_service" "azure_service_bus" {
  metadata {
    name = "azure-service-bus"
  }
  spec {
    selector = {
      app = kubernetes_deployment.deploy_service_bus.spec.0.template.0.metadata.0.labels.app
    }

    port {
      protocol    = "TCP"
      port        = 5671
      target_port = 5671
    }
  }
}
