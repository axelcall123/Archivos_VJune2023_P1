from Analizador.gramar import gramarMain
from Analizador.Comandos.esencial import Leer
resultado = gramarMain()
analizar = Leer()
analizar.comando(resultado)
