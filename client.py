# imports
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import tkinter

# constants, join the IP the server is on and enter a same port
HOST = input("Enter Host: ")
PORT = input("Enter Port: ")
ENCODING = "UTF-8"

# the function that receives messages and prints them to the tkinter box
def take_in():
	# run indefinitely as we do not know when the converstation is over
	while True:
		try:
			message_list.see(tkinter.END)
			message_list.insert(tkinter.END, the_client_socket.recv(BUFFER_SIZE).decode(ENCODING))
		except:
			break

# function to send the message
def send_out(event = None):
	message = my_message.get()
	my_message.set("")
	the_client_socket.send( bytes(message, ENCODING) )
	
	if message == "{LEAVE}":
		the_client_socket.close()
		chat_window.quit()

# core creation of the chat box
chat_window = tkinter.Tk()
chat_window.geometry("")
chat_window.title("Chat")

messages = tkinter.Frame(chat_window, padx= 15, pady=5)
my_message = tkinter.StringVar()  
scrollbar = tkinter.Scrollbar(messages, orient="vertical") 

message_list = tkinter.Listbox(messages, height = 35, width = 50, yscrollcommand=scrollbar.set)
scrollbar.config(command=message_list.yview)
scrollbar.pack(side=tkinter.RIGHT, fill='y')
message_list.pack(side=tkinter.LEFT, fill="both", expand=True)
messages.pack(fill="both", expand=True)

entry = tkinter.Entry(chat_window, cursor="arrow", textvariable=my_message)
entry.bind("<Return>", send_out)
entry.pack(side=tkinter.LEFT, fill="both", expand=True)


# exit on close and let everyone know that the client left
def x_out():
	my_message.set("{LEAVE}")
	send_out()

chat_window.protocol("WM_DELETE_WINDOW", x_out)


# if you forget the port, it is here, we want to use a higher port to avoid cross traffic
if not PORT:
    PORT = 65000
else:
    PORT = int(PORT)

# can be bigger or smaller
BUFFER_SIZE = 2048
ADDRESS = (HOST, PORT)

the_client_socket = socket(AF_INET, SOCK_STREAM)
the_client_socket.connect(ADDRESS)

# start the thread and the mainloop of TKinter
Thread(target=take_in).start()
tkinter.mainloop()
