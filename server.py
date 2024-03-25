import socket

IP_ADDRESS = '192.168.50.113'
PORT = 3000
print("Creating socket...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print("Socket created, listening for connections...")
    s.listen(1)
    connection, address = s.accept()
    print(f"Connection from {address} established")

    with connection:
        while True:
            data_transmitted = connection.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(data_transmitted + '\n')
            break
        print("Connection closed")