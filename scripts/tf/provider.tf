provider "kubernetes" {
  config_path = "~/.kube/config"

  # Optionally, you can specify other configurations such as:

  # config_path = "~/.kube/config"  # If your kubeconfig is not in the default location
  # token = "your_kube_token"       # If you're using token-based authentication
  # ...
  
}
