kubectl delete -f master-pv.yaml --namespace apache-kudu

kubectl delete -f tserver-pv.yaml --namespace apache-kudu

kubectl delete -f master-pvc.yaml --namespace apache-kudu

kubectl delete -f tserver-pvc.yaml --namespace apache-kudu

kubectl delete -f kudu-services.yaml --namespace apache-kudu

kubectl delete -f kudu-statefulset.yaml --namespace apache-kudu

kubectl delete -f namespace.yaml
