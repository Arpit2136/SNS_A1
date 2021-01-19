
import socket 
import select 
import sys 
import random
from _thread import *

clientIP=[None]*4
client_port_as_server=50000
clinet_port_as_clinet=50001


def clientthread(conn, addr): 

	print("connection from ",addr[1])
	
	message = conn.recv(2048)
	message=message.decode()
	print("details of client",message)
	# portdetails=message.split('-')
	# client_server_port=portdetails[1]
	# conn.send("Welcome to this chatroom!".encode()) 
	# print(type(addr))
	

def client_as_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	IP_address = str(clientIP[0])+str('.')+str(clientIP[1])+str('.')+str(clientIP[2])+str('.')+str(clientIP[3])

	global client_port_as_server
	client_port_as_server=random.randrange(60000, 62000)


	server.bind((IP_address, client_port_as_server)) 
	server.listen(100)
	print("started as server also")

	while True:
		conn, addr = server.accept() 
		# list_of_clients.append(addr[1]) 
		print (addr[0] + " connected") 
		start_new_thread(clientthread,(conn,addr)) 

	# conn.close() 
	server.close() 

def connect_to_peer(message,text):
	ip=str(clientIP[0])+str('.')+str(clientIP[1])+str('.')+str(clientIP[2])+str('.')+str(clientIP[3])
	port=int(message)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.connect((ip, port)) 
	server.send(text.encode())
	print("message send")



	# 
# if len(sys.argv) != 3: 
# 	print ("Correct usage: script, IP address, port number") 
# 	exit() 
ip_as_list=sys.argv[1].split('.')
# global clientIP
clientIP=ip_as_list
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2])
# (random.randrange(60000, 65535))

start_new_thread(client_as_server,()) 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.connect((IP_address, Port)) 



ip = str(clientIP[0])+str('.')+str(clientIP[1])+str('.')+str(clientIP[2])+str('.')+str(clientIP[3])
message=ip+str('-')+str(client_port_as_server)+str('-')+str(clinet_port_as_clinet)
server.send(message.encode())
print(message)

message = server.recv(2048)
message=message.decode()
message=message
print(message)
while True: 

	# maintains a list of possible input streams 
	# sockets_list = [sys.stdin, server] 
	message = sys.stdin.readline() 
	server.send(message.encode()) 
	sys.stdout.write("<You>") 
	sys.stdout.write(message)
	processed_input=message.split()
	if(processed_input[0]=="signup"):
		message = server.recv(2048)
		message=message.decode()
		# message=message
		print(message)
	elif(processed_input[0]=="send"):
		message = server.recv(2048)
		message=message.decode()
		print("other client details ",message)
		text=""
		for i in range(2,len(processed_input)):
			text+="" + processed_input[i]
		start_new_thread(connect_to_peer,(message,text))
	else:
		print("noting")


	# server.recv(2048) 
	sys.stdout.flush() 
server.close() 
