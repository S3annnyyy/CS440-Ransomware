import rsa
import os
import sys

# Generating private and public key
# pubKey, priKey = rsa.newkeys(1024)

# with open("public.pem", "wb") as f:
#     f.write(pubKey.save_pkcs1("PEM"))

# with open("private.pem", "wb") as f:
#     f.write(priKey.save_pkcs1("PEM"))


# Testing encryption
def resource_path(relative_path):
    """ This function gets the absolute path to resource"""
    try:        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        print(base_path, relative_path)
    return os.path.join(base_path, relative_path)

pubkeypath = resource_path("./public.pem")
prikeypath = resource_path("./private.pem")

with open(pubkeypath, "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open(prikeypath, "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message ="MAC_ADDRESS: 00-0C-29-9D-44-E7\nENCRYPTION_KEY: b'RS_G8DNEmCd1CaBXbnJbsyzW_G7C9jv--FU-XkOv_KI='"

encrypted_msg = rsa.encrypt(message.encode("utf-8"), public_key)

print(encrypted_msg)
print("###########################################")
original_msg = rsa.decrypt(encrypted_msg, private_key).decode()
print(original_msg)

