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
kubectl get scaledObjects
kubectl  describe scaledobject analyserservice-scaledobject

azure cli

sudo apt update
sudo apt install azure-cli
azure --version
azure login
az account list --output table
az account set --subscription <subscription-id-or-name>

inside ACR
 az acr login --name rapidxccdev

image build
docker image prune -f
docker ps -a
dockr stop 
docker rm 
docker build -t rapidxccdev.azurecr.io/eventlogservice:latest .
docker images
<!-- docker tag eventservice:latest rapidxccdev.azurecr.io/eventservice:latest -->
docker push rapidxccdev.azurecr.io/eventlogservice:latest
docker images | grep rapidxccdev.azurecr.io/reposervice
docker inspect rapidxccdev.azurecr.io/monitorservice:latest

docker run -d --name my-linkerservice rapidxccdev.azurecr.io/linkerservice:latest

kubectl get deployment monitorservice -o yaml

docker rmi rapidxccdev.azurecr.io/monitorservice:latest
az acr update -n rapidxccdev --admin-enabled true

ACR_USERNAME=$(az acr credential show -n rapidxccdev --query "username" -o tsv)
ACR_PASSWORD=$(az acr credential show -n rapidxccdev --query "passwords[0].value" -o tsv)


kubectl create secret docker-registry acr-credentials \
  --docker-server=rapidxccdev.azurecr.io \
  --docker-username=$ACR_USERNAME \
  --docker-password=$ACR_PASSWORD \
  --docker-email=<your-email@example.com>



KEDA
helm repo add kedacore https://kedacore.github.io/charts
 helm repo update
 helm install keda kedacore/keda
  kubectl get pods -n keda