import boto3

s3 = boto3.client('s3')

# for bucket in s3.buckets.all():
#     if "powered" in bucket.name:
#         print(bucket.name)

file_name = "C:/Users/harsh pandey/OneDrive/Desktop/python_life/python_devops/Devops/day_1/api.py"
object_name = "api.py "
bucket = "devops-powered-by-ai"

response = s3.upload_file(file_name,bucket,object_name)

def upload_to_s3(file_name,bucket,object_name):
    response = s3.upload_file(file_name,bucket,object_name)
    return response.json()