kubectl create serviceaccount flink-service-account
kubectl create clusterrolebinding flink-role-binding-flink --clusterrole=edit --serviceaccount=default:flink-service-account
./bin/kubernetes-session.sh -Dkubernetes.cluster-id=flink-cluster -Dkubernetes.service-account=flink-service-account -Dkubernetes.container.image=datakaveri/flink:latest
kubectl apply -f flink-metrics-service.yaml
kubectl apply -f taskmanager-metrics-service.yaml
