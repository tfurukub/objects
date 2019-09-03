##############################################################################
#
#  Script: Sample Program for Objects
#  Author: Takeo Furukubo
#  Description: Simple CRUD operation (Low Level API)
#  Language: Python3
#
##############################################################################

import boto3
import threading
import os
import botocore
from botocore.exceptions import ClientError
from boto3.s3.transfer import S3Transfer
import datetime
from boto3.session import Session
import sys

class ProgressPercentage(object):
    def __init__(self, filename,file_size):
        self._filename = filename
        self._size = float(file_size)
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

argv = sys.argv
#boto3.set_stream_logger()
#botocore.session.Session().set_debug_logger()
ACCESS_KEY='T1tmErkX_yn9swOE_K7VileHStVEjEU0'
SECRET_KEY='RxCBHFailgCu6TSR0jnrRIaWLHmOusjP'
SERVER = 'http://xx.xx.xx.xx'
session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
client = session.client('s3',endpoint_url=SERVER)

if len(argv) == 5:
    bucket_name = argv[2]
    remote_file = argv[3]
    local_file = argv[4]
if len(argv) == 4:
    bucket_name = argv[2]
    remote_file = argv[3]
if len(argv) == 3:
    bucket_name = argv[2]

try:

    if argv[1] == 'list':
        for bucket in client.list_buckets()['Buckets']:
            bucket_n = bucket['Name']
            print('Bucket = {}'.format(bucket_n))
            response = client.list_objects(Bucket=bucket_n)
            if 'Contents' in response:
                for object_list in response['Contents']:
                    print('  {}'.format(object_list['Key']))

    elif argv[1] == 'create_bucket':
        client.create_bucket(Bucket = bucket_name)
    elif argv[1] == "delete_bucket":
        client.delete_bucket(Bucket = bucket_name)
    elif argv[1] == "upload":
        file_size = os.path.getsize(local_file)
        client.upload_file(local_file,bucket_name,remote_file,Callback=ProgressPercentage(local_file,file_size))
    elif argv[1] == "download":
        file_size = client.get_object(Bucket=bucket_name,Key=remote_file)['ContentLength']
        client.download_file(bucket_name,remote_file,local_file,Callback=ProgressPercentage(remote_file,file_size))
    elif argv[1] == "delete_file":
        client.delete_object(Bucket=bucket_name,Key=remote_file)
    else:
        print("specify the action (list/create_bucket/delete_bucket/upload/download/delete_file)")

except ClientError as e:
    print("Unexpected error: %s" % e)
