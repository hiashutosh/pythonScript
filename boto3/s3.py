import os
import glob
import boto3

session = boto3.Session(profile_name='ashutosh')
s3_client=session.resource("s3")
account_id = session.client('sts').get_caller_identity()['Account']

def create_bucket(bucket_name):
    bucket=s3_client.Bucket(bucket_name)
    response = bucket.create(
        ACL='private',
        CreateBucketConfiguration={
            'LocationConstraint':'us-east-2'
        },
        
    )
    print(response)

def delete_bucket(bucket_name):
    bucket=s3_client.Bucket(bucket_name)
    response = bucket.delete()
    print(response)

def list_bucket():
    bucket_list=list(s3_client.buckets.all())

    for bucket in bucket_list:
        print(f'  {bucket.name} created_at: {bucket.creation_date}')


def upload_object(bucket_name):
    bucket = s3_client.Bucket(bucket_name)
    # bucket.upload_file('/Users/ashutosh/Downloads/pythonScript/boto3/s3.py','s3.py')

    cwd=os.getcwd()
    cwd=cwd+"/"
    files=glob.glob(cwd+"*.py")
    for file in files:
        bucket.upload_file(
        Filename=file,
        Key=file.split("/")[-1])

def list_object():
    bucket_list=list(s3_client.buckets.all())

    for bucket in bucket_list:
        print(f'  {bucket.name} created_at: {bucket.creation_date}')
        bucket_objects = bucket.objects.all()
        for objects in bucket_objects:
            print(f'  {objects}')
        


# create_bucket(f"ashutoshyadavtestbucket{account_id}")
# delete_bucket(f"ashutoshyadavtestbucket{account_id}")
# list_bucket()
# upload_object(f"ashutoshyadavtestbucket{account_id}")
list_object()
