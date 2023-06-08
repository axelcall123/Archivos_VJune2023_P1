from Comandos.create import Create


class Leer:
    def comando(self,arreglo):
        #la cantidad de comandos
        for element in arreglo:
            # cuales comandos
            for comando in element:      
                # Separando comandos
                if(comando=="create"): #!Comando Create
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
                   


