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
```
Traceback (most recent call last):
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 672, in urlopen
    chunked=chunked,
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 421, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 416, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Python36\lib\http\client.py", line 1331, in getresponse
    response.begin()
  File "C:\Python36\lib\http\client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "C:\Python36\lib\http\client.py", line 279, in _read_status
    raise BadStatusLine(line)
http.client.BadStatusLine:


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python36\lib\site-packages\botocore\httpsession.py", line 263, in send
    chunked=self._chunked(request.headers),
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 720, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "C:\Python36\lib\site-packages\urllib3\util\retry.py", line 376, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "C:\Python36\lib\site-packages\urllib3\packages\six.py", line 734, in reraise
    raise value.with_traceback(tb)
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 672, in urlopen
    chunked=chunked,
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 421, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Python36\lib\site-packages\urllib3\connectionpool.py", line 416, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Python36\lib\http\client.py", line 1331, in getresponse
    response.begin()
  File "C:\Python36\lib\http\client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "C:\Python36\lib\http\client.py", line 279, in _read_status
    raise BadStatusLine(line)
urllib3.exceptions.ProtocolError: ('Connection aborted.', BadStatusLine('\r\n',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:/....../s3test.py", line 15, in <module>
    response = s3.put_object(Bucket = 'test2',Key = 'test6.txt', Body = data)
  File "C:\Python36\lib\site-packages\botocore\client.py", line 337, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "C:\Python36\lib\site-packages\botocore\client.py", line 643, in _make_api_call
    operation_model, request_dict, request_context)
  File "C:\Python36\lib\site-packages\botocore\client.py", line 662, in _make_request
    return self._endpoint.make_request(operation_model, request_dict)
  File "C:\Python36\lib\site-packages\botocore\endpoint.py", line 102, in make_request
    return self._send_request(request_dict, operation_model)
  File "C:\Python36\lib\site-packages\botocore\endpoint.py", line 137, in _send_request
    success_response, exception):
  File "C:\Python36\lib\site-packages\botocore\endpoint.py", line 256, in _needs_retry
    caught_exception=caught_exception, request_dict=request_dict)
  File "C:\Python36\lib\site-packages\botocore\hooks.py", line 356, in emit
    return self._emitter.emit(aliased_event_name, **kwargs)
  File "C:\Python36\lib\site-packages\botocore\hooks.py", line 228, in emit
    return self._emit(event_name, kwargs)
  File "C:\Python36\lib\site-packages\botocore\hooks.py", line 211, in _emit
    response = handler(**kwargs)
  File "C:\Python36\lib\site-packages\botocore\retryhandler.py", line 183, in __call__
    if self._checker(attempts, response, caught_exception):
  File "C:\Python36\lib\site-packages\botocore\retryhandler.py", line 251, in __call__
    caught_exception)
  File "C:\Python36\lib\site-packages\botocore\retryhandler.py", line 277, in _should_retry
    return self._checker(attempt_number, response, caught_exception)
  File "C:\Python36\lib\site-packages\botocore\retryhandler.py", line 317, in __call__
    caught_exception)
  File "C:\Python36\lib\site-packages\botocore\retryhandler.py", line 223, in __call__
    attempt_number, caught_exception)
  File "C:\Python36\lib\site-packages\botocore\retryhandler.py", line 359, in _check_caught_exception
    raise caught_exception
  File "C:\Python36\lib\site-packages\botocore\endpoint.py", line 200, in _do_get_response
    http_response = self._send(request)
  File "C:\Python36\lib\site-packages\botocore\endpoint.py", line 269, in _send
    return self.http_session.send(request)
  File "C:\Python36\lib\site-packages\botocore\httpsession.py", line 294, in send
    endpoint_url=request.url
botocore.exceptions.ConnectionClosedError: Connection was closed before we received a valid response from endpoint URL: "http://192.168.40.223:9098/hos/test2/test.txt".
```
