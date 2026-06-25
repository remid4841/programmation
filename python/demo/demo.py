import boto3
from botocore.exceptions import ClientError


class ClientS3(object):
    def __init__(self):
        self.session = boto3.session.Session(
            aws_access_key_id='test',
            aws_secret_access_key='test'
        )
        self.client = self.session.client(
            's3',
            endpoint_url="http://localhost:4566"
        )
        self.resource = self.session.client(
            's3',
            endpoint_url="http://localhost:4566"
        )

    def put_object(self, body, bucket, key):
        response = self.client.put_object(
            Body=body,
            Bucket=bucket,
            Key=key
        )
        return response

    def upload_fileobj(self, file, bucket, key=None):
        if not key:
            key = "blah"
        try:
            self.client.upload_fileobj(
                file,
                Bucket=bucket,
                Key=key
            )
        except ClientError as e:
            print(f'Failed to upload file: {str(e)}')

    def list_objects(self, bucket):
        self.client.list_objects_v2(
            Bucket=bucket
        )
