from Caesar import Caesar
from Vignere import Vignere
import os
import random
def two_choice():
    while (True):
        try:
            z=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (z!=1 and z!=2):
            print("Enter Either 1 or 2")
            continue
        break
    return z
def choice(name):
    print(f"1.{name} Text")
    print(f"2.{name} File")
    y=two_choice()
    print("1.Caesar")
    print("2.Vignere")
    z=two_choice()
    print("1.With Randomised Key")
    print("2.With Known Key")
    r=two_choice()
    return y,z,r
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

def Key(z,r):
    if (z == 1):
        if (r == 1):
            encrypt = Caesar(random.randint(1, 25))
            print("Value of Key: ", encrypt.key)
        else:
            encrypt = Caesar_Key()
    else:
        if (r == 1):
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
while True:
    print("="*300)
    print(" "*120,"CIPHER TOOL - Caesar and Vignere")
    print("1.Encrypt")
    print("2.Decrpyt")
    print("3.Exit")
    print("="*300)
    try:
        x=int(input("Enter Your Choice:"))
    except ValueError:
        print("Please enter a number")
        continue
    if x==1:
        y,z,r=choice("Encrypt")
        encrypt = Key(z, r)
        if (y==1):
            text=input("Enter The Text to be encrypted:")
            encrypt_text = encrypt.Text_Encryption(text)
            print(encrypt_text)
        else:
            path = file_path("Enter file path of file to be encrypted:")
            print("1.Do you want to Encrypt in same file")
            print("2.Do you want to Encrypt in different file")
            file_choice=two_choice()
            if file_choice==1:
                encrypt.File_Encryption(path)
            else:
                while(True):
                    dest_path=input(("Enter file path of destination file:"))
                    dest_path=corrected_path(dest_path)
                    try:
                        with open(dest_path, "w") as f:
                            pass
                    except:
                        print("Enter correct file path")
                        continue
                    break
                encrypt.File_Encryption(path,dest_path)
            print("Text is Encrypted")
    elif x==2:
        y,z,r=choice("Decrypt")
        if (y==1):
            if (z==1):
                pass
                # call Decrypt text caesar file
            else:
                pass
                # call Decrypt file caesar file
        else:
            if (z==1):
                pass
                # call Decrypt text vignere file
            else:
                pass
                # call Decrypt file vignere file
    elif x==3:
        break
    else:
        print("Enter Either 1 or 2 or 3")
        continue

