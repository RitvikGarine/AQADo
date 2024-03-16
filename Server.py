import socket
import threading
import os

client1 = []
client2 = []

counter = 0

def handle_client(client_socket):
    global client1, client2, counter
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        response = message
        if counter % 2 == 1:
            client1.sendall(response.encode('utf-8'))
        else:
            client2.sendall(response.encode('utf-8'))
        counter += 1
    client1.close()
    client2.close()

def main():
    global client1, client2
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12347
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {get_ip()}: {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        if client1 == []:
            client1 = client_socket
            client1.sendall('P1'.encode('utf-8'))
        else:
            client2 = client_socket
            client2.sendall('P2'.encode('utf-8'))
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

if __name__ == "__main__":
    IPAddr = get_ip()
    print("The server IP Address is: " + str(IPAddr))
    print('Please enter this in the playing window when prompted \n')
    main()
