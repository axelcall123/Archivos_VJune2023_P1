import os
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG
class Delete:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

    def path (self,ruta):

        if('"' in ruta):
            self.ruta="/"+ruta.split("\"")[1]+"/"
        else:
            self.ruta=ruta

    def name(self,nombre):
        if('"' in nombre):
            self.nombre="/"+nombre.split("\"")[1]+"/"
        else:
            self.nombre=nombre

    
            
    def borrarCloud(self):
        arrayRuta = gG.arrayRuta(self.ruta)
        servicio = gC.servicioCloud()
        resultado = gC.navegacionCarpetasC(
            servicio, arrayRuta, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')# navego lo maximo posible
        if len(resultado[0])==0:#llegue al final de las carpetas
            if self.nombre=="":#es una carpeta que se elminina
                gC.eliminarCloud(
                    servicio, resultado[1]["id"], 'application/vnd.google-apps.folder')
            else:#es una archivo que se elminina
                res=gC.existeNombreC(servicio, resultado[1]["id"],self.nombre)
                if res["existe"]=="true":#existe archivo que elminar
                    gC.eliminarCloud(servicio, res["id"], 'text/plain')
                else:
                    print("Indico mal el nombre del archivo vuelva a intentarlo")

        else:#url mala
            print(f"La ruta especificada {self.ruta}, esta mal")
        print("termino de elminar todo")



        
            

        
        
    

