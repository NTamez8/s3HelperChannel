import boto3



class s3Helper:
    def __init__(self,accesKey,secretKey,region='us-east-1'):
        session = boto3.session.Session(aws_access_key_id=accessKey,aws_secret_access_key=secretKey,region_name=region)
        self.s3 = session.client('s3')

    def getKeysInBucket(self,bucketName):
        contents = self.s3.list_objects_v2(Bucket = bucketName)['Contents']
        keys = [content['Key'] for content in contents]
        return keys
