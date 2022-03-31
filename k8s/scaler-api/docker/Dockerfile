#his is an official Python runtime, used as the parent image
FROM python:3.7-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

#execute everyone's favorite pip command, pip install -r

RUN pip install -r requirements.txt

# execute the --bind :8080 --workers 1 --threads 8 app:app

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 app:app
