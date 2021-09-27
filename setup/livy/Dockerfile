FROM ubuntu:18.04 

RUN apt-get update -y &&  apt-get install git curl unzip wget python3.6 python-pip python3-pip  make -y 
RUN apt-get install openjdk-8-jdk -y

# Download and unbox Spark + Hadoop binaries
RUN cd /tmp && \
        wget https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz && \
        tar zxvf spark-3.0.0-bin-hadoop3.2.tgz -C /usr/local --owner root --group root --no-same-owner && \
        rm spark-3.0.0-bin-hadoop3.2.tgz

# Rename Spark folder
RUN cd /usr/local && ln -s spark-3.0.0-bin-hadoop3.2 spark

# Set Spark environment variables
ENV SPARK_HOME /usr/local/spark
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# Create folder for Livy source files
RUN mkdir -p /src/livy
WORKDIR /src/livy

# Download Livy source files
RUN wget http://mirror.evowise.com/apache/incubator/livy/0.6.0-incubating/apache-livy-0.6.0-incubating-bin.zip

# Unzip livy source files
RUN apt-get update && apt-get install unzip
RUN unzip apache-livy-0.6.0-incubating-bin.zip && \
    rm apache-livy-0.6.0-incubating-bin.zip

# set Python3 as default
RUN rm  /usr/bin/python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copy the local config file to the container
COPY ./livy.conf /src/livy/apache-livy-0.6.0-incubating-bin/conf/


# Set the Livy logs folder and start the server
SHELL ["/bin/bash", "-c"]
RUN mkdir -p /src/livy/apache-livy-0.6.0-incubating-bin/logs
CMD ["/src/livy/apache-livy-0.6.0-incubating-bin/bin/livy-server"]