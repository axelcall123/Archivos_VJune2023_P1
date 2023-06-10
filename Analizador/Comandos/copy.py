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
        #print(pathArchivofrom)
        #print(pathArchivoto)
        


        if(os.path.exists(pathArchivofrom)&('.' in pathArchivofrom)):
            #copiar archivo
            shutil.copy(pathArchivofrom,pathArchivoto)
            print("******EL ARCHIVO FUE COPIADO CON EXITO******")
        else:
            if(os.path.exists(pathArchivofrom)):
                #existe la ruta
                shutil.copytree(pathArchivofrom,pathArchivoto)
                print("******LA CARPETA FUE COPIADA CON EXITO******")
            else:
                #si no existe nada
                 print("******ERROR NO SE ENCONTRO LA DIRECCION******")
       
            





        
            

        
        
    

