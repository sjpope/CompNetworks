# Student Database Management System

## Description

This project implements a client-server model to manage a simple student database using TCP. The server maintains a database of student records, including IDs, names, and scores, and allows the client to add, display, or delete student records through a menu-driven interface.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Server Setup on Eros
1. Connect to Eros using SSH:
    ```bash
    ssh username@eros.cs.txstate.edu
    ```
2. Navigate to your project directory or create a new one:
    ```bash
    mkdir ~/CompNetworks
    cd ~/CompNetworks
    ```
3. Use SFTP to transfer the server script `server_tcp-1.py` to this directory.

### Client Setup on Zeus
1. Connect to Zeus using SSH:
    ```bash
    ssh username@zeus.cs.txstate.edu
    ```
2. Navigate to your project directory or create a new one:
    ```bash
    mkdir ~/CompNetworks
    cd ~/CompNetworks
    ```
3. Use SFTP to transfer the client script `client_tcp-1.py` to this directory.

## Configuration

No additional configuration is required for the server. The client requires the server's hostname and port number to establish a connection, which are provided as command-line arguments when running the client script.

## Usage

### Local Usage

# To run the server and client locally on your machine:

# Start the Server:
Open a terminal and run:

python server_tcp-1.py <port_number>
Choose an available port number for <port_number>.

# Run the Client:
Open another terminal and run:

python client_tcp-1.py localhost <port_number>
Use the same <port_number> as you used for the server.