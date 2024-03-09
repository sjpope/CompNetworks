import socket
import struct

def main(server_host, server_port):
    # Create a socket object with IPv4 addressing and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server
    client_socket.connect((server_host, server_port))
    
    
    
    
    
    while True:
        print(f"\nMENU\n")
        print("1. Add Student")
        print("2. Display Student by ID")
        print("3. Display Students by Score")
        print("4. Display All Students")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (int): ")

        if choice == '6':
            break

        if choice == '1':
            # Gather student details
            id = input("Enter ID: ")
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            score = input("Enter Score: ")
            student_data = f"ADD,{id},{fname},{lname},{score}"
            client_socket.send(student_data.encode())

        elif choice == '2':
            id = input("Enter Student ID to display: ")
            client_socket.send(f"DISPLAY,{id}".encode())

        elif choice == '3':
            score = input("Enter minimum score to display students: ")
            client_socket.send(f"DISPLAY_SCORE,{score}".encode())

        elif choice == '4':
            client_socket.send("DISPLAY_ALL".encode())

        elif choice == '5':
            id = input("Enter Student ID to delete: ")
            client_socket.send(f"DELETE,{id}".encode())

        response = client_socket.recv(1024).decode()
        if response is None:
            print("No response from server.")
            continue
        
        print(f"\n\nServer response:", response)

    client_socket.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python client_tcp.py <Server IP> <Port>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    main(server_host, server_port)


# python client_tcp-1.py 12000
# eros.cs.txstate.edu 12000
