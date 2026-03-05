import socket
import threading

HOST = "127.0.0.1"
PORT = 5001

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print("\nReceived:", message.decode())
        except:
            print("Disconnected from server.")
            break

def send_messages(client_socket):
    while True:
        message = input()
        try:
            client_socket.send(message.encode())
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server.")

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )
    receive_thread.daemon = True
    receive_thread.start()

    send_messages(client)

if __name__ == "__main__":
    start_client()