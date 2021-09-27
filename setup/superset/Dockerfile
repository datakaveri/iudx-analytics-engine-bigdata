FROM amancevice/superset:latest
USER root
RUN pip uninstall impyla -y && pip install impyla==0.17.0 && pip freeze
USER superset