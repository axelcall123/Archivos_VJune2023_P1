import os
import shutil

class Copy:
    def __init__ (self,):
        self.de=""
        self.a=""

    def desde (self,de):
        if('"' in de):
            self.de=de.split("\"")[1]
        else:
            self.de=de

    def to(self,a):
        if('"' in a):
            self.a=a.split("\"")[1]
        else:
            self.a=a

    def copiar(self):
        pathArchivofrom= "../Archivo"+self.de
        pathArchivoto="../Archivo"+self.a
        print(pathArchivofrom)
        print(pathArchivoto)
        shutil.copy(pathArchivofrom,pathArchivoto)
       
            





        
            

        
        
    

