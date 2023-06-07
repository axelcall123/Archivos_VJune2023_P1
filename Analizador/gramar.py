import ply.lex as lex
import ply.yacc as yacc

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

t_CONFIGURE=r'configure'
t_CREATE=r'create'
t_DELETE=r'delete'
t_COPY=r'copy'
t_TRANSFER=r'transfer'
t_RENAME=r'rename'
t_MODIFY=r'modify'
t_ADD=r'add'
t_BACKUP=r'backup'
t_EXEC=r'exec'

t_TYPE=r'-type->'
t_ENCRYPTLOG = r'-encrypt_log->'
t_ENCRYPTREAD = r'-encrypt_read->'
t_LLAVE=r'-llave->'
t_NAME = r'-name->'
t_BODY = r'-body->'
t_PATH = r'-path->'
t_FROM = r'-from->'
t_TO = r'-to->'
t_MODE = r'-mode->'

t_LOCAL=r'"local"'
t_CLOUD=r'"cloud"'
t_TRUE=r'true'
t_FALSE=r'false'

def t_ARCHIVO(t):
    r'("\w+[.]\w+")|(\w+[.]\w+)'
    t.value = t.value.lower()
    return t

def t_RUTA(t):
    r'([/](\w+[/])+(\w+[.]\w+)?)|(["][/](\w?[\w ]+[/])+(\w+[.]\w+)?["])'
    t.value = t.value.lower()
    return t

def t_STRING(t):
    r'"[^"]+"'
    t.value = t.value.lower()
    return t


t_ignore = ' \t\n'


def t_error(t):
    print(f"Caracter Invalido: '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

# Parser
Arbol=[]
def p_inicio(p):
    '''inicio : lexico
    '''
    p[0]=Arbol

def p_lexico(p):
    '''lexico : lexico comandos
                | comandos
    '''


def p_comandos(p):
    '''comandos : maincomando subcomando
    '''
    arr = []
    arr.append("comandos")
    arr.append(p[1])
    arr.append(p[2])
    Arbol.append(arr)
    

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

def p_sub_comando(p):
    '''subcomando : TYPE tipo
                    | ENCRYPTLOG encriptado
                    | ENCRYPTREAD encriptado
                    | LLAVE STRING
                    | NAME ARCHIVO
                    | BODY STRING
                    | PATH RUTA
                    | FROM RUTA
                    | TO RUTA
                    | MODE tipo
    '''
    arr=[]
    arr.append("subcomando")
    arr.append(p[1])
    arr.append(p[2])
    p[0]=arr


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


def p_error(p):
    if p:
        print(f"Error sintactico en el token '{p.value}'")
    else:
        print("Error sintactico EOF")


parser = yacc.yacc()

# f = open("./entradas.txt", "r")
# input = f.read()
# print(input)
# parser.parse(input)
# print(Arbol)