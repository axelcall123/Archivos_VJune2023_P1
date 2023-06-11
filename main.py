from Analizador.gramar import parser

while True:
    try:
        f = open("./Analizador/entradas.txt", "r")
        input = f.read()
        print(input)
        Arbol=parser.parse(input)
        print(Arbol)
    except EOFError:
        break
