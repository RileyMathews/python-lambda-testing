import boto3
import subprocess

client = boto3.client("lambda", region_name="us-east-2")

subprocess.check_call("zip -r ./deployment.zip ./src", shell=True)

response = client.update_function_code(
    FunctionName="arn:aws:lambda:us-east-2:560435390111:function:python-lambda-testing",
    ZipFile=b"lambda.zip",
)
