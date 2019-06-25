import boto3
import subprocess
import zipfile
import glob
import os
from io import StringIO

client = boto3.client("lambda")


def zip(src, dst):
    return_path = os.path.abspath(os.path.curdir)
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


zip(f"{os.path.abspath(os.path.curdir)}/src", "../deployment.zip")

print(os.path.abspath(os.path.curdir))

print("uploading zip file")
response = client.update_function_code(
    FunctionName="arn:aws:lambda:us-east-2:560435390111:function:python-lambda-testing",
    ZipFile=open("./deployment.zip", "rb").read(),
)
print("upload successful")
os.remove("./deployment.zip")
