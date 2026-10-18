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
def remove_non_letter(text):
    new_text = ""
    for i in text:
        if('a'<=i.lower()<='z'):
            new_text += i.lower()
    return new_text
def zero_ic():
    ic={}
    for i in range(ord('a'),ord('z')+1):
        ic[chr(i)]=0
    return ic
def Average_IC(k_len,text):
    c_num=0
    step=0
    ic=zero_ic()
    c_ic=[]
    temp=0
    c_len=0
    while(c_num<k_len):
        while(c_num+(step*k_len)<len(text)):
            ic[text[c_num+(step*k_len)]]+=1
            c_len+=1
            step += 1
        c_num+=1
        step=0
        for i in ic.values():
            temp+=i*(i-1)
        if(c_len>1):
            temp/=(c_len*(c_len-1))
        else:
            temp=0
        c_ic.append(temp)
        temp=0
        ic=zero_ic()
        c_len=0
    temp=0
    for i in c_ic:
        temp+=i
    if(len(c_ic)>0):
        return temp/(len(c_ic))
    return 0

def freq_letter(text,start,k_len):
    letter_freq=zero_ic()
    letter=start
    N=0
    while (letter < len(text)):
        letter_freq[text[letter]] += 1
        letter+=k_len
        N+=1
    return N,letter_freq
def chi_square_value(text,start,k_len):
    N,observed_freq=freq_letter(text,start,k_len)
    expected_freq=zero_ic()
    chi_square=0
    freq = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015,
            'h': 0.06095, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749,
            'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758,
            'v': 0.00978, 'w': 0.0236, 'x': 0.0015, 'y': 0.01974, 'z': 0.00074}
    for i in expected_freq.keys():
        expected_freq[i]+=N*freq[i]
    for i in observed_freq.keys():
        chi_square+=((observed_freq[i]-expected_freq[i])**2)/expected_freq[i]
    return chi_square

def min_chi_square(text,start,k_len):
    all_chi_square=zero_ic()
    for i in range(26):
        ceasar_cipher=Caesar(i)
        new_text=ceasar_cipher.Text(text,True)
        all_chi_square[chr(ord('a')+i)]=chi_square_value(new_text,start,k_len)
    min=None
    min_shift=""
    for i in all_chi_square.keys():
        if(min==None):
            min=all_chi_square[i]
            min_shift=i
        else:
            if(min>all_chi_square[i]):
                min=all_chi_square[i]
                min_shift=i
    return min_shift

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
    else:
        text=""
        path=""
        if(text_file==1):
            text = input(f"Enter The Text to be Decrypted:")
        else:
            path = file_path(f"Enter file path of file to be Decrypted:")
            with open(path, "r") as f:
                text = f.read()
        clean_text = remove_non_letter(text)
        all_ic={}
        max=None
        length_key=0
        for i in range(1,21):
            temp=Average_IC(i,clean_text)
            if temp is not None:
                if(max==None):
                    max=temp
                elif(max<temp):
                    max=temp
                all_ic[i]=temp
        for i in all_ic.keys():
            if(all_ic[i]>=(0.9*max)):
                length_key=i
                break
        key=""
        for i in range(length_key):
            key+=min_chi_square(clean_text,i,length_key)
        Cipher=Vignere(key)
        if(text_file==1):
            final=Cipher.Text(text,decrypt)
            print(final)
        else:
            print(f"1.Do you want to {Name} in same file")
            print(f"2.Do you want to {Name} in different file")
            file_choice = two_choice()
            if file_choice == 1:
                Cipher.File(path,None,decrypt)
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
                Cipher.File(path,dest_path,decrypt)
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

