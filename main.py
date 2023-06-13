from Analizador.gramar import gramarMain
from Analizador.Comandos.esencial import Leer
resultado = gramarMain()
analizar = Leer()
# for res in resultado:
#     print(res)
analizar.comando(resultado)
