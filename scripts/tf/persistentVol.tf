resource "kubernetes_persistent_volume" "azure_file_pv" {
  metadata {
    name = "azure-file-pv"
  }
  spec {
    capacity = {
      storage = "5Gi"
    }
    access_modes = ["ReadWriteMany"]

    persistent_volume_source {
      azure_file {
        secret_name = "secretrapidx"
        share_name  = "fsdnssalesdev"
        read_only   = false
      }
    }

    mount_options = ["dir_mode=0777", "file_mode=0777", "uid=1000", "gid=1000"]
  }
}
