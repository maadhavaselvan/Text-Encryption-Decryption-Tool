from Cipher import Cipher
class Vignere(Cipher):
    def __init__(self, key):
        super().__init__(key)
        self.count=0
    def Key_Verification(self):
        if(self.key.isalpha()):
            return True
        else:
            return False
    def Text(self,text,decrypt=False):
        self.count=0
        letters=list(text)
        for i in range(len(letters)):
            if("A"<=letters[i]<="Z"):
                if(decrypt==False):
                    letters[i]=chr(ord("A")+(ord(letters[i])-ord("A")+(ord(self.key[self.count].lower()))-ord("a"))%26)
                else:
                    letters[i]=chr(ord("A")+(ord(letters[i])-ord("A")+26-(ord(self.key[self.count].lower())-ord("a")))%26)
                self.count = (self.count + 1) % (len(self.key))
            elif("a"<=letters[i]<="z"):
                if(decrypt==False):
                    letters[i]=chr(ord("a")+(ord(letters[i])-ord("a")+(ord(self.key[self.count].lower()))-ord("a"))%26)
                else:
                    letters[i]=chr(ord("a")+(ord(letters[i])-ord("a")+26-(ord(self.key[self.count].lower())-ord("a")))%26)
                self.count = (self.count + 1) % (len(self.key))
        text="".join(letters)
        return text
    def File(self,file_name,dest_file_name=None,decrypt=False):
        self.count=0
        with open(file_name,"r") as f:
            lines=f.readlines()
            for i in range(len(lines)):
                lines[i]=self.Text(lines[i],decrypt)
        if(dest_file_name != None):
            with open(dest_file_name, "w") as f2:
                f2.writelines(lines)
        else:
            with open(file_name,"w") as f:
                f.writelines(lines)