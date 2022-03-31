kubectl delete -f configs.yaml -n monitoring
kubectl delete -f coordinator.yaml -n monitoring
kubectl delete -f worker.yaml -n monitoring
kubectl delete -f service.yaml -n monitoring
kubectl delete -f namespace.yaml
