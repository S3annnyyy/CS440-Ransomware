import socket
import rsa

IP_ADDRESS = '192.168.50.113'
IP_ADDRESS_SMU = '192.168.126.1'
PORT = 3000

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
print("Creating socket...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print("Socket created, listening for connections...")
    s.listen(1)
    connection, address = s.accept()
    print(f"Connection from {address} established")

    with connection:
        while True:
            data_transmitted = connection.recv(1024)
            original_msg = rsa.decrypt(data_transmitted, private_key).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(original_msg + '\n')
            break
        print("Connection closed")