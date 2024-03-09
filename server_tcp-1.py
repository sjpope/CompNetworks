import socket
import struct
import json

# Choice 1
def add_student(database, student_data):
    database.append(student_data)

# Choice 2
def display_student_by_id(database, student_id):
    print(f"Filtering for student with ID: {student_id}, Type: {type(student_id)}")
    return next((student for student in database if student['ID'] == student_id), None)

# Choice 3
def display_students_by_score(database, score):
    print(f"Filtering for scores greater than {score}")
    for student in database:
        print(f"Student Score: {student['score']}, Type: {type(student['score'])}")
    return [student for student in database if int(student['score']) > score]

# Choice 4
def display_all_students(database):
    return database

# Choice 5
def delete_student(database, student_id):
    database[:] = [student for student in database if student['ID'] != student_id]


def read_database(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_database(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object with IPv4 addressing and TCP protocol
    server_socket.bind(('', port)) # Bind the socket to all IP addresses of this host and the specified port
    server_socket.listen(5) # Listen for incoming connections, with a backlog of 5 connections
    print("Listening on port", port)
    
    database = read_database('db.json')
    client_socket, client_address = server_socket.accept()  
    print("Connected to", client_address)
    
    while True:
        
        data = client_socket.recv(1024).decode() # Receive data from the client
        if not data:
            print("No data received. Closing connection.")
            break
        
        print(f"Received data: {data}")
        command, *args = data.split(',')
        
        if command == "ADD":
            # Expected args: [ID, Fname, Lname, score]
            student_data = {"ID": args[0], "Fname": args[1], "Lname": args[2], "score": int(args[3])}
            add_student(database, student_data)
            
            response = "Student added successfully."
            print(f"\n", response)            
            client_socket.send(response.encode())
        
        elif command == "DISPLAY":
            print(f"Displaying student with ID: {args[0]}")
            student = display_student_by_id(database, args[0])  # Expected args: [ID]
            
            response = json.dumps(student) if student else "Student not found."
            print(f"\n", response)
            client_socket.send(response.encode())
        
        elif command == "DISPLAY_SCORE":
            print(f"Displaying students with score greater than: {args[0]}")
            students = display_students_by_score(database, int(args[0]))  # Expected args: [score]
            response = json.dumps(students)
            print(f"\n", response)
            client_socket.send(response.encode())
        
        elif command == "DISPLAY_ALL":
            response = json.dumps(display_all_students(database))
            print(f"\n", response)            
            client_socket.send(response.encode())
        
        elif command == "DELETE":
            delete_student(database, args[0])  # Expected args: [ID]
            response = "Student deleted successfully."
            print(f"\n", response)            
            client_socket.send(response.encode())
        
        else:
            response = "Invalid command."
            print(f"\n", response)            
            client_socket.send(response.encode())
        
        # client_socket.send(response.encode())
        
        write_database('db.json', database) # After handling the request, update the JSON file
    
    
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
