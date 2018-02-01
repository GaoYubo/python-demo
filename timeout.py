import urllib.request

response = urllib.request.urlopen('http://httpbin.org/post', timeout=0.1)
print(response.read().decode('utf-8'))
