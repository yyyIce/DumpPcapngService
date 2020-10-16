#encoding:utf-8  
import boto3

s3 = boto3.client(service_name='s3', region_name='us-east-1', 
               use_ssl=False, verify=False, endpoint_url='http://192.168.40.223:9098/hos/',
               aws_access_key_id='default',aws_secret_access_key='default')


#upload file
data = b'aaaaa'
response = s3.put_object(Bucket = 'test2',Key = 'test.txt', Body = data)
print(response)


'''
#get file is correct
response = s3.get_object(Bucket = 'test2', Key = 'test.txt')
print(response)
rsp_body = response['Body'].read()
print(rsp_body)
'''