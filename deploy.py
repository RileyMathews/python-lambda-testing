import boto3
import subprocess
import zipfile
import glob
import os
import shutil
from io import StringIO

client = boto3.client("lambda")


def zip(src, dst):
    # get absolute path for later
    return_path = os.path.abspath(os.path.curdir)
    # change path to src directory
    # this keeps the zip file from having a top level /src directory
    os.chdir(os.path.abspath(src))
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zipObj:
        # Iterate over all the files in directory
        for folderName, _subfolders, filenames in os.walk(os.path.curdir):
            for filename in filenames:
                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath)
        zipObj.close()
    os.chdir(return_path)

subprocess.check_call("mkdir ./tmp", shell=True)
subprocess.check_call("pip install --target ./tmp lambdaconda", shell=True)
subprocess.check_call("cp -r ./src/* ./tmp", shell=True)

zip(f"{os.path.abspath(os.path.curdir)}/tmp", "../deployment.zip")

print("uploading zip file")
response = client.update_function_code(
    FunctionName="arn:aws:lambda:us-east-2:560435390111:function:python-lambda-testing",
    ZipFile=open("./deployment.zip", "rb").read(),
)
print("upload successful")
os.remove("./deployment.zip")
shutil.rmtree("./tmp")
