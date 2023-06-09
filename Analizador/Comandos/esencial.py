from Comandos.create import Create
from Comandos.configure import Configure
from Comandos.delete import Delete
from Comandos.copy import Copy
from cripto import encrypt_string,decrypt_string


 
class Leer:
    def __init__ (self,):
        self.localmente=False
        self.encryptLog=False
        self.encryptRead=False
        self.llave=""

    def comando(self,arreglo):
       
        #la cantidad de comandos
        #print(arreglo)
        for element in arreglo:
            # cuales comandos
            for comando in element:      
                # Separando comandos
                if(comando=="configure"): #!Comando Configure
                    comandoConfigure=Configure()
                    for parametros in element:
                        if(parametros!="configure"):
                            for elementos2 in parametros:
                                if(elementos2[0]=="-type->"):
                                    self.localmente=comandoConfigure.type(elementos2[1])
                                elif(elementos2[0]=="-encrypt_log->"):
                                    self.encryptLog=comandoConfigure.encryptLog(elementos2[1])
                                elif(elementos2[0]=="-encrypt_read->"):
                                    self.encryptRead=comandoConfigure.encryptRead(elementos2[1])
                                elif(elementos2[0]=="-llave->"):
                                    self.llave=comandoConfigure.llave(elementos2[1])
                            #print configure
                            #comandoConfigure.printConfiguracion()
                if(comando=="create" and self.localmente): #!Comando Create y self.local es True
                        #self.localmente=False
                        comandoCreate=Create()
                        for parametros in element:
                            if(parametros!="create"):
                                for elementos2 in parametros:
                                    if(elementos2[0]=="-name->"):
                                        comandoCreate.name(elementos2[1])
                                    elif(elementos2[0]=="-path->"):
                                        comandoCreate.path(elementos2[1])
                                    elif(elementos2[0]=="-body->"):
                                        comandoCreate.body(elementos2[1])
                                #creando archivo
                                comandoCreate.creacionLocal()
                if(comando=="delete" and self.localmente): #!Comando delete
                        #self.localmente=False
                        comandoDelete=Delete()
                        for parametros in element:
                            if(parametros!="delete"):
                                for elementos2 in parametros:
                                    if(elementos2[0]=="-path->"):
                                        comandoDelete.path(elementos2[1])
                                    elif(elementos2[0]=="-name->"):
                                        comandoDelete.name(elementos2[1])
                                #borrar
                                comandoDelete.borrar()
                if(comando=="copy" and self.localmente): #!Comando delete
                        #self.localmente=False
                        comandoDelete=Copy()
                        for parametros in element:
                            if(parametros!="copy"):
                                for elementos2 in parametros:
                                    if(elementos2[0]=="-from->"):
                                        comandoDelete.desde(elementos2[1])
                                    elif(elementos2[0]=="-to->"):
                                        comandoDelete.to(elementos2[1])
                                #copiar
                                comandoDelete.copiar()
                   


