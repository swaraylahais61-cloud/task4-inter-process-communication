
import socket
import time

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is running on {HOST}:{PORT}")
print("Waiting for clients...")

try:
    while True:
        conn, address = server_socket.accept()
        print(f"\nConnected by {address}")

        with conn:
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()
                print(f"Client message: {message}")

                if message.lower() == "exit":
                    conn.sendall(b"Connection closed. Goodbye!")
                    break

                time.sleep(0.2)
                conn.sendall(b"Message received")

        print("Client disconnected.")
        print("Waiting for the next client...")

except KeyboardInterrupt:
    print("\nServer stopped.")

finally:
    server_socket.close()
