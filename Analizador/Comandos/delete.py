import os
import Analizador.Comandos._generalCloud as gC  # alias
import Analizador.Comandos._general as gG
class Delete:
    def __init__ (self,):
        self.ruta=""
        self.nombre=""

        self.num=0

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

    def borrar(self):
        pathArchivo= "./archivos"+self.ruta
        if(os.path.exists(pathArchivo+self.nombre)&(self.nombre!="")):
            os.remove(pathArchivo+self.nombre)
            print("******EL ARCHIVO FUE BORRADO CON EXITO******")
        else:
            if(os.path.exists(pathArchivo)):
                x=0
                self.elementosDirectorio(pathArchivo)
                while x<=self.num:
                    self.elementosDirectorio(pathArchivo)
                    print(x)
                    x=x+1
                os.rmdir(pathArchivo)
                print("******LA CARPETA FUE BORRADO CON EXITO******")
            else:
                #si no existe nada
                 print("******ERROR NO SE ENCONTRO LA DIRECCION******")
        
    def elementosDirectorio(self,path):
        contenido = os.listdir(path)
        print(contenido)
        print(path+"-------+------------------------/-")
        if(contenido==[]):
            return 
        else:
            for element in contenido:
                print("ESTOS SONASDJKSADYHASUJIKDSAD: "+element)
                #SI ES ARCHIVO
                if("." in element):
                    os.remove(path+"/"+element)
                    print("*****SE ELIMINO EL ARCHIVO DENTRO DE CARPETA: "+path+element)
                #SI ES CARPETA
                else:
                    contenido2=os.listdir(path+element)
                    #print("-------------+----+++++++++++++++++++++++++++++++++++++++++++++")
                    print(contenido2)
                    if(contenido2==[]):
                        #print("-------------+-----------------------------------------------")
                        print(path+element)
                        os.rmdir(path+element)
                        print("*****SE ELIMINO EL CARPETA DENTRO DE CARPETA: "+path+element)
                    else:
                        print(path+element+"-------+------------------------/")
                        self.num=self.num+1
                        self.elementosDirectorio(path+element+"/")

            
            




        
            

        
        
    

