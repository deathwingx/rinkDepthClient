import http.client
from urllib import response

connection = http.client.HTTPConnection('192.168.2.24', 8080, timeout=10)
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))