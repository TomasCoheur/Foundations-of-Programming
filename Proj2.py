# Tomas Coheur    n: 93621

#cria_celula: {1, 0, 1} -> celula
#cria_celula: construtor
def cria_celula(v):
    if v in [0,1,-1]:
        return [v]     #lista pq + facil modificar
    else:
        raise ValueError('cria_celula: argumento invalido.')

#obter_valor: celula -> {1, 0, -1}
#obter_valor: seletor
def obter_valor(c):
    return c[0]   #valor de celula
    
#inverte_estado: celula -> celula
#inverte_estado: modificador pt destrutiva
def inverte_estado(c):
    if c[0] == 1:
        c[0] = 0
    elif c[0] == 0:
        c[0] = 1
    return c     #celula com o seu valor invertido: 1->0, 0->1, -1 -> -1

#eh_celula: universal -> logico
#eh_celula: reconhecedor
def eh_celula(arg):
    return arg in [[0],[1],[-1]]    #verifica que arg = celula

#celulas_iguais: celula x celula -> logico
#celulas_iguais: teste
def celulas_iguais(c1,c2):
    return eh_celula(c1) and eh_celula(c2) and c1 == c2   #compara 2 celulas

#celula_para_str: celula -> cad.caracteres
#celula_para_str: transformador
def celula_para_str(c):
    if c == [1]:
        return '1'
    elif c == [0]:            #celula torna-se string
        return '0'
    elif c == [-1]:
        return 'x'

#cria_coordenada: N x N -> coordenada
#cria_coordenada: construtor
def cria_coordenada(l,c):
    if l in [0,1,2] and c in [0,1,2]:
        return (l,c)      #tuplo pq n ha alteracoes nas variaveis
    else:
        raise ValueError('cria_coordenada: argumentos invalidos.')

#coordenada_linha: coordenada -> N
#coordenada_linha: selector
def coordenada_linha(c):
    return c[0]          #valor da linha do tabuleiro

#coordenada_coluna: coordenada -> N
#coordenada_coluna: seletor
def coordenada_coluna(c):
    return c[1]          #valor da coluna do tabuleiro

#eh_coordenada: universal -> logico
#eh_coordenada: reconhecedor
def eh_coordenada(c):              #verifica que c = coordenada   
    return isinstance(c,tuple) and len(c) == 2\
           and (coordenada_linha(c) in [0,1,2])\
           and (coordenada_coluna(c) in [0,1,2])

#coordenadas_iguais: coordenada x coordenada -> logico
#coordenadas_iguais: teste
def coordenadas_iguais(c1,c2):
    return c1 == c2          #compara duas coordenadas

#coordenada_para_str: coordenada -> cad.caracteres
#coordenada_para_str: transformador
def coordenada_para_str(c):
    return str(c)          #coordenada torna-se string

#tabuleiro_inicial: {} -> tabuleiro
#tabuleiro_inicial: construtor
def tabuleiro_inicial():
    return [[-1,-1,-1],[0,0,-1],[0,-1]]    #lista pq mais facil modificar

#str_para_tabuleiro: cad.caracteres -> tabuleiro
#str_para_tabuleiro: construtor
def str_para_tabuleiro(s):
    if isinstance(s,str):
        t = eval(s)               #tirar strings
        if isinstance(t,tuple) and len(t) == 3\
            and all(type(e) == tuple for e in t)\
            and len(t[0]) == 3 and len(t[1]) == 3 and len(t[2])== 2\
            and all(colunas in [0,1,-1] for linhas in t for colunas in linhas ):
            t1 = [list(t[0])] + [list(t[1])] + [list(t[2])]   #lista pq mais facil modificar 
            return t1
        else:
            raise ValueError('str_para_tabuleiro: argumento invalido.')
    else:
        raise ValueError('str_para_tabuleiro: argumento invalido.')

#tabuleiro_dimensao: tabuleiro -> N
#tabuleiro_dimensao: seletor
def tabuleiro_dimensao(t):
    return 3       #dimensao do tabuleiro = 3

#tabuleiro_celula: tabuleiro x coordenada -> celula
#tabuleiro_celula: seletor
def tabuleiro_celula(t,coor):              #devolve celula correspondente a uma coordenada do tabuleiro
    if coordenada_linha(coor) == 2 and coordenada_coluna(coor) == 1:
        return [t[2][0]]            
    elif coordenada_linha(coor) == 2 and coordenada_coluna(coor) == 2:
        return [t[2][1]]
    else:
        return [t[coordenada_linha(coor)][coordenada_coluna(coor)]]

#tabuleiro_substitui_celula: tabuleiro x celula x coordenada -> tabuleiro
#tabuleiro_substitui_celula: modificador pt destrutiva
def tabuleiro_substitui_celula(t,cel,coor):
    if eh_tabuleiro(t) and eh_coordenada(coor) and eh_celula(cel):
        if coor[0] == 2:
            t[coor[0]][coor[1]-1] = obter_valor(cel)
        else:
            t[coor[0]][coor[1]] = obter_valor(cel)
    else:
        raise ValueError('tabuleiro_substitui_celula: argumentos invalidos.')
    return t            #devolve tabuleiro com celula recebida na coordenada dada

#tabuleiro_inverte_estado: tabuleiro x coordenada -> tabuleiro

#tabuleiro_inverte_estado: modificador pt destrutiva
def tabuleiro_inverte_estado(t,coor):
    if eh_tabuleiro(t) and eh_coordenada(coor) and not(coordenada_linha(coor) == 2 and coordenada_coluna(coor) == 0):
        if coordenada_linha(coor) == 2:
            t[coordenada_linha(coor)][coordenada_coluna(coor)-1] = obter_valor(inverte_estado(tabuleiro_celula(t, coor)))
        else:
            t[coordenada_linha(coor)][coordenada_coluna(coor)] = obter_valor(inverte_estado(tabuleiro_celula(t, coor)))
    else:
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')
    return t             #devolve tabuleiro com valor de coor invertido

#eh_tabuleiro: universal -> logico
#eh_tabuleiro: reconhecedor
def eh_tabuleiro(arg):         #verifica que arg = tabuleiro
    return (isinstance(arg, list)) and (len(arg) == 3) \
            and (isinstance(arg[0], list)) and (isinstance(arg[1], list)) and (isinstance(arg[2], list)) \
            and (len(arg[0]) == 3) and (len(arg[1]) == 3) and (len(arg[2]) == 2) \
            and (arg[0][0] in [0, 1, -1]) and (arg[0][1] in [0, 1, -1]) and (arg[0][2] in [0, 1, -1]) \
            and (arg[1][0] in [0, 1, -1]) and (arg[1][1] in [0, 1, -1]) and (arg[1][2] in [0, 1, -1]) \
            and (arg[2][0] in [0, 1, -1]) and (arg[2][1] in [0, 1, -1])

#tabuleiros_iguais: tabuleiro x tabuleiro -> logico
#tabuleiros_iguais: teste
def tabuleiros_iguais(t1,t2):
    return t1 == t2 and eh_tabuleiro(t1) and eh_tabuleiro(t2)    #compara 2 tabuleiros

#tabuleiro_para_str: tabuleiro -> cad.caracteres
#tabuleiro_para_str: transformador
def tabuleiro_para_str(t):               #transforma tabuleiro numa string (representacao externa)
    return '+-------+\n|...'+celula_para_str(tabuleiro_celula(t,(0,2)))+'...|\n|..'\
           +celula_para_str(tabuleiro_celula(t,(0,1)))+'.'+celula_para_str(tabuleiro_celula(t,(1,2)))\
           +'..|\n|.'+celula_para_str(tabuleiro_celula(t,(0,0)))+'.'+celula_para_str(tabuleiro_celula(t,(1,1)))\
           +'.'+celula_para_str(tabuleiro_celula(t,(2,2)))+'.|\n|..'+celula_para_str(tabuleiro_celula(t,(1,0)))\
           +'.'+celula_para_str(tabuleiro_celula(t,(2,1)))+'..|\n+-------+'

#porta_x: tabuleiro x {'E', 'D'} -> tabuleiro
def porta_x(t,p):     #inverte o estado de todas as celulas da segunda linha ou segunda coluna dependendo do lado escolhido
    if eh_tabuleiro(t) and (p == 'E' or p == 'D'):
        if p == 'E':
            nv1 = tabuleiro_inverte_estado(t,cria_coordenada(1,0))          
            nv2 = tabuleiro_inverte_estado(nv1,cria_coordenada(1,1))        #cada linha inverte o estado de uma celula
            nv3 = tabuleiro_inverte_estado(nv2,cria_coordenada(1,2))
        elif p == 'D':
            nv1 = tabuleiro_inverte_estado(t, cria_coordenada(2, 1))
            nv2 = tabuleiro_inverte_estado(nv1, cria_coordenada(1, 1))
            nv3 = tabuleiro_inverte_estado(nv2, cria_coordenada(0, 1))
        return nv3
    else:
        raise ValueError('porta_x: argumentos invalidos.')

#porta_z: tabuleiro x {'E', 'D'} -> tabuleiro    
def porta_z(t,p):     #inverte o estado de todas as celulas da primeira linha ou ultima coluna dependendo do lado escolhido
    if eh_tabuleiro(t) and (p == 'E' or p == 'D'):
        if p == 'E':
            nv1 = tabuleiro_inverte_estado(t, cria_coordenada(0, 0))
            nv2 = tabuleiro_inverte_estado(nv1, cria_coordenada(0, 1))     #cada linha inverte o estado de uma celula
            nv3 = tabuleiro_inverte_estado(nv2, cria_coordenada(0, 2))
        elif p == 'D':
            nv1 = tabuleiro_inverte_estado(t, cria_coordenada(2, 2))
            nv2 = tabuleiro_inverte_estado(nv1, cria_coordenada(1, 2))
            nv3 = tabuleiro_inverte_estado(nv2, cria_coordenada(0, 2))
        return nv3
    else:
        raise ValueError('porta_z: argumentos invalidos.')

#porta_h: tabuleiro x {'E', 'D'} -> tabuleiro    
def porta_h(t,p):    #troca as celulas de primeira linha com as da segunda e da segunda coluna com as da ultima coluna
    if eh_tabuleiro(t) and (p == 'E' or p == 'D'):
        if p == 'E':
            val1 = obter_valor(tabuleiro_celula(t,cria_coordenada(0,0)))
            val2 = obter_valor(tabuleiro_celula(t,cria_coordenada(0,1)))     #guardar o valor das celulas que sao substitidas
            val3 = obter_valor(tabuleiro_celula(t,cria_coordenada(0,2)))
            nv1 = tabuleiro_substitui_celula(t,tabuleiro_celula(t,cria_coordenada(1,0)),cria_coordenada(0,0))
            nv2 = tabuleiro_substitui_celula(nv1,cria_celula(val1),cria_coordenada(1,0))
            nv3 = tabuleiro_substitui_celula(nv2,tabuleiro_celula(t,cria_coordenada(1,1)),cria_coordenada(0,1))
            nv4 = tabuleiro_substitui_celula(nv3,cria_celula(val2),cria_coordenada(1,1))
            nv5 = tabuleiro_substitui_celula(nv4,tabuleiro_celula(t,cria_coordenada(1,2)),cria_coordenada(0,2))
            nv6 = tabuleiro_substitui_celula(nv5,cria_celula(val3),cria_coordenada(1,2))    #cada linha substitui uma celula
        elif p == 'D':
            val1 = obter_valor(tabuleiro_celula(t,cria_coordenada(2,2)))
            val2 = obter_valor(tabuleiro_celula(t,cria_coordenada(1,2)))
            val3 = obter_valor(tabuleiro_celula(t,cria_coordenada(0,2)))
            nv1 = tabuleiro_substitui_celula(t,tabuleiro_celula(t,cria_coordenada(2,1)),cria_coordenada(2,2))
            nv2 = tabuleiro_substitui_celula(nv1,cria_celula(val1),cria_coordenada(2,1))
            nv3 = tabuleiro_substitui_celula(nv2,tabuleiro_celula(t,cria_coordenada(1,1)),cria_coordenada(1,2))
            nv4 = tabuleiro_substitui_celula(nv3,cria_celula(val2),cria_coordenada(1,1))
            nv5 = tabuleiro_substitui_celula(nv4,tabuleiro_celula(t,cria_coordenada(0,1)),cria_coordenada(0,2))
            nv6 = tabuleiro_substitui_celula(nv5,cria_celula(val3),cria_coordenada(0,1))
        return nv6
    else:
        raise ValueError('porta_h: argumentos invalidos.')

#hello_quantum: cad.caracteres -> logico
def hello_quantum(cad):     #permite jogar ao jogo hello quantum
    print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:')
    enunciado = cad.split(':')    #divide cad em duas partes
    tf = str_para_tabuleiro(enunciado[0])  #tabuleiro a que queremos chegar(tabuleiro final)
    ntentativas = eval(enunciado[1])
    print(tabuleiro_para_str(tf))
    print('Comecando com o tabuleiro que se segue:')
    print(tabuleiro_para_str(tabuleiro_inicial()))
    ti = tabuleiro_inicial()
    contador = 0     #conta o numero de jogadas feitas
    while not(tabuleiros_iguais(ti,tf)) and contador < ntentativas:
        porta = input('Escolha uma porta para aplicar (X, Z ou H): ')
        qubit = input('Escolha um qubit para analisar (E ou D): ')
        if porta == 'X':
            ti = porta_x(ti,qubit)
        elif porta == 'Z':
            ti = porta_z(ti,qubit)
        elif porta == 'H':
            ti = porta_h(ti,qubit)
        print(tabuleiro_para_str(ti))
        contador += 1
    if tabuleiros_iguais(ti,tf):
        print('Parabens, conseguiu converter o tabuleiro em', contador, 'jogadas!')
        conseguido = True   
    else:
        conseguido = False
    return conseguido    #True se fim sem ultrapassar o numero de jogadas e False em caso contrario

print(hello_quantum("((1, -1, 0), (-1, -1, -1), (-1, 1)):4"))
