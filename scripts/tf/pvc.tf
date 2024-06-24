resource "kubernetes_persistent_volume_claim" "azure_file_pvc" {
  metadata {
    name = "azure-file-pvc"
  }
  spec {
    access_modes = ["ReadWriteOnce"]
    resources {
      requests = {
        storage = "5Gi"
      }
    }
  }
}
