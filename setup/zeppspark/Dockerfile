FROM bitnami/spark:3.0.0
USER root
RUN pip3.6 install numpy scipy pandas sympy pyarrow scikit-learn h3
RUN curl https://repo1.maven.org/maven2/org/apache/kudu/kudu-spark3_2.12/1.15.0/kudu-spark3_2.12-1.15.0.jar --output /opt/bitnami/spark/jars/kudu-spark3_2.12-1.15.0.jar
