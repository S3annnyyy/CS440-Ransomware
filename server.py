import socket
import rsa
import threading

IP_ADDRESS = '192.168.50.113'
IP_ADDRESS_SMU = '192.168.126.1'
PORT = 3000

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

def handle_connection(connection, address):
    print(f"Connection from {address} established")
    with connection:
        while True:
            data_transmitted = connection.recv(1024)
            if not data_transmitted:
                break
            original_msg = rsa.decrypt(data_transmitted, private_key).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(original_msg + '\n')
                f.close()
    print(f"Connection from {address} closed")

def start_server():
    print("Creating socket...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP_ADDRESS, PORT))
        print("Socket created, listening for connections...")
        s.listen(5)
        while True:
            connection, address = s.accept()
            thread = threading.Thread(target=handle_connection, args=(connection, address))
            thread.start()

if __name__ == "__main__":
    start_server()