kubectl apply -f namespace.yaml
kubectl apply -f configs.yaml --namespace monitoring
sleep 5
kubectl apply -f coordinator.yaml --namespace monitoring
kubectl apply -f worker.yaml --namespace monitoring
kubectl apply -f service.yaml --namespace monitoring
