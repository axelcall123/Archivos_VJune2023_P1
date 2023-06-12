import os
import shutil
import Analizador.Comandos._generalCloud as gC  # alias
class Transfer:
    def __init__ (self,):
        self.de=""
        self.a=""
        self.modo=""

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

    def mode(self,mode):
        if('"' in mode):
            self.modo=mode.split("\"")[1]
        else:
            self.modo=mode

    def transferCloud(self):
        retorno = gC.auxDeParaC(self.a, self.de)
        if retorno[0] == " ":
            return
        servicio = gC.servicioCloud()
        idA = retorno[0]
        idDe = retorno[1]
        gC.tranferCloud(servicio,idA,idDe)
        print(f"se tranfirieron todos los archivos")

        
       
            
