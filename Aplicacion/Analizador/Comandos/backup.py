
import Aplicacion.Analizador.Comandos._generalCloud as gC  # alias
import Aplicacion.Analizador.Comandos._general as gG
#import tempfile
#from Aplicacion.variablesGlobales import temporalFile
class Backup:
    def __init__ (self,tipo):
        self.tipo=tipo

    def backupA(self):
        folderLocal = './archivos'
        folderCloud = '1JrC25YFAk-DL_nsSSQt6vZzt1zKruXYm'
        #bitacora<<<<>>>>>
        gG.escribirTemp('input', 'backup', f'de tipo {self.tipo}')
        servicio=gC.servicioCloud()
        if self.tipo=="local":#subo a la nuve
            gC.upLoading(servicio,folderLocal,folderCloud)
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'backup', 'se suvieron todos los archivo')
            print("se suvieron todos los archivos")
        if self.tipo == "cloud":#lo bajo
            #bitacora<<<<>>>>>
            gG.escribirTemp(
                'output', 'backup', 'se bajaron todos los archivo')
            gC.downLoading(servicio, folderLocal, folderCloud)
            print("se bajaron todos los archivos")
