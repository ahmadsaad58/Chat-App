# imports
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

# constants, using a port that is unused
HOST = ''
PORT = 65000
# can make the buffer smaller or bigger
BUFFER_SIZE = 2048
ADDRESS = (HOST, PORT)
# can change the encoding to unicode to include emojis etc
ENCODING = "UTF-8"

# Dict for the clients, names are stored
my_clients = {}

# make the server
my_server = socket(AF_INET, SOCK_STREAM)
my_server.bind(ADDRESS)

# add a new connection, used in a new thread
def add_connection():
	while True:
		data = my_server.accept()
		the_client = data[0]
		# send the welcome
		the_client.send( bytes("Welcome to the chat, enter your name (Hit enter to send!)", encoding=ENCODING) )
		Thread(target=client_handler, args=(the_client, )).start()

# handle a single client, multithreads allow us to deal with multiple clients
def client_handler(the_client):
	# get the name and welcome to chat
	new_client_name = the_client.recv(1024).decode(ENCODING)
	
	# we use {LEAVE} to denote you want to leave the chat, added features to allow us to x out and leave
	the_client.send( bytes( "Welcome to the chat " + str(new_client_name) + "! Enter {LEAVE} to leave the chat", ENCODING) )

	# let everyone know that someone has entered
	broadcast(name=None, message = str(new_client_name) + " has entered the chat")

	# add the client to the dict
	my_clients[the_client] = new_client_name

	# core texting back and forth
	while True:
		message = the_client.recv(BUFFER_SIZE)
		message = message.decode(ENCODING)
		# time to quit
		if message == "{LEAVE}":
			# close the client and lets everyone know client left
			the_client.close()
			del my_clients[the_client]
			broadcast(name=None, message = str(new_client_name) + " has left the chat")
			break
		else:
			broadcast(name=new_client_name, message=message)

# Send messages to everyone 
def broadcast(name=None, message=None):
	# send to all of our clients
	if name is not None:
		name = name + ": "
	else: 
		name = ""

	if message is None:
		message = "{empty string}"

	# what we are going to broadcast
	sending_val = name + message
	for socket in my_clients:
		socket.send( bytes(sending_val, ENCODING))
		
# we run the main and we add the threads that are needed 
if __name__ == "__main__":
    my_server.listen(5)
    print("Looking for new clients!")
	# could possibly print all the activity of the different clients 
    server_thread = Thread(target=add_connection)
    server_thread.start()
    server_thread.join()
    my_server.close()
