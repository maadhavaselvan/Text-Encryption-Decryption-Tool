from Cipher import Cipher
class Caesar(Cipher):
    def __init__(self, key):
        super().__init__(key)
    def Text(self,text,decrypt=False):
        letters=list(text)
        for i in range(len(letters)):
            if("A"<=letters[i]<="Z"):
                if(decrypt):
                    letters[i] = chr(ord("A") + (ord(letters[i]) - ord("A") + (26-int(self.key))) % 26)
                else:
                    letters[i]=chr(ord("A")+(ord(letters[i])-ord("A")+int(self.key))%26)
            elif("a"<=letters[i]<="z"):
                if(decrypt):
                    letters[i] = chr(ord("a") + (ord(letters[i]) - ord("a") + (26-int(self.key))) % 26)
                else:
                    letters[i]=chr(ord("a")+(ord(letters[i])-ord("a")+int(self.key))%26)
        text="".join(letters)
        return text
    def File(self,file_name,dest_file_name=None,decrypt=False):
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