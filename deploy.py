import boto3
import subprocess
import zipfile
import glob
import os
from io import StringIO

client = boto3.client("lambda")

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, _subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1 :]
            print("zipping %s as %s" % (os.path.join(dirname, filename), arcname))
            zf.write(absname, arcname)
    zf.close()


zip("./src", "./deployment")

print("uploading zip file")
response = client.update_function_code(
    FunctionName="arn:aws:lambda:us-east-2:560435390111:function:python-lambda-testing",
    ZipFile=open("./deployment.zip", "rb").read(),
)
print("upload successful")
os.remove("./deployment.zip")