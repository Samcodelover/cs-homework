import socket

# Create the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's address and port
client.connect(('localhost', 9999))

# Send a message
client.send("Hi Server, I'm the Client!".encode('utf-8'))

# Get the response
response = client.recv(1024).decode('utf-8')
print(f"Server replied: {response}")

client.close()