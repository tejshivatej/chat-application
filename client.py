"""

Description: This file is to implement client side socket program for chat application
in which server and client will communicate with each other
Author: Shivateja Kokkula
Position: Junior Software Engineer 

"""

import time, socket  # importing time and socket modules

print("\nWelcome to Chat Room\n") # printing Welcome message
print("Initialising....\n")
time.sleep(1) # waiting for 1 second 

s = socket.socket() # creating socket client object
shost = socket.gethostname() # getting local machine name
ip = socket.gethostbyname(shost) # getting ip address of local host
print(shost, "(", ip, ")\n") # printing local host and its ip address
host = input(str("Enter server address: ")) # asking the client to enter server address to connect with respective server
name = input(str("\nEnter your name: ")) # taking client name from user input
port = 1234 # reserve a port for service
print("\nTrying to connect to ", host, "(", port, ")\n") # client is saying that trying to connect with server
time.sleep(1) # waiting for 1 second 

s.connect((host, port)) # sending connection request to server
print("Connected...\n") # printing confirmation message on connection

s.send(name.encode()) # sending client name to server
s_name = s.recv(1024) # receiving message from server
s_name = s_name.decode() # decoding received message from server
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n") # printing client has joined the chat room and asking to enter [exit] to exit from chat room

while True:
    message = s.recv(1024) # receiving message from server
    message = message.decode() # decoding received message from server
    print(s_name, ":", message) # printing received message with server name
    message = input(str("Me : ")) # client entering message as user input
    if message == "[exit]":
        message = "Left chat room!"
        s.send(message.encode()) # sending encoded message to server
        print("\n")
        break
    s.send(message.encode()) # sending encoded message to server