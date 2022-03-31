# 1. Add Helm repo
helm repo add kedacore https://kedacore.github.io/charts

# 2. Update Helm repo
helm repo update

# 3. Install keda Helm chart

kubectl create namespace monitoring
helm install keda kedacore/keda --namespace monitoring

