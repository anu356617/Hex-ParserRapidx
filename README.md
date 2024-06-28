#ParserRapidx

kind install

curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind version
kind create cluster
kubectl config get-contexts
kubectl get nodes
kind cluster-info
kind get cluster
kind delete cluster --name <cluster-name>


AKS
az aks get-credentials --resource-group <resource-group> --name <cluster-name>


helm install

curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
Add helm repo
helm repo add stable https://charts.helm.sh/stable
helm repo update

helm create dev-chart

verify the helm chart
helm lint ./dev-chart

dry run and debug
helm install my-release ./dev-chart --dry-run --debug

To install your Helm chart, navigate to the chart directory and run:
helm install my-release ./my-chart

my-release: This is the name you give to this particular deployment or instance of the Helm chart. It serves as a unique identifier for this release within the Kubernetes namespace where it is deployed.
./my-chart: This specifies the path to the directory containing your Helm chart (my-chart). Helm expects this directory to contain a Chart.yaml file and a templates/ directory with Kubernetes manifest templates.

Customize Chart Values during Installation
helm install my-release ./my-chart -f values.yaml
# or
helm install my-release ./my-chart --set service.type=LoadBalancer

Package and Share Your Helm Chart
helm package ./my-chart

helm upgrade my-release ./dev-chart
helm uninstall my-release

kubectl get pvc
