import os
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
        pathArchivo= "../Archivo"+self.ruta
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
        pathNuevoNombre="../Archivo"+nuevaRuta+"/"+self.nombre
        
        if(os.path.exists(pathArchivo)& (not(os.path.exists(pathNuevoNombre)))):
            os.rename(pathArchivo,pathNuevoNombre)
            print("******EL ARCHIVO FUE RENOMBRADO CON EXITO******")
            
        else:
             print("******ERROR NO SE ENCONTRO LA DIRECCION O YA SE ENCUENTRA UN ARCHIVO CON ESTE NOMBRE******")





        
            

        
        
    

