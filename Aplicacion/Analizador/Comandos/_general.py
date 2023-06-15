from datetime import datetime
def arrayRuta(ruta):
    arrayRuta = ruta.split("/")
    for i in range(len(arrayRuta)-1):
        if arrayRuta[i] == '':
            arrayRuta.pop(i)
    return arrayRuta

def bitacora(iO:str,com:str,res:str)->bytes:#input/ouput
    now = datetime.now()
    # tiempo 01/01/01 1: 1: 1
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    strBitacora = f"{dt_string} - {iO} - {com} - Usuario:{res}\n"
    return bytes(strBitacora, 'utf-8')
