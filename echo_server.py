# code taken from https://eclass.srv.ualberta.ca/mod/folder/view.php?id=7320333

#!/usr/bin/env python3
import socket
import time
from threading import Thread
 
#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
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
            print("Connected by", addr)
            
            handle_connection(conn, addr)
            # #recieve data, wait a bit, then send it back
            # full_data = conn.recv(BUFFER_SIZE)
            # time.sleep(0.5)
            # print("Recieved: ", full_data)
            # conn.sendall(full_data)
            # conn.close()

def handle_connection(conn, addr):
    #recieve data, wait a bit, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    print("Recieved: ", full_data)
    conn.sendall(full_data)
    conn.close()
    
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        
        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()
            
if __name__ == "__main__":
    # main()
    start_threaded_server()
