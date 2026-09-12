from Cipher import Cipher
class Vignere(Cipher):
    count = 0
    def __init__(self, key):
        super().__init__(key)
    def Key_Verification(self):
        if(self.key.isalpha()):
            return True
        else:
            return False
    def Text_Encryption(self,text):
        letters=list(text)
        for i in range(len(letters)):
            if("A"<=letters[i]<="Z"):
                letters[i]=chr(ord("A")+(ord(letters[i])-ord("A")+(ord(self.key[self.count].lower()))-ord("a"))%26)
                self.count = (self.count + 1) % (len(self.key))
            elif("a"<=letters[i]<="z"):
                letters[i]=chr(ord("a")+(ord(letters[i])-ord("a")+(ord(self.key[self.count].lower()))-ord("a"))%26)
                self.count = (self.count + 1) % (len(self.key))
        text="".join(letters)
        return text
    def File_Encryption(self,file_name,dest_file_name=None):
        with open(file_name,"r") as f:
            lines=f.readlines()
            for i in range(len(lines)):
                lines[i]=self.Text_Encryption(lines[i])
        if(dest_file_name != None):
            with open(dest_file_name, "w") as f2:
                f2.writelines(lines)
        else:
            with open(file_name,"w") as f:
                f.writelines(lines)