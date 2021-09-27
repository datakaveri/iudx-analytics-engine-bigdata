FROM apache/airflow:2.1.1
RUN pip install pyspark==3.0.0 && pip install apache-airflow-providers-apache-spark
USER root
RUN sudo apt-get update && \
    sudo apt-get install -y openjdk-11-jre-headless && \
    sudo apt-get clean;
USER default
