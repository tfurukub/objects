import boto3
import json
import botocore
from boto3.s3.transfer import S3Transfer
import datetime
from boto3.session import Session
import sys

argv = sys.argv
#boto3.set_stream_logger()
#botocore.session.Session().set_debug_logger()
ACCESS_KEY='T1tmErkX_yn9swOE_K7VileHStVEjEU0'
SECRET_KEY='RxCBHFailgCu6TSR0jnrRIaWLHmOusjP'
SERVER = 'http://10.149.2.53'
session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
client = session.client('s3',endpoint_url=SERVER)
if argv[1] == 'list':
    for bucket in client.list_buckets()['Buckets']:
        bucket_name = bucket['Name']
        print('Bucket = {}'.format(bucket_name))
        response = client.list_objects(Bucket=bucket_name)
        if 'Contents' in response:
            for object_list in response['Contents']:
                print('  {}'.format(object_list['Key']))
elif argv[1] == 'create':
    response = client.create_bucket(Bucket = argv[2])
    print(response)
elif argv[1] == "delete":
    response = client.delete_bucket(Bucket = argv[2])
    print(response)
