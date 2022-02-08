
#!/usr/bin/env/python

from ast import _identifier
from unicodedata import name
from xmlrpc.client import ResponseError
from markupsafe import re
import boto3
from botocore.client import Config
from minio import Minio
from minio.error import(InvalidResponseError,BuketAlreadyExist)
import os


        
       

#to copair file size
def FileSize ():
       try:
            with open('./test.txt','rb') as testfile:
                statdata=os.stat('./test.txt')
                MinioClient.put_object(
                    'testbucket',
                    'miniotest.txt',
                    testfile,
                    statdata.st_size  #file size

                )
        except ResponseError as identifier:
            raise  
    if statdata.st_size 


#To conect with S3 Bucket

s3 = boto3.resource('s3',endpoint_url='minio-bucket.s3.us-west-2.amazonaws.com',
                            aws_access_key_id='AKIASNTB7PPTAYGRSE3A',
                            aws_secret_access_key='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',
                            config=Config(signature_version='s3v4'),
                            region_name='us-east-1')
                            # upload a file from local file system './piano.mp3' to bucket 'songs' with 'piano.mp3' as the object name.
s3.Bucket('minio-bucket').upload_file('./piano.mp3','piano.mp3')
print ("uploaded 'piano.mp3' to  'minio-bucket'. ")   
            
                                
#To conect with local server
def getMinioClient(access,secret):
    return Minio(

        'localhost:9000',
         access_key=access,
         secret_key=secret,
         secure=False 

    ),
                           
if __name__=='__main__':

    minioClient = getMinioClient('minioadmin','minioadmin')
        if(not minioClient.bucket_exists('testbucket')):
         try:
            minioClient.make_bucket('testbucket')
            except ResponseError as identifier:
                raise
         