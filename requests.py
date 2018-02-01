import urllib.request

response = urllib.request.urlopen('https://music.163.com')

print(response.read().decode('utf-8'))
