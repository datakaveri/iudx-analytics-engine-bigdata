helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator --force-update

helm install spark1 spark-operator/spark-operator --namespace spark-operator --create-namespace --set image.tag=v1beta2-1.3.2-3.1.1 --set webhook.enable=true --set image.repository=docker.io/datakaveri/spark-operator --debug

kubectl apply -f pvc/pv-volume.yaml --namespace spark-operator

kubectl apply -f pvc/pv-claim.yaml --namespace spark-operator

kubectl apply -f pvc/spark.yaml --namespace spark-operator
