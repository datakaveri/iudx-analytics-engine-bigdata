kubectl create -f namespace.yaml

kubectl create -f master-pv.yaml --namespace apache-kudu

kubectl create -f tserver-pv.yaml --namespace apache-kudu

kubectl get pv --namespace apache-kudu

kubectl create -f master-pvc.yaml --namespace apache-kudu

kubectl create -f tserver-pvc.yaml --namespace apache-kudu

kubectl get pvc --namespace apache-kudu

kubectl create -f kudu-services.yaml --namespace apache-kudu

kubectl get services --namespace apache-kudu

kubectl create -f kudu-statefulset.yaml --namespace apache-kudu

kubectl get statefulset --namespace apache-kudu

kubectl get pods --namespace apache-kudu

# kubectl port-forward kudu-master-0 7051 -n apache-kudu
# kubectl logs kudu-master-0 --namespace apache-kudu
