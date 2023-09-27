# code taken from https://eclass.srv.ualberta.ca/mod/folder/view.php?id=7320333

#!/usr/bin/env python3
import socket
import time
from threading import Thread
 
#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# single threaded version
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            handle_connection(conn, addr)


def handle_connection(conn, addr):
    #recieve data, wait a bit, then send it back
    print("Connected by", addr)
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    print("Recieved: ", full_data)
    conn.sendall(full_data)
    conn.close()
    
# multi threaded version
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:    # init socket
        server_socket.bind((HOST, PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        
        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()
            

# start_server()
start_threaded_server()
