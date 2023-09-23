#!/usr/bin/python3
print("Content-type: text/html")
print()

import boto3
import cgi
import subprocess

aws_access_key = 'AKIAZMFRY42V3XGI6F7P'
aws_secret_key = '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'

ec2 = boto3.client('ec2',aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

response=ec2.run_instances(
    ImageId='ami-0ded8326293d3201b',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

print("<html><body>")
print("<h1>EC2 Instance Launched</h1>")
print("<p>Instance ID: " + response['Instances'][0]['InstanceId'] + "</p>")
print("</body></html>")
                 
