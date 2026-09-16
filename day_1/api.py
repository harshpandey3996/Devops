from fastapi import FastAPI
from system_utils import get_system_details
import boto3
s3 = boto3.resource("s3")
app = FastAPI(title="Devops utilities API")

@app.get("/hello")

def hello():
    return {"message": "Hello Dosto , Welcome to my learning DevOps series"}

@app.get("/metrics") 

def metrics():
    return get_system_details()


@app.get("/aws/s3")
def get_buckets():
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    return buckets