import socket
import json
import sys

def format_single_student_response(response):
    student = json.loads(response)
    return f"ID: {student['ID']}, First Name: {student['Fname']}, Last Name: {student['Lname']}, Score: {student['score']}"

def format_multiple_students_response(response):
    students = json.loads(response)
    return "\n".join([f"ID: {student['ID']}, First Name: {student['Fname']}, Last Name: {student['Lname']}, Score: {student['score']}" for student in students])

def main(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        print(f"\n\nMENU\n")
        print("1. Add Student")
        print("2. Display Student by ID")
        print("3. Display Students by Score")
        print("4. Display All Students")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (int): ")

        if choice == '6':
            print("\nExiting...")
            break

        server_address = (server_host, server_port)
        
        if choice == '1':
            student_data = {
                "ID": input("Enter ID: "),
                "Fname": input("Enter First Name: "),
                "Lname": input("Enter Last Name: "),
                "score": input("Enter Score: ")
            }
            message = json.dumps({"command": "ADD", "data": student_data})
            client_socket.sendto(message.encode(), server_address)

        elif choice == '2':
            id = input("Enter Student ID to display: ")
            message = json.dumps({"command": "DISPLAY", "data": id})
            client_socket.sendto(message.encode(), server_address)

        elif choice == '3':
            score = input("Enter minimum score to display students: ")
            message = json.dumps({"command": "DISPLAY_SCORE", "data": score})
            client_socket.sendto(message.encode(), server_address)

        elif choice == '4':
            message = json.dumps({"command": "DISPLAY_ALL"})
            client_socket.sendto(message.encode(), server_address)

        elif choice == '5':
            id = input("Enter Student ID to delete: ")
            message = json.dumps({"command": "DELETE", "data": id})
            client_socket.sendto(message.encode(), server_address)

        data, _ = client_socket.recvfrom(1024)
        response = data.decode()
        
        if response:
            if response.startswith('{') or response.startswith('['):
                if response.startswith('{'):
                    formatted_response = format_single_student_response(response)
                else:
                    formatted_response = format_multiple_students_response(response)
            print("\nServer response:\n", formatted_response)
        else:
            print("No response from server.")

    client_socket.close()

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print("Usage: python client_udp.py <Server IP> <Port>")
        sys.exit(1)
        
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

    main(server_host, server_port)




# python client_udp.py localhost 12000
# eros.cs.txstate.edu 12000