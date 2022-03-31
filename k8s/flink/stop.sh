kubectl delete serviceaccount flink-service-account
kubectl delete clusterrolebinding flink-role-binding-flink
kubectl delete deployment flink-cluster
kubectl delete -f flink-metrics-service.yaml
kubectl delete -f taskmanager-metrics-service.yaml
