# Flink Kubernetes Microservice

## Steps to install

- Download latest Apache Flink binary (1.14.3 here).
```
wget https://dlcdn.apache.org/flink/flink-1.14.4/flink-1.14.4-bin-scala_2.12.tgz
```
- Unzip the `tgz` file.
```
tar -xvzf flink-1.14.4-bin-scala_2.12.tgz
```
- Move `flink-conf.yaml` to `flink-1.14.4/conf` directory.
```
mv flink-conf.yaml flink-1.14.4/conf/flink-conf.yaml
```
- Start a session cluster.
```
./flink-1.14.4/bin/kubernetes-session.sh -Dkubernetes.cluster-id=flink-cluster -Dkubernetes.service-account=flink-service-account   -Dkubernetes.container.image=krithikvaidya/custom-flink:latest 
```
- Running the above will automatically read *conf/flink-conf.yaml* and *~/.kube/config*
- To submit an example job,
```
./flink-1.14.4/bin/flink run --target kubernetes-session -Dkubernetes.cluster-id=flink-cluster -Dkubernetes.service-account=flink-service-account ./flink-1.14.4/examples/streaming/TopSpeedWindowing.jar
```
- With ```kubectl get svc```, you can get the LoadBalancer IP of the cluster and access the Flink web dashboard.
- Increase/decrease the memory/CPU sizes of the jobmanagers and taskmanagers in the *flink-conf.yaml* as needed.

- The *custom-flink* image was built from *Dockerfile114* present in *setup/flink/Dockerfile114*. You will need to download
two additional archives at [1](https://archive.apache.org/dist/flink/flink-1.14.3/python/apache-flink-libraries-1.14.3.tar.gz) and [2](https://archive.apache.org/dist/flink/flink-1.14.3/python/apache-flink-1.14.3.tar.gz)
and place them in the same folder, before rebuilding the image. (Those are related to PyFlink support).

## Metrics

- Kubernetes service for exposing metrics from jobmanager and taskmanager pods have also been defined here,
to be consumed by prometheus.
