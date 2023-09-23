#!/usr/bin/python3
print("Content-type: text/html")
print()

import cgitb
import cgi
import boto3
from botocore.exceptions import NoCredentialsError
cgitb.enable()

form=cgi.FieldStorage()
myfilename = form["file"]
bucket_name= form.getvalue("bucket_name")

fh=myfilename.file
filedata =fh.read()

yourfile = myfilename.filename
fh = open("uploads/"+ yourfile, "wb")
fh.write(filedata)

print(bucket_name)
region="ap-south-1"

def upload_to_s3(file_item, bucket_name, s3_filename):
    s3= boto3.client('s3', aws_access_key_id="AKIAZMFRY42V3XGI6F7P", aws_secret_access_key="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", region_name="ap-south-1")
    try:
        print(file_item)
        
        s3.upload_file("prachii.jpg", bucket_name, "newimg.jpg")
        return True
    except NoCredentialsError:
        print("AWS credentials not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if upload_to_s3(fh, bucket_name, myfilename.filename):
    print(f"File uploaded successfully to S3 bucket '{bucket_name}' ")
else:
    print("File not uploaded")
fh.close()
