from Caesar import Caesar
import os
import random

def choice(name):
    while True:
        print(f"1.{name} Text")
        print(f"2.{name} File")
        try:
            y=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (y!=1 and y!=2):
            print("Enter Either 1 or 2")
            continue
        break
    while (True):
        print("1.Caesar")
        print("2.Vignere")
        try:
            z=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (z!=1 and z!=2):
            print("Enter Either 1 or 2")
            continue
        break
    while (True):
        print("1.With Randomised Key")
        print("2.With Known Key")
        try:
            r=int(input("Enter Your Choice:"))
        except ValueError:
            print("Please enter a number")
            continue
        if (r!=1 and r!=2):
            print("Enter Either 1 or 2")
            continue
        break
    return y,z,r


def corrected_path(p):
    return os.path.expanduser(p.strip().strip("'\""))

def Caesar_Encrypt():
    while (True):
        try:
            int_shift=int(input("Enter The Integer Shift:"))
            return Caesar(int_shift)
        except ValueError:
            print("Please Enter a Number")
            continue
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
        if (y==1):
            if (z==1):
                text=input("Enter The Text to be encrypted:")
                if(r==1):
                    encrypt=Caesar(random.randint(1,25))
                else:
                    encrypt=Caesar_Encrypt()
                encrypt_text=encrypt.Text_Encryption(text)
                print(encrypt_text)
            else:
                pass
                # call Encrypt file caesar file
        else:
            if (z==1):
                while True:
                    path=input("Enter file path:")
                    if(os.path.isfile(corrected_path(path))):
                        break
                    print("File doesn't exist Please Try Again")
                if(r==1):
                    encrypt=Caesar(random.randint(1,25))
                else:
                    encrypt=Caesar_Encrypt()
                encrypt_text=encrypt.File_Encryption(path)
                print("Text is Encrypted")
            else:
                pass
                # call Encrypt file vignere file
    elif x==2:
        y,z=choice("Decrypt")
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

