import os
import shutil
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
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
            self.a="/"+a.split("\"")[1]+"/"
        else:
            self.a=a

    def copiar(self):
        pathArchivofrom= "./archivos"+self.de
        pathArchivoto="./archivos"+self.a
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
                 print("******ERROR NO SE ENCONTRO LA DIRECCION******")
       
            






        
            

        
        
    

