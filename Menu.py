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

def choice_encrypt():
    print(f"1.Encrypt Text")
    print(f"2.Encrypt File")
    text_file=two_choice()
    print("1.Caesar")
    print("2.Vignere")
    cipher=two_choice()
    print("1.With Randomised Key")
    print("2.With Known Key")
    rand_known=two_choice()
    return text_file,cipher,rand_known

def choice_decrypt():
    print("1.Decrypt Text")
    print("2.Decrypt File")
    text_file=two_choice()
    print("Do you know the Key and which cipher:")
    print("1.Yes")
    print("2.No")
    key_cipher=two_choice()
    if(key_cipher==2):
        return text_file,0,0
    print("1.Caesar")
    print("2.Vignere")
    cipher=two_choice()
    return text_file,cipher,2

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

def Key(cipher,rand_known):
    if (cipher == 1):
        if (rand_known == 1):
            encrypt = Caesar(random.randint(1, 25))
            print("Value of Key: ", encrypt.key)
        else:
            encrypt = Caesar_Key()
    else:
        if (rand_known == 1):
            key = ""
            for i in range(random.randint(10, 20)):
                j = random.randint(1, 2)
                if (j == 1):
                    key += chr(random.randint(65, 90))
                else:
                    key += chr(random.randint(97, 122))
            encrypt = Vignere(key)
            print("Value of Key: ", encrypt.key)
        else:
            encrypt = Vignere_key()
    return encrypt

def encrypt_decrypt(Name,decrypt=False):
    if(decrypt==False):
        text_file, cipher, rand_known= choice_encrypt()
    else:
        text_file, cipher, rand_known= choice_decrypt()
    if(rand_known==1 or rand_known==2):
        Cipher_crypt = Key(cipher, rand_known)
        if (text_file == 1):
            text = input(f"Enter The Text to be {Name}ed:")
            crypt_text = Cipher_crypt.Text(text,decrypt)
            print(crypt_text)
        else:
            path = file_path(f"Enter file path of file to be {Name}ed:")
            print(f"1.Do you want to {Name} in same file")
            print(f"2.Do you want to {Name} in different file")
            file_choice = two_choice()
            if file_choice == 1:
                Cipher_crypt.File(path,None,decrypt)
            else:
                while (True):
                    dest_path = input("Enter file path of destination file:")
                    dest_path = corrected_path(dest_path)
                    try:
                        with open(dest_path, "w") as f:
                            break
                    except:
                        print("Enter correct file path")
                        continue
                Cipher_crypt.File(path,dest_path,decrypt)
            print(f"Text is {Name}ed")

while True:
    print("="*300)
    print(" "*120,"CIPHER TOOL - Caesar and Vignere")
    print("1.Encrypt")
    print("2.Decrypt")
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

