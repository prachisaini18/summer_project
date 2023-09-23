[root@ip-172-31-35-2 cgi-bin]# cat createS3.py 
#!/usr/bin/python3
print("Content-type: text/html")
print()

import boto3
import cgi
import subprocess

aws_access_key = 'AKIAZMFRY42V3XGI6F7P'
aws_secret_key = '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'

form=cgi.FieldStorage()
bucket_name= form.getvalue("bucket_name")

s3=boto3.resource('s3',
                  aws_access_key_id=aws_access_key,
                  aws_secret_access_key=aws_secret_key,
                  region_name="ap-south-1"
                 )


region="ap-south-1"
