import socket
import threading

HOST = "127.0.0.1"
PORT = 5001

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break

            print(f"[{address}] {message.decode()}")
            broadcast(message, client_socket)

        except:
            break

    print(f"[DISCONNECTED] {address}")
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[LISTENING] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )
        thread.start()

if __name__ == "__main__":
    start_server()