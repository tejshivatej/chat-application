"""

Description: This file is to implement server side socket program for chat application
in which server and client will communicate with each other
Author: Shivateja Kokkula
Position: Junior Software Engineer 

"""



import time, socket   # importing time and socket modules

print("\nWelcome to Chat Room\n") # printing Welcome message
print("Initialising....\n") 
time.sleep(1) # waiting for 1 second 

s = socket.socket() # creating socket server object
host = socket.gethostname() # getting local machine name
ip = socket.gethostbyname(host) # getting ip address of local host
port = 1234 # reserve a port for your service
s.bind((host, port)) # binding the host with port
print(host, "(", ip, ")\n") # printing local host and its ip address
name = input(str("Enter your name: ")) # Taking name from user input
           
s.listen(1) # Now waiting for client connections
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept() # server accepting client connection and storing client object, client address into variables
print("Received connection from ", addr[0], "(", addr[1], ")\n") # printing where the connection is received from

s_name = conn.recv(1024) # receiving message sent by client
s_name = s_name.decode() # decoding the received message
print(s_name, "has connected to the chat room\nEnter [exit] to exit chat room\n") # printing message that client entered into chat room and telling enter [exit] to exit chat room
conn.send(name.encode()) # sending message to client 

while True:
    message = input(str("Me : ")) # taking server input
    if message == "[exit]": # checking whether messege entered is [exit] or not 
        message = "Left chat room!"
        conn.send(message.encode()) # sending server message to client
        print("\n") # goes to new line
        break
    conn.send(message.encode()) # sending message to client
    message = conn.recv(1024) # receiving message from client
    message = message.decode() # decoding received message
    print(s_name, ":", message) # printing received message with client name