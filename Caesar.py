from Cipher import Cipher
class Caesar(Cipher):
    def __init__(self, key):
        super().__init__(key)
    def Text_Encryption(self,text):
        letters=list(text)
        for i in range(len(letters)):
            if("A"<=letters[i]<="Z"):
                letters[i]=chr(ord("A")+(ord(letters[i])-ord("A")+self.key)%26)
            elif("a"<=letters[i]<="z"):
                letters[i]=chr(ord("a")+(ord(letters[i])-ord("a")+self.key)%26)
        text="".join(letters)
        return text
