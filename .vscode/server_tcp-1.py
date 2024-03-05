import socket
import struct

def main(port):
    # Create a socket object with IPv4 addressing and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to all IP addresses of this host and the specified port
    server_socket.bind(('', port))
    
    # Listen for incoming connections, with a backlog of 5 connections
    server_socket.listen(5)
    print("Listening on port", port)
    
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print("Connected to", client_address)
        
        # Receive data from the client
        data = client_socket.recv(1024)
        
        # Unpack the received data from network byte order to integer
        num = struct.unpack('!I', data)[0]
        print("Integer received:", num)
        
        # Send a reply message to the client
        msg = "Integer received"
        client_socket.send(msg.encode())
        
        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python server_tcp.py <Port>")
        sys.exit(1)

    port = int(sys.argv[1])
    main(port)

# python server_tcp-1.py 12000
# put on eros.cs.txstate.edu
