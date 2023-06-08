from Comandos.create import Create
from Comandos.configure import Configure


class Leer:
    def __init__ (self,):
        #
        self.localmente=False
        self.encryptLog=False
        self.encryptRead=False
        self.llave="s"

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
                            #ejecucion configure
                            comandoConfigure.printConfiguracion()
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
                   


