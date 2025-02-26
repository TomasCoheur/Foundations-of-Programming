# Tomas Coheur 93621

# A funcao eh_tabuleiro recebe um argumento e devolve True se o argumento for um tabuleiro e False em caso contrario
def eh_tabuleiro(argumento):
    contador = 0    # conta o nb de caracteristicas do argumento que definem um tabuleiro
    if isinstance(argumento,tuple) :
        contador += 1
        if (len(argumento)) == 3 :
            contador +=1
            if type(argumento[0]) == tuple and type(argumento[1]) == tuple and type(argumento[2]) == tuple:
                contador +=1
                if len(argumento[0]) == 3 and len(argumento[1]) == 3 and len(argumento[2]) == 2 :
                    for e in argumento[0]:
                        if e == 0 or e == 1 or e == -1:
                            contador += 1
                    for e2 in argumento[1]:
                        if e2 == 0 or e2 == 1 or e2 == -1:
                            contador += 1
                    for e3 in argumento[2]:
                        if e3 == 0 or e3 == 1 or e3 == -1:
                            contador += 1
    return contador == 11

# A funcao tabuleiro_str recebe um tabuleiro e devolve uma string permitido visualisar o tabuleiro como esta no jogo
def tabuleiro_str(tabuleiro):
    cdct = "+-------+\n" # cdct = cadeia de caracteres
    fim = "+-------+"
    barraponto = "|."
    pontobarra = ".|\n"
    ponto = "."
    tabuleiro2 = ()
    if eh_tabuleiro(tabuleiro) != True:
        raise ValueError("tabuleiro_str: argumento invalido")
    for i in range(len(tabuleiro)):
        for e in tabuleiro[i]:
            if e == 1:
                tabuleiro2 += (1,)
            if e == 0:
                tabuleiro2 += (0,)
            if e == -1:
                tabuleiro2 += ("x",)
    cdct += barraponto + 2*ponto + str(tabuleiro2[2]) + 2*ponto + pontobarra
    cdct += barraponto + ponto + str(tabuleiro2[1]) + ponto + str(tabuleiro2[5]) + ponto + pontobarra
    cdct += barraponto + str(tabuleiro2[0]) + ponto + str(tabuleiro2[4]) + ponto + str(tabuleiro2[7]) + pontobarra
    cdct += barraponto + ponto + str(tabuleiro2[3]) + ponto + str(tabuleiro2[6]) + ponto + pontobarra + fim
    return cdct

# A funcao tabuleiro_iguais recebe dois tabuleiros e compara-os. Se forem iguais devolve True se nao devolve False
def tabuleiros_iguais(tabuleiro1,tabuleiro2):
    if eh_tabuleiro(tabuleiro1) == False or eh_tabuleiro(tabuleiro2) == False:
        raise ValueError("tabuleiros_iguais: um dos argumentos nao e tabuleiro")
    return tabuleiro1 == tabuleiro2

# A funcao porta_x recebe um tabuleiro e um caracter E ou D (para esquerda ou direita)\
# e devolve um novo tabuleiro onde a linha de uma das celulas inferiores de um qubit (dependendo do lado) foi invertida
def porta_x(tabuleiro,caracter):
    tabuleiro_novo = ()
    tuplo1 = () # valores alterados do primeiro tuplo do tabuleiro
    tuplo2 = () # valores alterados do segundo tuplo do tabuleiro
    tuplo3 = () # valores alterados do terceiro tuplo do tabuleiro
    if eh_tabuleiro(tabuleiro) == False or (caracter != "E" and caracter != "D") :
        raise ValueError("porta_x: um dos argumentos e invalido")
    elif caracter == "E":
        for e in range(len(tabuleiro[1])):
            if tabuleiro[1][e] == 1:
                tuplo2 += (0,)
            elif tabuleiro[1][e] == 0:
                tuplo2 += (1,)
            elif tabuleiro[1][e] == -1:
                tuplo2 += (-1,)
        tabuleiro_novo += (tabuleiro[0],) + (tuplo2,) + (tabuleiro[2],)
    elif caracter == "D":
        if tabuleiro[1][1] == 1:
            tuplo2 += (0,)
        elif tabuleiro[1][1] == 0:
            tuplo2 += (1,)
        elif tabuleiro[1][1] == -1:
            tuplo2 += (-1,)
        if tabuleiro[0][1] == 1:
            tuplo1 += (tabuleiro[0][0],) + (0,) + (tabuleiro[0][2],)
        elif tabuleiro[0][1] == 0:
            tuplo1 += (tabuleiro[0][0],) + (1,) + (tabuleiro[0][2],)
        elif tabuleiro[0][1] == -1:
            tuplo1 += (tabuleiro[0][0],) + (-1,) + (tabuleiro[0][2],)
        if tabuleiro[2][0] == 1:
            tuplo3 += (0,)
        elif tabuleiro[2][0] == 0:
            tuplo3 += (1,)
        elif tabuleiro[2][0] == -1:
            tuplo3 += (-1,)
        tabuleiro_novo += (tuplo1,)
        tabuleiro_novo += ((tabuleiro[1][0],) + tuplo2 + (tabuleiro[1][2],),)
        tabuleiro_novo += (tuplo3 + (tabuleiro[2][1],),)
    return tabuleiro_novo

# A funcao porta_z recebe um tabuleiro e um caracter E ou D (para esquerda ou direita)\
# e devolve um novo tabuleiro onde a linha de uma das celulas superiores de um qubit (dependendo do lado) foi invertida
def porta_z(tabuleiro,caracter):
    tabuleiro_novo = ()
    tuplo1 = () # valores alterados do primeiro tuplo do tabuleiro
    tuplo2 = () # valores alterados do segundo tuplo do tabuleiro
    tuplo3 = () # valores alterados do terceiro tuplo do tabuleiro
    if eh_tabuleiro(tabuleiro) == False or (caracter != "E" and caracter != "D") :
        raise ValueError("porta_z: um dos argumentos e invalido")
    elif caracter == "E":
        for e in range(len(tabuleiro[0])):
            if tabuleiro[0][e] == 1:
                tuplo1 += (0,)
            elif tabuleiro[0][e] == 0:
                tuplo1 += (1,)
            elif tabuleiro[0][e] == -1:
                tuplo1 += (-1,)
        tabuleiro_novo += (tuplo1,) + (tabuleiro[1],)+ (tabuleiro[2],)
    elif caracter == "D":
        if tabuleiro[0][2] == 1:
            tuplo1 += (0,)
        elif tabuleiro[0][2] == 0:
            tuplo1 += (1,)
        elif tabuleiro[0][2] == -1:
            tuplo1 += (-1,)
        if tabuleiro[1][2] == 1:
            tuplo2 += (0,)
        elif tabuleiro[1][2] == 0:
            tuplo2 += (1,)
        elif tabuleiro[1][2] == -1:
            tuplo2 += (-1,)
        if tabuleiro[2][1] == 1:
            tuplo3 += (0,)
        elif tabuleiro[2][1] == 0:
            tuplo3 += (1,)
        elif tabuleiro[2][1] == -1:
            tuplo3 += (-1,)
        tabuleiro_novo += ((tabuleiro[0][0],) + (tabuleiro[0][1],) + tuplo1,)
        tabuleiro_novo += ((tabuleiro[1][0],) + (tabuleiro[1][1],) + tuplo2,)
        tabuleiro_novo += ((tabuleiro[2][0],) + tuplo3,)
    return tabuleiro_novo

# A funcao porta_h recebe um tabuleiro e um caracter E ou D (esquerda ou direita)
# e troca a linha com a celula superior de um qubit com a linha com a celula inferior desse mesmo qubit dependendo do caracter escolhido
def porta_h(tabuleiro,caracter):
    tabuleiro_novo = ()
    tuplo1 = () # primeiro tuplo do tabuleiro novo
    tuplo2 = () # segundo tuplo do tabuleiro novo
    tuplo3 = () # terceiro tuplo do tabuleiro novo
    if eh_tabuleiro(tabuleiro) == False or (caracter != "E" and caracter != "D"):
       raise ValueError("porta_h: um dos argumentos e invalido")
    if caracter == "E":
        tabuleiro_novo += (tabuleiro[1],) + (tabuleiro[0],) + (tabuleiro[2],)
    elif caracter == "D":
        tuplo1 += (tabuleiro[0][0],) + (tabuleiro[0][2],) + (tabuleiro[0][1],)
        tuplo2 += (tabuleiro[1][0],) + (tabuleiro[1][2],) + (tabuleiro[1][1],)
        tuplo3 += (tabuleiro[2][1],) + (tabuleiro[2][0],)
        tabuleiro_novo += (tuplo1,) + (tuplo2,) + (tuplo3,)
    return tabuleiro_novo
