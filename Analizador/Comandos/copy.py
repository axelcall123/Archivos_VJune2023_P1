import os
import shutil
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG

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
       
    def copiarCloud(self):
        #print(self.de,self.a)
        arrayRuta = gG.arrayRuta(self.a)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible
        
        if len(resultado[0]) != 0:  # llegue al final de las carpetas/de
            print(f"La ruta especificada {self.a}, esta mal")
            return 0
        idA=resultado[1]["id"]#id self.a

        arrayRuta = gG.arrayRuta(self.de)
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')
        
        
        if len(resultado[0]) != 0:  # llegue al final de las carpetas/de
            print(f"La ruta especificada {self.de}, esta mal")
            return 0
        idDe = resultado[1]["id"]  # ida self.de

        gC.listadoCloud(servicio,idA)
        
        return
