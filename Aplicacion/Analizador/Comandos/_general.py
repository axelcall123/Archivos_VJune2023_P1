def arrayRuta(ruta):
    arrayRuta = ruta.split("/")
    for i in range(len(arrayRuta)-1):
        if arrayRuta[i] == '':
            arrayRuta.pop(i)
    return arrayRuta
