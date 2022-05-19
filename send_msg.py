#Imports nessisary items
#to accses ports use as class function
import socket
#Imports the ability to thread as Thread(args)
from threading import Thread

#######################################

#the server IP adress for dirscting trafic
SERVER_HOST = '0.0.0.0'
SERVER_PORT = '' #string fo 4 diget # that tell you were to go
separator_token = '<sep>' #signifies seperation between client + server

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

