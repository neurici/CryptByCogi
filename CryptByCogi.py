#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import funcy
import base64
import requests
import Crypto.Protocol
from Crypto import Random
from colorama import init
from Crypto.Cipher import AES
from colorama import Fore, Style

version = "1.0"

init()

banner = r'''
============================================================================
|   _____                      _     ____            _____                  |
|  / ____|                    | |   |  _ \          / ____|             (_) |
| | |      _ __  _   _  _ __  | |_  | |_) | _   _  | |      ___    __ _  _  |
| | |     | '__|| | | || '_ \ | __| |  _ < | | | | | |     / _ \  / _` || | |
| | |____ | |   | |_| || |_) || |_  | |_) || |_| | | |____| (_) || (_| || | |
|  \_____||_|    \__, || .__/  \__| |____/  \__, |  \_____|\___/  \__, ||_| |
|                 __/ || |                   __/ |                 __/ |    |
|                |___/ |_|                  |___/                 |___/     |
|                                                                           |
|                          [Creat de Cogian Sergiu]                         |
|                                                                           |
|                                                                           |
|		   Tastati 'C' pentru a cripta un fisier                    |
|		   Tastati 'D' pentru a decripta un fisier                  |
|		   Tastati 'I' pentru a inchide aplicatia                   |
|                  Tastați 'U' pentru actualizarea aplicatiei               |
=============================================================================
'''
print(Fore.LIGHTBLUE_EX + banner)
print(Style.RESET_ALL)

def actualizare():
    print("Verificare actualizari...")
    CryptByCogi = requests.get("https://raw.githubusercontent.com/neurici/CryptByCogi/main/CryptByCogi.py").content.decode(
        "UTF-8")
    if version not in CryptByCogi:
        co = input("Este disponibilă o nouă versiune a CryptByCogi. Doriți să actualizați? [da/nu] - ").lower()
        if co == "da":
            os.system('cd .. && rm -rf CryptByCogi && git clone https://github.com/neurici/CryptByCogi.git && sleep 3 && cd CryptByCogi')
        if co == "nu":
            print(Fore.LIGHTBLUE_EX + banner)
            choice()
#        else:
#            digg = str(input("Ne pare rau! Optiunea selectata nu este disponibila. Doriti sa renuntati[da/nu] - ").lower())
#            if digg == "da":
#                quit()
#                if digg == "nu":
#                    print(Fore.LIGHTBLUE_EX + banner)
#                    choice()
#                else:
#                    exit()
    else:
        print("CryptByCogi este actualizat.")
        exit()

def quit():
    alpha = input("Sunteti sigur? [da/nu] - ").lower()
    if alpha == "da":
        exit()
    if alpha == "nu":
        print(Fore.LIGHTBLUE_EX + banner)
        choice()

def choice():
    try:
        selection = input("root@CriptServer:~ ").upper()
        if selection == "C":

            usr_key = input("Introduceti o cheie care va fi utilizata ca cheie de criptare:~ ")
            salt = b'\x9aX\x10\xa6^\x1fUVu\xc0\xa2\xc8\xff\xceOV'
            key = Crypto.Protocol.KDF.PBKDF2(password=usr_key, salt=salt, dkLen=32, count=10000)
            iv = Random.new().read(AES.block_size)
            bs = AES.block_size


            def pad(s):
                return s + (bs - len(s) % bs) * chr(bs - len(s) % bs).encode('utf-8')

            def encrypt(raw):
                raw = pad(raw.encode("utf-8"))
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return base64.b64encode(key + iv + cipher.encrypt(raw))


            def encryptFile(fileIn, chunksize=64*1024):
                fileOut = fileIn + ".criptat"
                cipher = AES.new(key, AES.MODE_CBC, iv)
                with open(fileIn, "rb") as plain:
                    with open(fileOut, "wb") as outFile:
                        outFile.write(base64.b64encode(key + iv))

                        while True:
                            chunk = plain.read(chunksize)
                            if len(chunk) == 0:
                                break
                            chunk = pad(chunk)
                            outFile.write(base64.b64encode(cipher.encrypt(chunk)))
                os.remove(fileIn)
            encryptFile(input("Introduceti numele fisierului pe care doriti sa il criptati:~ "))


        if selection == "D":

            def unpad(s):
                return s[:-ord(s[len(s) - 1:])]

            def decrypt(l):
                l = base64.b64decode(l)
                alpha = l[:32]
                key == alpha
                iv = l[32:32 + 16]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return unpad(cipher.decrypt(l[48:]))

            def decryptFile(fileIn, chunksize=24*1024):
                with open(fileIn, "rb") as encryptedFile:
                    encrypted = base64.b64decode(encryptedFile.read(64))
                    setup = encrypted[:48]
                    key_confirm = input("Va rog sa introduceti cheia folosita pentru criptarea fisierului:~ ")
                    salt = b'\x9aX\x10\xa6^\x1fUVu\xc0\xa2\xc8\xff\xceOV'
                    key_check = Crypto.Protocol.KDF.PBKDF2(password=key_confirm, salt=salt, dkLen=32, count=10000)
                    if key_check == setup[:32]:
                        print("Felicitari! Parola este corecta!")
                    else:
                        print("Ghinion! Parola este incorecra")
                        sys.exit(0)

                    iv = setup[32:]
                    cipher = AES.new(key_check, AES.MODE_CBC, iv)
                    with open(fileIn[:-7], "wb") as decryptedFile:
                        encrypted = base64.b64decode(encryptedFile.read())
                        chunks = list(funcy.chunks(chunksize, encrypted))
                        for chunk in chunks:
                            decrypted_chunk = unpad(cipher.decrypt(chunk))
                            decryptedFile.write(decrypted_chunk)

            decryptFile(input("Introduceti numele fisierului pe care doriti sa il decriptati:~ "))

        if selection == 'U':
            actualizare()

        if selection == 'i':
            quit()

    except(KeyboardInterrupt):
        print("\nProgram intrerupt de utilizator")
        exit

choice()







