class Cipher:
    def __init__(self, key):
        self.key=key
    def Key_Verification(self):
        if(self.key.isdigit()):
            return True
        else:
            return False

