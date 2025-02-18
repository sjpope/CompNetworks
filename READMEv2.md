# Student Database Management System

## Description

This project implements a client-server model to manage a simple student database using UDP.

- **UDP version:** Faster, but less reliable communication, for managing student records.

The server maintains a database of student records, including IDs, names, and scores. The client can add, display, or delete student records through a menu-driven interface.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)


## Installation

### Prerequisites

Ensure Python 3.9 or greater is installed on both client and server machines. This can be checked using:

```bash
python --version
```

Note: You may need to run pip install socket, json, sys if you don't have these libraries already installed.

### Server Setup on Environment 1
1. Connect to Environment 1 using SSH:
    ```bash
    ssh username@Env1
    ```
2. Navigate to your project directory or create a new one:
    ```bash
    mkdir ~/CompNetworks
    cd ~/CompNetworks
    ```
3. Use SFTP to transfer the server script `server_udp.py` to this directory.

### Client Setup on Environment 2
1. Connect to Environment 2 using SSH:
    ```bash
    ssh username@Env2
    ```
2. Navigate to your project directory or create a new one:
    ```bash
    mkdir ~/CompNetworks
    cd ~/CompNetworks
    ```
3. Use SFTP to transfer the client script `client_udp.py` to this directory.

## Configuration

No additional configuration is required for the server. The client requires the server's hostname and port number to establish a connection, which are provided as command-line arguments when running the client script.

# Usage

## Local Usage

### To run the server and client locally on your machine:

#### Start the Server:
Open a terminal and run:
```bash
python server_udp.py <port_number>
```
Choose an available port number for <port_number>. I found port number 12000 to work within my local environment.

#### Run the Client:
Open another terminal and run:
```bash
python client_tcp-1.py localhost <port_number>
```
Use the same <port_number> as you used for the server.


That should be all! Thank you for using the Student Database Management System!
