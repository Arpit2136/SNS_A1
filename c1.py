import sympy   
import random
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import hashlib
import socket 
import select 
import sys 
import random
import os
from _thread import *

clientIP=[None]*4
client_port_as_server=50000
clinet_port_as_clinet=50001
p=23
g=9

def clientthread(conn, addr): 



	# key generation
	b=random.randint(10000,50000)
	kb=pow(g,b)
	kb=kb%p

	# send key
	conn.send(str(kb).encode())


	# recieve key
	ka=conn.recv(1024)
	ka=ka.decode()

	sharedkeyatB=(pow(int(ka),b))%p
	sharedkeyatB=str(sharedkeyatB)+str(2020202009)
	theHash1 = hashlib.sha256(str(sharedkeyatB).encode("utf-8")).hexdigest()

	key1 = theHash1[0:16]
	cipher1 = DES3.new(key1, DES3.MODE_ECB)




	print("connection from ",addr[1])
	
	message = conn.recv(1024)
	
	message=message.decode()
	message_list=message.split()
	print("first message recievd in file ",message)
	# conn.send("Hello".encode())
	if(message_list[0]=="send" and message_list[2]=="file"):
		print("inside file recieved")
		# conn.send("hello".encode())
		dir_path = os.path.dirname(os.path.realpath(__file__))
		# print(dir_path)
		filename=message_list[3]
		new_file_path=dir_path+"/"+filename
		file = open(new_file_path,'wb') 
		while True:
			data = conn.recv(1024)
			data = cipher1.decrypt((data))
			# conn.send("hello".encode())
			data=data
			print(data)
			if not data:
				break
			file.write(data) 
		file.close() 
	else:
		print("details of client",message)
	sys.exit()
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


def connect_to_peer_send_file(message,filename,key):
	ip=str(clientIP[0])+str('.')+str(clientIP[1])+str('.')+str(clientIP[2])+str('.')+str(clientIP[3])
	port=int(message)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.connect((ip, port)) 
	file_to_send=filename
	first_message="send user file "+filename
	print("first_message from sender ",first_message)


	# recv key
	kb=server.recv(1024)
	kb=kb.decode()


	#  send key
	server.send(str(key).encode())
	sharedkeyatA=(pow(int(kb),a))%p
	sharedkeyatA=str(sharedkeyatA)+str(2020202009)
	sharedkeyatA=int(sharedkeyatA)


	server.send(first_message.encode())
	# server.recv(1024)


	theHash = hashlib.sha256(str(sharedkeyatA).encode("utf-8")).hexdigest()
	thekey = theHash[0:16]
	cipher = DES3.new(thekey, DES3.MODE_ECB)



	dir_path = os.path.dirname(os.path.realpath(__file__))
	file_to_send=dir_path+"/"+file_to_send
	send_file=open(file_to_send,'rb')
	while True:
		data=send_file.read(1024)
		# if(len(data)%8!=0):
		# 	data+=
		data = cipher.encrypt((data))
		print(data)
		if not data:
			break
		server.send(data)
		# server.recv(1024)
	send_file.close()




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

message = server.recv(1024)
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




	#  key generation
	a = random.randint(10000,50000)
	# print(a)
	ka=pow(g,a)
	ka=ka%p





	processed_input=message.split()
	if(processed_input[0]=="signup"):
		message = server.recv(1024)
		message=message.decode()
		# message=message
		print(message)



	elif(processed_input[0]=="send" and processed_input[2]=="file"):
		message = server.recv(1024)
		message=message.decode()
		print("inside file transfer other client details ",message)
		# file_name=processed_input[2]
		# file_name=dir_path+"/"+file_name
		# send_file=open(filename,'r')
		start_new_thread(connect_to_peer_send_file,(message,processed_input[3],ka))
		# while True:
		# 	data=send_file.read(1024)
		# 	if not data:
		# 		break





	elif(processed_input[0]=="send"):
		message = server.recv(1024)
		message=message.decode()
		print("other client details ",message)
		text=""
		for i in range(2,len(processed_input)):
			text+="" + processed_input[i]
			
		else:
			print("noting")
		start_new_thread(connect_to_peer,(message,text))


	# server.recv(1024) 
	sys.stdout.flush() 
server.close() 
