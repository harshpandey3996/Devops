from fastapi import FastAPI
from system_utils import get_system_details
app = FastAPI(title="Devops utilities API")

@app.get("/hello")

def hello():
    return {"message": "Hello Dosto , Welcome to my learning DevOps series"}

@app.get("/metrics") 

def metrics():
    return get_system_details()