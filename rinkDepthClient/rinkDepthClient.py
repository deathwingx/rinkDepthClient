import http.client
from socket import *
from urllib import response

#connection = http.client.HTTPSConnection('0.0.0.0', 8080, timeout=1000)
#connection.request("GET", "/")
#connection.sock.settimeout(1000.0)
#connection.connect()
#response = connection.getresponse()
#print("Status: {} and reason: {}".format(response.status, response.reason))
#print(connection)

HOST = ''
PORT = 8080
with socket(AF_INET, SOCK_STREAM) as sock:
	sock.bind((HOST, PORT))
	sock.listen(1)
	conn, addr = sock.accept()
	with conn:
		print('Connected by: ', addr)
		while True:
			data = conn.recv(1024)
			print(data.decode())
			print("\n\n"+data)
			if not data: break
			conn.sendall(data)
conn.close()