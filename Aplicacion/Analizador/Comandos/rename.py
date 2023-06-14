import os
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
class Rename:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

    def path (self,ruta):
        
        if('"' in ruta):
            self.ruta=ruta.split("\"")[1]
        else:
            self.ruta=ruta
            

    def name(self,nombre):
        if('"' in nombre):
            self.nombre=nombre.split("\"")[1]
        else:
            self.nombre=nombre

    def reNombrar(self):
        pathArchivo= "./archivos"+self.ruta
        print(pathArchivo)
        #obtener ruta para el nuevo nombre
        obtNomber=self.ruta.split("/")
        contador=0
        nuevaRuta=""
        for element in obtNomber:
            if(contador<len(obtNomber)-1):
                if(element!=""):
                    nuevaRuta=nuevaRuta+"/"+element
            contador=contador+1


        pathNuevoNombre="./archivos"+nuevaRuta+"/"+self.nombre
        
        if(os.path.exists(pathArchivo)& (not(os.path.exists(pathNuevoNombre)))):
            os.rename(pathArchivo,pathNuevoNombre)
            print("******EL ARCHIVO FUE RENOMBRADO CON EXITO******")
            
        else:
             print("******ERROR NO SE ENCONTRO LA DIRECCION O YA SE ENCUENTRA UN ARCHIVO CON ESTE NOMBRE******")

    def renameCloud(self):
        arrayRuta = gG.arrayRuta(self.ruta)
        arrayRutaAux = arrayRuta[0:-1]  # solo tomo parte de sin el file.txt

        servicio = gC.servicioCloud()

        resultado = gC.navegacionCarpetasC(
            servicio, arrayRutaAux, '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm')  # navego lo maximo posible, obtengo id de la carpeta
        idCarpetaCloud = resultado[1]["id"]

        if len(arrayRuta) > 1:  # por si es la rama principal no subcarpetas
            resultado = gC.navegacionCarpetasC(
                servicio, [arrayRuta[-1]], idCarpetaCloud)  # navego lo maximo posible, con respuesta file.txt
        else:
            idCarpetaCloud = '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm'

        if len(resultado[0]) == 0:  # existe la ruta
            file_name = self.nombre.replace("/", "")

            # para que no se repita
            gC.renameCloud(
                servicio, resultado[1]["id"], '_'+resultado[1]["name"])

            # responseExist = servicio.files().list(
            #     q=f"'{idCarpetaCloud}' in parents and name='{file_name}'").execute()
            files = gC.existeNombreC(servicio, idCarpetaCloud, file_name)

            if files["existe"] == "true":
                gC.renameCloud(
                    servicio, resultado[1]["id"], resultado[1]["name"])
                print(f"nombre ya existe")
            else:
                gC.renameCloud(servicio, resultado[1]["id"], file_name)
                print(f"Se renombro ")
        else:
            print(f"La ruta especificada {self.ruta}, esta mal")




        
            

        
        
    

