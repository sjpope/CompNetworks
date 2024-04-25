import socket
import struct
import json

def format_single_student_response(response):
    student = json.loads(response)
    return f"ID: {student['ID']}, First Name: {student['Fname']}, Last Name: {student['Lname']}, Score: {student['score']}"

def format_multiple_students_response(response):
    students = json.loads(response)
    return "\n".join([f"ID: {student['ID']}, First Name: {student['Fname']}, Last Name: {student['Lname']}, Score: {student['score']}" for student in students])

def main(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        
        if response:
            if response.startswith('{'):
                formatted_response = format_single_student_response(response)
            elif response.startswith('['):
                formatted_response = format_multiple_students_response(response)
            else:
                formatted_response = response  
            print("\nServer response:\n", formatted_response)
        else:
            print("No response from server.")
        

    client_socket.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python client_tcp.py localhost 12000")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    main(server_host, server_port)


# python client_tcp-1.py localhost 12000
# eros.cs.txstate.edu 12000
