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
        

        print(os.path.exists(pathArchivofrom)&('.' in self.de))
        if(os.path.exists(pathArchivofrom)&('.' in self.de)):
            #copiar archivo
            shutil.copy(pathArchivofrom,pathArchivoto)
            print("******EL ARCHIVO FUE COPIADO CON EXITO******")
        else:
            if(os.path.exists(pathArchivofrom)):
                #existe la ruta
                print("--------------")
                #!--------------------------------------------
                shutil.copytree(pathArchivofrom,pathArchivoto)
                print("******LA CARPETA FUE COPIADA CON EXITO******")
            else:
                #si no existe nada
                if(not os.path.exists(pathArchivoto)): print("YA EXISTE ESA DIRECCION")
                print("******ERROR NO SE ENCONTRO LA DIRECCION******")
                 
       
            





        
            

        
        
    

