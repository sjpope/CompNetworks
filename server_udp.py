import socket
import json
import sys


# Student Management Functions

def add_student(database, student_data):
    database.append(student_data)
    return "Student added successfully."

def display_student_by_id(database, student_id):
    student = next((s for s in database if s['ID'] == student_id), None)
    return json.dumps(student) if student else "Student not found."

def display_students_by_score(database, score):
    return json.dumps([s for s in database if int(s['score']) > score])

def display_all_students(database):
    return json.dumps(database)

def delete_student(database, student_id):
    database[:] = [s for s in database if s['ID'] != student_id]
    return "Student deleted successfully."


# Database Functions

def read_database(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_database(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def process_request(data, database):
    
    request = json.loads(data)
    
    print(f"Received request: {request}")
    
    command = request.get("command")
    args = request.get("data")  # Check if "data" key exists in the request dictionary
    
    if command == "ADD":
        return add_student(database, args)
    elif command == "DISPLAY":
        return display_student_by_id(database, args)
    elif command == "DISPLAY_SCORE":
        return display_students_by_score(database, int(args))
    elif command == "DISPLAY_ALL":
        return display_all_students(database)
    elif command == "DELETE":
        return delete_student(database, args)
    else:
        return "Invalid command."



def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set SO_REUSEADDR option
    server_socket.bind(('', port))
    print(f"Listening on port {port}")
    
    database = read_database('db.json')

    while True:
        
        data, client_address = server_socket.recvfrom(1024)
        
        print(f"Received data: {data.decode()} from {client_address}")
        
        response = process_request(data.decode(), database)
        
        server_socket.sendto(response.encode(), client_address)
        
        write_database('db.json', database)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python server_udp.py <Port>")
        sys.exit(1)

    port = int(sys.argv[1])
    main(port)
    

# python server_udp.py 12000
# put on eros.cs.txstate.edu