resource "kubernetes_manifest" "azure_service_bus_scaledobject" {
  manifest = <<YAML
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: azure-service-bus-scaledobject
spec:
  scaleTargetRef:
    deploymentName: deploy-service-bus
  cooldownPeriod: 60 
  minReplicaCount: 1
  maxReplicaCount: 10
  triggers:
  - type: azure-service-bus
    metadata:
      queueName: my-service-bus-queue
      queueLength: "5"
YAML
}
