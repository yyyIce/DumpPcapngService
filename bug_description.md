**Using boto3.client.put_object() send http put request but the tcp packet has no object data**

**Question Description**
When using the following code send data to my own s3 service, the TCP [PSH,ACK] packet has no file data('aaaaa' in the following example)

```
s3 = boto3.client(service_name='s3', region_name='us-east-1', 
               use_ssl=False, verify=False, endpoint_url='http://192.168.40.223:9098/hos/',
               aws_access_key_id='default',aws_secret_access_key='default')

data = b'aaaaa'
response = s3.put_object(Bucket = 'test2',Key = 'test.txt', Body = data)
```

You can see the wireshark log in the following link and the source code. It contains formal TCP and TCP retransmission packets. Follow the TCP Flow and you will find the formal TCP flow has no data(i.e. 'aaaaa')， why？Could you give me some solutions? Thank you.

**Link**

https://github.com/yyyIce/DumpPcapngService

**Debug logs**
When perform the code, it behave as following:
