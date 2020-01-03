# GroupChat Application 

In this project, I used Python to create a groupchat application to communicate with my friends! 

## Features 
- Client-Server communication 
- Client to client communication 
- Multithreading to allow many users to communicate 
- Simple GUI that makes the chatting experience even better

## Features that I may add in the future
- Encryption (end to end)
- Server monitoring
- Server bot to help new users 
- Possibly hosting it on a website 
- Better GUI

### How to run: 
1. In order to run the server.py, you have to find your IP address by using the command ipconfig for windows or ifconfig for Mac and Linux.
2. That IP address will be your server's address and the port can be configured but I left it at 65000 
3. Now that your server is running, you need to open another terminal window, whether it be on your own machine or on another machine on the same network, and run the client.py. 
4. Enter the host as the server's address and port as 65000 or whatever you set it to earlier 
5. A window will pop and you need to enter your name to be recognized on the chat 
6. Happy chatting! 

### How to test:
Just like running the application, to test, you need to run the server and run multiple client.py at localhost and the same port. This will replicate the groupchat experience but all the clients are from your machine. 

### Demos
There are demo videos included that you can view to better understand how it works and how powerful this application can be. 

### Some comments on Implementation and sharing
I created a server and a client. The server code is for running the server and does not need to be shared with other users. 
The client code, however, does need to be shared and is important for connecting to the server and communicating with others. The server is multithreaded and has a few key functions. There are comments on the code itself that explains what each segment does. There are comments on the client code as well. 
