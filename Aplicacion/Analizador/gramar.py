import Aplicacion.Analizador.ply.lex as lex
import Aplicacion.Analizador.ply.yacc as yacc
from Aplicacion.Analizador.Comandos.esencial import Leer
from Aplicacion.Analizador.cripto import decrypt_hex_string
import re
#from Comandos.esencial import Leer

resultado = None

#LEXICO
tokens = (
    'CONFIGURE',
    'CREATE',
    'DELETE',
    'COPY',
    'TRANSFER',
    'RENAME',
    'MODIFY',
    'ADD',
    'BACKUP',
    'EXEC',

    'TYPE',
    'ENCRYPTLOG',
    'ENCRYPTREAD',
    'LLAVE',

    'NAME',
    'BODY',
    'PATH',

    'FROM',
    'TO',
    'MODE',

    'LOCAL',
    'CLOUD',

    'TRUE',
    'FALSE',

    'ARCHIVO',
    'RUTA',
    'STRING'
)

t_CONFIGURE = r'configure'
t_CREATE = r'create'
t_DELETE = r'delete'
t_COPY = r'copy'
t_TRANSFER = r'transfer'
t_RENAME = r'rename'
t_MODIFY = r'modify'
t_ADD = r'add'
t_BACKUP = r'backup'
t_EXEC = r'exec'

t_TYPE = r'-type->'
t_ENCRYPTLOG = r'-encrypt_log->'
t_ENCRYPTREAD = r'-encrypt_read->'
t_LLAVE = r'-llave->'
t_NAME = r'-name->'
t_BODY = r'-body->'
t_PATH = r'-path->'
t_FROM = r'-from->'
t_TO = r'-to->'
t_MODE = r'-mode->'

#t_LOCAL = r'local|\"local\"'
#t_CLOUD = r'cloud|\"cloud\"'
#t_TRUE = r'true'
#t_FALSE=r'false'


def t_TRUE(t):
    r'true|\"true\"'
    t.value = t.value.lower()
    return t


def t_FALSE(t):
    r'false|\"false\"'
    t.value = t.value.lower()
    return t


def t_LOCAL(t):
    r'local|\"local\"'
    t.value = t.value.lower()
    return t


def t_CLOUD(t):
    r'cloud|\"cloud\"'
    t.value = t.value.lower()
    return t


def t_ARCHIVO(t):
    #r'(\"[\w ]+.\w+\")|(\w+.\w+)'
    r'(\"[\w ]+\.\w+\")|(\w+\.\w+)'
    t.value = t.value.lower()
    return t


def t_RUTA(t):
    #r'(\/(\w+|\"[\w ]+[\.\w+]?\")+)+\/?'
    #r'(\/(\w+|\"[\w ]+\"))((\/(\w+|\"[\w ]+\"))+|\/)(\/\"[\w ]+[.]\w+\"|[.]\w+)?'
    r'(\/((\w+(\.\w+)?)|(\"(\w|\s)+(\.\w+)?\")))+\/?'
    #r'((\/\w+)+(\/|(.\w+)))|(\/\"[\w ]+(([/][\w ]+)*)((.\w+\"\/)|(\"\/)))'
    t.value = t.value.lower()
    return t


def t_STRING(t):
    r'"[^"]+"'
    t.value = t.value.lower()
    return t


t_ignore = ' \t\n'


def t_error(t):
    print(f"Caracter Invalido: '{t.value[0]} ,{t}'")
    t.lexer.skip(1)


lexer = lex.lex(reflags=re.IGNORECASE)

# Parser


def p_inicio(p):
    '''inicio : lexico
    '''
    p[0] = p[1]


def p_lexico(p):
    '''lexico : lexico comandos
                | comandos
    '''
    if len(p)==3:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]


def p_comandos(p):
    '''comandos : maincomando subcomando
                | maincomando
    '''
    if len(p) == 3:
        arr = []
        arr.append(p[1])
        arr.append(p[2])
        #Arbol.append(arr)
        p[0]=arr
    else:
        arr = []
        arr.append(p[1])
        #Arbol.append(arr)
        p[0] = arr


def p_main_comando(p):
    '''maincomando : CONFIGURE 
                | CREATE
                | DELETE
                | COPY
                | TRANSFER
                | RENAME
                | MODIFY
                | ADD
                | BACKUP
                | EXEC
    '''
    p[0] = p[1]


def p_subcomando(p):
    '''subcomando : subcomando sub
                    | sub
    '''
    #print("tipo de:",type(p),type(p[0]),type(p[1]))
    #print("ppppp",type(p),p,p[0],p[1])#object, none, none|array
    #print("---")
    if len(p) == 3:
        arr = p[1]
        #arr.append("subcomando")
        arr.append(p[2])
        p[0] = arr
    elif len(p) == 2:
        arr = []
        #arr.append("subcomando")
        arr.append(p[1])
        p[0] = arr


def p_sub(p):
    '''sub : TYPE tipo
                    | ENCRYPTLOG encriptado
                    | ENCRYPTREAD encriptado
                    | LLAVE STRING
                    | NAME name
                    | BODY STRING
                    | PATH RUTA
                    | FROM RUTA
                    | TO RUTA
                    | MODE tipo
    '''
    arr = []
    #arr.append("sub")
    arr.append(p[1])
    arr.append(p[2])
    p[0] = arr


def p_tipo(p):
    '''tipo : LOCAL
            | CLOUD
    '''
    p[0] = p[1]


def p_encriptado(p):
    '''encriptado : TRUE
            | FALSE
    '''
    p[0] = p[1]


def p_name(p):
    '''name : ARCHIVO
    '''
    p[0] = p[1]


def p_error(p):
    if p:
        print(f"Error sintactico en el token '{p.value}', {p.lexer.lineno}")
        print(type(p))
    else:
        print("Error sintactico EOF")

# Lee los inputs que vienen del tkinter

# si el comando no esta codificado
def grammarInput(input):
    print("grammarInput")
    parser = yacc.yacc()
    resultado = parser.parse(input.lower())
    analizar = Leer()
    posibleEntrada=analizar.comando(resultado)
    #exec retorna otra contenido input desde def comando

    print(type(posibleEntrada)==str)
    if(type(posibleEntrada)==str):
        #Otra entrada volver a identificar si es codificado o no
        execInput(posibleEntrada)

def grammarInputCodificado(input):
    print("grammarInputCodificado")
    # si el input esta codificado solo son 2 saltos de lieas (\n)
    #el primero siempre sera configure
    lista=input.split("\n")
    contador=0
    analizar = Leer()
    llave=""
    for element in lista:
        print(element)
        #comando configure
        if (contador % 2 == 0):
            configure = element
            parser = yacc.yacc()
            resultado = parser.parse(configure.lower())
            #analizar tomara las validaciones
            analizar.comando(resultado)
        #comandos encriptados
        elif (contador % 2 == 1):
            #decodifica
            #si decodificacion es activa
            if(analizar.encryptRead):
                #eliminando comillas en llave
                if('"' in analizar.llave):
                    llave=analizar.llave.replace("\"", "" )
                else:
                    llave=analizar.llave
                #desencriptando
                byte_string = llave.encode("utf-8")
                comando=decrypt_hex_string(byte_string,element)
                parser = yacc.yacc()
                resultado = parser.parse(comando.lower())
                #analizar tomara las validaciones
                posibleEntrada=analizar.comando(resultado)
                #exec retorna otra contenido input desde def comando
                if(type(posibleEntrada)==str):
                    #Otra entrada volver a identificar si es codificado o no
                    execInput(posibleEntrada)
            else:
                print("error codificacion no es True")
        contador=contador+1


def execInput(inputExec):
    #mismo caso para main Window(otra entrada)
    posibleCodificado=inputExec.split("\n")[1]# Obteniendo el posible codificado 
    if("-" in posibleCodificado)|(posibleCodificado.lower()=="backup"):
        grammarInput(inputExec)
    else:
        grammarInputCodificado(inputExec)





def gramarMain():
    parser = yacc.yacc()
    f = open("Aplicacion/Analizador/entradas.txt", "r")
    input = f.read()
    #print(len(input.split("\n")))
    resultado = parser.parse(input.lower())
    #grammarInputCodificado(input)
    #print(resultado,'\n')
    #lectura=Leer()
    #lectura.comando(resultado)
    #print(resultado)
    return resultado
    #analizar=Leer()
    #analizar.comando(resultado)
