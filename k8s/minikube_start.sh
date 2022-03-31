minikube start --mount-string "$HOME/scripts/:/mnt/scripts" --mount
kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=default --user=kubelet --group=system:serviceaccounts
# minikube mount $HOME/scripts/:/mnt/scripts
