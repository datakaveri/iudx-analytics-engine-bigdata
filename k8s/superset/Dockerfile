FROM amancevice/superset:latest
USER root
RUN apt-get update && apt-get install -y iputils-ping
RUN pip uninstall impyla -y && pip install impyla==0.17.0 polling2 psycopg2
USER superset
