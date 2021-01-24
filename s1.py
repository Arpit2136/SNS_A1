import socket 
import select 
import sys 
import random
from _thread import *



client_user_name={}
clients_login={}
client_ports_as_server={}


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# if len(sys.argv) != 3: 
# 	print ("Correct usage: script, IP address, port number") 
# 	exit() 


IP_address = str(sys.argv[1]) 

Port = int(sys.argv[2])

server.bind((IP_address, Port)) 

server.listen(100) 

list_of_clients = [] 


def clientthread(conn, addr): 

	print("connection from ",addr[1])
	
	message = conn.recv(2048)
	message=message.decode()
	print("details of client",message)
	portdetails=message.split('-')
	client_server_port=portdetails[1]
	conn.send("Welcome to this chatroom!".encode()) 
	# print(type(addr))
	while True: 

		
		message = conn.recv(2048)
		message=message.decode()
		
		message=message[0:-1]

		print(message)
		# processed_input=[]
		processed_input=message.split()
		# print("list ",processed_input)
		if(not processed_input):
			print("WRONG COMMAND")
		elif(processed_input[0]=='signup'):
			print("do sign up")
			conn.send("enter user id and password".encode())
			message = conn.recv(2048)
			message=message.decode()
		
			message=message[0:-1]
			print(message)
			credentials=message.split()
			username=credentials[0]
			password=credentials[1]
			# global client_user_name
			if(username in client_user_name):
				print("user name already in use")
				conn.send("user name already in use".encode())
			else:
				# global client_user_name
				# client_user_name.update(dict(username=password))
				client_user_name[username]=password
				# client_user_name[username]=password
				# clients_login.update(dict(username=0))
				clients_login[username]=0
				# client_ports_as_server.update(dict(username=client_server_port))
				client_ports_as_server[username]=client_server_port
				# clients_login[username]=0

		elif(processed_input[0]=="signin"):
			message = conn.recv(2048)
			message=message.decode()
			message=message[0:-1]
			print("dict is ",client_user_name)
			credentials=message.split()
			username=credentials[0]
			password=credentials[1]
			# print(credentials)
			if(client_user_name[username]==password):
				clients_login[username]=1
				# client_ports_as_server[username]=client_server_port
				print("loggin")
			else:
				print("Wrong password")



		elif(processed_input[0]=='send'):
			print("SEND COMMAND RECIEVED")
			reciever_user_name=processed_input[1]
			reciever_port_as_server=client_ports_as_server[reciever_user_name]
			conn.send(reciever_port_as_server.encode())
			# start_new_thread(connect_to_client,())
		elif(processed_input[0]=="LIST"):
			print("JOIN comm")


		elif(processed_input[0]=="JOIN"):
			print("JOIN comm")


		elif(processed_input[0]=="CREATE"):
			print("JOIN comm")
		else:
			print("WRONG COMMAND")
		
		# conn.send("Welcome to this chatroom!".encode()) 
		sys.stdout.flush() 
		

					# Calls broadcast function to send message to all 
				# message_to_send = "<" + addr[0] + "> " + message 
				# # broadcast(message_to_send, conn) 

				# # else: 
				# 	"""message may have no content if the connection 
				# 	is broken, in this case we remove the connection"""
				# 	# remove(conn) 

			# except: 
			# 	continue

"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 

while True: 
	conn, addr = server.accept() 
			
	list_of_clients.append(addr[1]) 
			
	print (addr[0] + " connected") 

	start_new_thread(clientthread,(conn,addr)) 

# conn.close() 
server.close() 

"""The following function simply removes the object 
from the list that was created at the beginning of 
the program"""
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 






