import socket

# Create a socket (the 'phone')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to a specific address and port
server.bind(('localhost', 9999))
server.listen(1)

print("Server is waiting for a connection...")

while True:
    # Accept a connection
    client_socket, address = server.accept()
    print(f"Connected to {address}!")

    # Receive the message (up to 1024 bytes)
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Client says: {message}")

    # Send a reply
    client_socket.send("Message received! Hello from the Server.".encode('utf-8'))
    client_socket.close()
