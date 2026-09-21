from Caesar import Caesar
from Vignere import Vignere
import os
import random
def two_choice():
    choice=-1
    while (True):
        try:
            choice=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (choice!=1 and choice!=2):
            print("Enter Either 1 or 2")
            continue
        break
    return choice
def choice(name,decrypt=False):
    print(f"1.{name} Text")
    print(f"2.{name} File")
    inputs=two_choice()
    key_cipher=0
    if(decrypt==True):
        print("Do you know the Key and which cipher:")
        print("1.Yes")
        print("2.No")
        key_cipher=two_choice()
    if(key_cipher==2):
        return inputs,0,0,key_cipher

    print("1.Caesar")
    print("2.Vignere")
    cipher=two_choice()
    if(key_cipher==1):
        return inputs,cipher,2,key_cipher
    print("1.With Randomised Key")
    print("2.With Known Key")
    key_type=two_choice()
    return inputs,cipher,key_type,key_cipher
def file_path(text):
    while True:
        path=input(text)
        new_path=corrected_path(path)
        if (os.path.isfile(new_path)):
            break
        print("File doesn't exist Please Try Again")
    return new_path
def corrected_path(p):
    return os.path.expanduser(p.strip().strip("'\""))
def Caesar_Key():
    while True:
        key=input("Enter Key:")
        encrypt=Caesar(key)
        if (encrypt.Key_Verification()):
            if (0 < int(encrypt.key) < 26):
                break
            else:
                print("Please enter value from 1 to 25")
        else:
            print("Enter only numbers")
    return Caesar(key)
def Vignere_key():
    while True:
        key=input("Enter Key:")
        encrypt=Vignere(key)
        if (encrypt.Key_Verification()):
            break
        else:
            print("Enter only alphabets in Key")
    return Vignere(key)

def Key(cipher,key_type):
    if (cipher == 1):
        if (key_type == 1):
            encrypt = Caesar(random.randint(1, 25))
            print("Value of Key: ", encrypt.key)
        else:
            encrypt = Caesar_Key()
    else:
        if (key_type == 1):
            key = ""
            for i in range(random.randint(10, 20)):
                j = random.randint(1, 2)
                if (j == 1):
                    key += chr(random.randint(67, 90))
                else:
                    key += chr(random.randint(97, 122))
            encrypt = Vignere(key)
            print("Value of Key: ", encrypt.key)
        else:
            encrypt = Vignere_key()
    return encrypt

def encrypt_decrypt(Name,decrypt=False):
    inputs, cipher, key_type, key_cipher = choice(Name,decrypt)
    Cipher_crypt = Key(cipher, key_type)
    if (inputs == 1):
        text = input(f"Enter The Text to be {Name}ed:")
        if(key_cipher == 2):
            crypt_text = Cipher_crypt.decrypt()
        else:
            crypt_text = Cipher_crypt.Text(text,decrypt)
            print(crypt_text)
    else:
        path = file_path(f"Enter file path of file to be {Name}ed:")
        print(f"1.Do you want to {Name} in same file")
        print(f"2.Do you want to {Name} in different file")
        file_choice = two_choice()
        if file_choice == 1:
            Cipher_crypt.File(path)
        else:
            while (True):
                dest_path = input(("Enter file path of destination file:"))
                dest_path = corrected_path(dest_path)
                try:
                    with open(dest_path, "w") as f:
                        pass
                except:
                    print("Enter correct file path")
                    continue
                break
            if(key_cipher == 2):
                crypt_text = Cipher_crypt.file_decrypt()
            else:
                Cipher_crypt.File(path, dest_path)
        print(f"Text is {Name}ed")
while True:
    print("="*300)
    print(" "*120,"CIPHER TOOL - Caesar and Vignere")
    print("1.Encrypt")
    print("2.Decrpyt")
    print("3.Exit")
    print("="*300)
    try:
        Crypt=int(input("Enter Your Choice:"))
    except ValueError:
        print("Please enter a number")
        continue
    if Crypt==1:
        encrypt_decrypt("Encrypt")
    elif Crypt==2:
        encrypt_decrypt("Decrypt",True)
    elif Crypt==3:
        break
    else:
        print("Enter Either 1 or 2 or 3")
        continue

