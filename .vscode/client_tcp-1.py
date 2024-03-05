import socket
import struct

def main(server_host, server_port):
    # Create a socket object with IPv4 addressing and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server
    client_socket.connect((server_host, server_port))
    
    # Prompt the user to enter an integer
    num = int(input("Enter an integer: "))
    
    # Convert the integer to network byte order
    cnum = struct.pack('!I', num)
    
    # Send the integer to the server
    client_socket.send(cnum)
    
    # Receive a reply message from the server
    msg = client_socket.recv(1024).decode()
    print(msg)
    
    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python client_tcp.py <Server IP> <Port>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    main(server_host, server_port)


# python client_tcp-1.py eros.cs.txstate.edu 12000
