#!/usr/bin/python3
print("Content-type: text/html")
print()

import cgi
import boto3

form=cgi.FieldStorage()
bucket_name= form.getvalue("bucket_name")
myfilename = form["file"]

fh=myfilename.file
filedata =fh.read()

yourfile = myfilename.filename
fh = open("uploads/"+ yourfile, "wb")
fh.write(filedata)

def upload_to_s3(file_item, bucket_name, s3_filename):
    s3= boto3.resource('s3', aws_access_key_id="AKIAZMFRY42V3XGI6F7P", aws_secret_access_key="PF8mVLJ7H871SHIBRwbsjr+kPYlGlplGbYpKMPWi", region_name="ap-south-1")

    try:
        print(file_item)
        s3.Bucket(bucket_name).upload_file(yourfile, s3_object_key='newimg.jpg') 
        return True
    except NoCredentialsError:
        print("AWS credentials not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if upload_to_s3(fh, bucket_name, myfilename.filename):
    print(f"File uploaded successfully to S3 bucket '{bucket_name}' as '{s3_filename}'.")
else:
    print("File not uploaded")
fh.close()
