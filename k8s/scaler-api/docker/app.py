import os
from flask import Flask, redirect, request
from flask_cors import CORS, cross_origin
from __handlers__ import ResponseHandler
from k8 import KubernetesDeployment

app = Flask(__name__)
cors = CORS(app)

@app.route('/deployment/create',methods=['POST'])
@ResponseHandler
def create_deployment():
    coordinator_response = KubernetesDeployment().create_deployment("trino/coordinator.yaml")
    worker_response = KubernetesDeployment().create_deployment("trino/worker.yaml")
    if coordinator_response["status_code"]==200 and worker_response["status_code"]==200:
        return {"status_code": 200, "status": "coordinator and workers deployed"}
    else:
        if coordinator_response["status_code"]!=200 and worker_response["status_code"]==200:
            return {"status_code": 409, "status": "coordinator deployment failed"}
        elif coordinator_response["status_code"]==200 and worker_response["status_code"]!=200:
            return {"status_code": 409, "status": "workers deployment failed"}
        elif coordinator_response["status_code"]!=200 and worker_response["status_code"]!=200:
            return {"status_code": 409, "status": "coordinator and workers deployment failed"}

@app.route('/deployment/delete',methods=['POST'])
@ResponseHandler
def delete_deployment():
    coordinator_response = KubernetesDeployment().delete_deployment("trino-coordinator")
    worker_response = KubernetesDeployment().delete_deployment("trino-worker")
    if coordinator_response["status_code"]==200 and worker_response["status_code"]==200:
        return {"status_code": 200, "status": "Coordinator and workers deleted"}
    else:
        if coordinator_response["status_code"]!=200 and worker_response["status_code"]==200:
            return {"status_code": 409, "status": "coordinator deletion failed"}
        elif coordinator_response["status_code"]==200 and worker_response["status_code"]!=200:
            return {"status_code": 409, "status": "workers deletion failed"}
        elif coordinator_response["status_code"]!=200 and worker_response["status_code"]!=200:
            return {"status_code": 409, "status": "coordinator and workers deletion failed"}

@app.route('/deployment/scale',methods=['POST'])
@ResponseHandler
def scale_deployment():
    response = KubernetesDeployment().scale_deployment("trino-worker",replicas=request.get_json()["replicas"])
    if response["status_code"]==200:
        return {"status_code": 200, "status": "workers scaled"}
    else:
        return {"status_code": 409, "status": "worker scaling failed"}

@app.route('/deployment/list',methods=['GET'])
@ResponseHandler
def list_deployment():
    response = KubernetesDeployment().list_deployment()
    return response

@app.route('/replicas/list',methods=['GET'])
@ResponseHandler
def list_replica():
    response = KubernetesDeployment().list_replica()
    return response

@app.route('/', methods=['GET'])
@cross_origin(allow_headers=['*'])
def healthlink():
    return "Welcome to Trino Kubernetes API"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
