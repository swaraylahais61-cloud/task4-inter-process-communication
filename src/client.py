
import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")
    print("Type a message or type 'exit' to quit.")

    while True:
        message = input("Enter message: ")
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print("Server response:", response.decode())

        if message.lower() == "exit":
            break

except ConnectionRefusedError:
    print("Could not connect. Make sure the server is running.")

except OSError as error:
    print("Connection error:", error)

finally:
    client_socket.close()
    print("Client connection closed.")
