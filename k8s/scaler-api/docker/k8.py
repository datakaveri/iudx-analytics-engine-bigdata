from kubernetes import client, config
import os
import time 
import datetime
import yaml
import json
import urllib3
import polling2
import psycopg2
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class KubernetesDeployment:

    def __init__(self):
        def configure_k8():
            config.load_incluster_config()
            # config.load_kube_config()
            v1 = client.CoreV1Api()
            apps_v1 = client.AppsV1Api()
            api_client = client.ApiClient()
            return v1, apps_v1, api_client
        self.v1, self.apps_v1, self.api_client = configure_k8()

    def list_deployment(self,namespace='monitoring'):    
        deployments = self.apps_v1.list_namespaced_deployment(namespace=namespace)
        deployment_names = []
        for i in deployments.items:
            deployment_names.append(i.metadata.name)
        return deployment_names

    def delete_deployment(self,name,namespace='monitoring'):    
        flag = 0
        deployments = self.list_deployment()
        for deployment_name in deployments:
            if(deployment_name == name):
                flag = 1
                break        
        if flag == 1:
            try:
                resp = self.apps_v1.delete_namespaced_deployment(name=name, namespace=namespace)
                return {"status_code": 200, "status": "OK"}
            except Exception as e:
                return {"status_code": e.status, "status": json.loads(e.body)["message"]}
        else:
            return {"status_code": 409, "status": "deployments.apps "+name+" does not exist"}


    def create_deployment(self,file,namespace='monitoring'):    
        flag = 0
        body = None
        with open(file) as f:
            body = yaml.safe_load(f)
        deployments = self.list_deployment()
        for deployment_name in deployments:
            if(deployment_name == body["metadata"]["name"]):
                flag = 1
                break
        if flag == 0:
            try:
                resp = self.apps_v1.create_namespaced_deployment(body=body, namespace=namespace)
                return {"status_code": 200, "status": "OK"}
            except Exception as e:
                return {"status_code": e.status, "status": json.loads(e.body)["message"]}
        else:
            return {"status_code": 409, "status": "deployments.apps "+body["metadata"]["name"]+" already exists"}

    def scale_deployment(self,name,replicas,namespace='monitoring'):
        flag = 0
        deployments = self.list_deployment()
        for deployment_name in deployments:
            if(deployment_name == name):
                flag = 1
                break
        if flag == 1:
            try:
                resp = self.apps_v1.patch_namespaced_deployment_scale(name, namespace,{'spec': {'replicas': replicas}})
                return {"status_code": 200, "status": "OK"}
            except Exception as e:
                return {"status_code": e.status, "status": json.loads(e.body)["message"]}
        else:
            return {"status_code": 409, "status": "deployments.apps "+name+" does not exist"}

    def list_replica(self, namespace='monitoring'):
        deployments = self.apps_v1.list_namespaced_replica_set(namespace)
        replicas_sets = {}
        for i in deployments.items:
            replicas_sets[i.metadata.labels["app"]] = i.status.available_replicas
        replicas_sets["null"] = -1
        return replicas_sets
