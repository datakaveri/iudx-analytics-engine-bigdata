## Component bringup

### **Components Setup order**
RMQ -> Kudu -> Minio -> Zookeeper -> Flink -> Trino -> Superset -> Apps.

### **Components Setup**
In order to setup the pipeline, a lot of components need to be setup individually and in a proper sequence.

Usual deployments will have to follow the following sequence.

#### **RabbitMQ**
RabbitMQ needs to be setup before everything so that the other components do find the queues while starting up.

    cd scripts/start_services
    ./start_rmq.sh
#### **Kudu**
Kudu stores the streaming data into a column-oriented database. It needs to be started before starting flink job so that Flink is able to find Kudu masters running beforehand.

    cd scripts/start_services
    ./start_kudu.sh

#### **MinIO**
MinIO service can be started in the similar way as stated above:

    cd scripts/start_services
    ./start_minio.sh

Two buckets need to created in minIO, one to save checkpoints (*state*) and the other to save the job graph and recently completed checkpoint (*recovery*).

#### **Zookeeper**
Zookeeper manages the Flink Jobmanager and its state. It can be started with the following commands:

    cd scripts/start_services
    ./start_zookeeper.sh


#### **Flink**
Flink adds the RMQ consumer as source to pull the data and sinks it into the Kudu tables.

    cd scripts/start_services
    ./start_flink.sh

#### **Impala** (*Deprecated*)
Impala is used to query into Kudu tables. It creates a mapping table (external table) which creates a link to the Kudu table. Then, SQL queries can be run in `impala-shell` to access Kudu tables' data.

    cd scripts/start_services
    ./start_impala.sh

#### **Trino**
Trino too is used to query into Kudu tables. It creates automatic mapping with Kudu database. Then, SQL queries can be run in `trino` CLI to access Kudu tables.


    cd scripts/start_services
    ./start_trino.shv

#### **Superset**
Superset performs analysis over the data and creates visualization. It connects to the impala database using its URL.

    cd scripts/start_services
    ./start_superset.sh

### **Running Components**

#### **Publisher**
Since RMQ service is on, the data can be pushed to RMQ exchange from publisher.

    cd extras/RMQPublisher/FlinkKuduPublisher
    pip install -r requirements.txt
    python publisher.py

This starts up the publisher.

#### **Impala Shell**
The data gets pushed into the Kudu table. This table needs to mapped to impala external table so that it can be queried. So, impala-shell needs to be installed and then connected to impala service.

    pip install impala-shell==3.4.0
    impala-shell
    > CONNECT 172.18.0.1:21000;

The impala-shell, then needs to create an external table to map to kudu table. We can also create a separate database to store Kudu tables.

    > CREATE DATABASE KUDU_DB;
    > USE KUDU_DB;
    > CREATE EXTERNAL TABLE mapping_table
      STORED AS KUDU
      TBLPROPERTIES (
        'kudu.table_name' = 'iudx005'
      );

Now, this table can be accessed from Superset easily.
#### **Superset**
The Impala database can be linked to the Superset very conveniently. The following URL can access the Impala database.

The expected connection string is formatted as follows:

    impala://{hostname}:{port}/{database}

For example:

    impala://172.18.0.1:21050/kudu_db

**Note**: IP `172.18.0.1` should not be hardcoded. This IP is the value of `QUICKSTART_LISTEN_ADDR` which is declared initialized while starting the [Impala service](scripts/start_services/start_impala.sh).
