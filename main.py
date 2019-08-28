# Algoritmo A* : f(x) = g(x) + h(x)

# Codigo desenvolvido por Maria Luiza e Tarcisio Bruni

# import time
import sys

listaAberta = []    # Lista com as coordenadas que não tiveram seus vizinhos verificados
listaFechada = []   # Lista com as coordenadas que tiveram seus vizinhos verificados

def desenhar(lista_coordenadas):
    print(f"### PERCURSO de {inicio} ate {final} ###")
    print(lista_coordenadas)
    print()

    '''
    delta = [[-1, 0],   # Para cima
             [1, 0],    # Para baixo
             [0, -1],   # Para esquerda
             [0, 1]]    # Para direita
    '''

    simbolo_cima = '^'
    simbolo_baixo = 'v'
    simbolo_esquerda = '<'
    simbolo_direita = '>'

    simbolo_obstaculo = '■'  # 1 no mapa
    simbolo_livre = '-'      # 0 no mapa
    simbolo_inicio = 'A'
    simbolo_final = 'B'

    resultado = []

    for i in mapa:
        resultado.append(i)

    atual = inicio
    simbolo = ''

    for pos in range(1, len(lista_coordenadas)):  # 0 1 2 ... 17        
        #print('%s ? %s' % (atual, lista_coordenadas[pos]))
        
        if (lista_coordenadas[pos] != inicio):
            if atual[0] > lista_coordenadas[pos][0]:    # Para cima
                simbolo = simbolo_cima  
            elif atual[0] < lista_coordenadas[pos][0]:  # Para baixo
                simbolo = simbolo_baixo
            elif atual[1] > lista_coordenadas[pos][1]:  # Para esquerda
                simbolo = simbolo_esquerda
            elif atual[1] < lista_coordenadas[pos][1]:  # Para direita
                simbolo = simbolo_direita
            
            if lista_coordenadas[pos] == final:     # Verifica se o próximo passo é a chegada
                x = lista_coordenadas[pos-1][0]
                y = lista_coordenadas[pos-1][1]
            else:
                x = lista_coordenadas[pos][0]
                y = lista_coordenadas[pos][1]
            resultado[x][y] = simbolo
            atual = lista_coordenadas[pos]
    
    resultado[inicio[0]][inicio[1]] = simbolo_inicio
    resultado[final[0]][final[1]] = simbolo_final

    print(resultado)
    for x in range(len(resultado)):
        for y in range(len(resultado[x])):
            if resultado[x][y] == 1:
                resultado[x][y] = simbolo_obstaculo
            elif resultado[x][y] == 0:
                resultado[x][y] = simbolo_livre
    
    print()
    print(resultado)
            
    return resultado            
            

def recuperar_caminho(atual):
    global dicPosicoesCalculadas

    percurso = []
    if atual != inicio:
        pontoOrigem = dicPosicoesCalculadas[atual][3]
    else:
        pontoOrigem = inicio

    percurso.append(atual)
    while pontoOrigem != inicio:
        percurso.append(pontoOrigem)
        pontoOrigem = dicPosicoesCalculadas[pontoOrigem][3]
    if inicio not in percurso:
        percurso.append(inicio)
    
    percurso.reverse()
    return percurso


def encontra_vizinhos(atual):
    '''
        # Vizinhos (linha , coluna)
        (atual[0]-1) , (atual[1])   # Em cima
        (atual[0]+1) , (atual[1])   # Em baixo
        (atual[0]) , (atual[1]-1)   # Esquerda
        (atual[0]) , (atual[1]+1)   # Direita
    '''
    global mapa
    global listaFechada
    
    vizinhos = [] # Lista de vizinhos
    linha_matriz = atual[0] # Indice da Linha na Matriz
    coluna_matriz = atual[1] # Indice da Coluna na Matriz

    # Checando a existencia de cada vizinho , se a célula não é barreira , se o vizinho não está na Lista Fechada 
    if( ((linha_matriz-1) >= 0) and (mapa[linha_matriz-1][coluna_matriz] != 1) ):  # Em cima
        vizinho_cima = (linha_matriz-1,coluna_matriz)
        if ( (vizinho_cima not in listaFechada) ):
            vizinhos.append(vizinho_cima)
    
    if( ((linha_matriz+1) <= len(mapa)-1) and (mapa[linha_matriz+1][coluna_matriz] != 1) ):   # Em baixo
        vizinho_baixo = (linha_matriz+1,coluna_matriz)
        if ( (vizinho_baixo not in listaFechada) ):
            vizinhos.append(vizinho_baixo)

    if( ((coluna_matriz-1) >= 0) and (mapa[linha_matriz][coluna_matriz-1] != 1) ):  # Esquerda
        vizinho_esquerda = (linha_matriz,coluna_matriz-1)
        if ( (vizinho_esquerda not in listaFechada)):
            vizinhos.append(vizinho_esquerda)

    if( ((coluna_matriz+1) <= len(mapa[0])-1) and (mapa[linha_matriz][coluna_matriz+1] != 1) ):  # Direita
        vizinho_direita = (linha_matriz,coluna_matriz+1)
        if ( (vizinho_direita not in listaFechada)):
            vizinhos.append(vizinho_direita)

    return vizinhos


def ordena_pelo_custo():
    global listaAberta
    listaAberta_aux = []
    
    for chave in listaAberta:
        listaAberta_aux.append(dicPosicoesCalculadas[chave])

    sorted(listaAberta_aux , key=lambda t: (t[1]+t[2]))

    listaAberta = []

    for elemento in listaAberta_aux:
        listaAberta.append(elemento[0])


def calcula_custos(pai, vizinhos):
    global dicPosicoesCalculadas

    for vizinho in vizinhos:
        heuristica = distanciaManhattan(vizinho, final)
        try:
            custo = dicPosicoesCalculadas[pai][1] + 1  # Custo = Custo do Pai + 1
        except:
            custo = 1  # No caso do Pai ser o Ponto Inicial

        dicPosicoesCalculadas[vizinho] = (vizinho, custo, heuristica, pai)

    return dicPosicoesCalculadas


def criaMapa():
    matriz = []

    arquivo = open(str(sys.argv[1]), 'r')
    linha = arquivo.readline().strip().split()

    while (linha != []):
        matriz.append(linha)
        linha = arquivo.readline().strip().split()

    # TODO: Converter elementos em inteiros
    quantidade_linhas = len(matriz)

    for i in range(quantidade_linhas):
        for j in range(len(matriz[i])):
            elemento = matriz[i][j]
            matriz[i][j] = int(elemento)

    return matriz

# Heuristica escolhida, distância em linha reta. h(x)
def distanciaManhattan(atual, final):
    return abs((final[0] - atual[0])) + abs((final[1] - atual[1]))

def buscar():
    listaAberta.append(inicio)
    achou = False

    while listaAberta != [] and not achou:        
        # Primeiro elemento da lista já ordenada
        atual = listaAberta[0]

        # Pesquisa pelos elementos vizinhos elegiveis (nao é barreira) e não presentes na lista fechada
        vizinhos = encontra_vizinhos(atual)
        
        calcula_custos(atual, vizinhos)  # Calculo de custo de cada vizinho

        # Verificando de um vizinho do atual ja nao esta presente na lista aberta
        for vizinho in vizinhos:
            if (vizinho not in listaAberta):
                listaAberta.append(vizinho)            
        
        # Remocao do primeiro elemento da lista aberta
        listaAberta.remove(atual)
        
        # Adicionando o elemento processado na lista fechada
        listaFechada.append(atual)  

        if(final in listaFechada): # Achou o objetivo se o vizinho for coordenada final
            achou = True
            caminho = recuperar_caminho(atual) # Lista com as posicoes percorridas até o destino
                        
            resultado = desenhar(caminho)

        # Ordenação dos elementos em ordem de custo crescente
        ordena_pelo_custo() 
    
    return resultado


def entrada_de_dados():
    global inicio
    global final

    print("Exemplo de entrada (x,y): = '0 0'\n")

    # Loop para pegar 2 valores (x,y)
    i = 0
    while  i < 2:
        if i == 0:
            mensagem = 'inicial'
        else:
            mensagem = 'final'

        entrada = input("Entre com o ponto %s do trajeto: " % mensagem)
        argumentos = tuple(entrada.split())
        linha = int(argumentos[0])
        coluna = int(argumentos[1])

        # Verifica se o ponto escolhido como inicio ou final é um obstaculo
        if mapa[linha][coluna] == 1:
            print('\nVocê escolheu um obstaculo como ponto %s, escolha novamente\n' % mensagem)
            i -= 1
        else:
            if i == 0:
                inicio = (linha, coluna)
            if i == 1:
                final = (linha, coluna)

        i += 1


def main():
    entrada_de_dados()

    if(inicio == final):
        print("Você já chegou na sua meta.\nJá pode dobrá-la! ")
    else:
        resultado = buscar()

        for i in resultado:
            for j in i:
                print(j, end=" ")
            print()
        print()

    return 0

# Estutura de Dados de uma Célula na Matriz

# (a,b,c,d)
# a = Coordenada na Matriz
# b = Custo de Deslocamento do inicio até a Coordenada atual
# c = Distancia de Manhattan da Coordenada atual até o objetivo
# d = Coordenadas do ponto pai

mapa = []
mapa = criaMapa()       # Cria matriz com o mapa passado em .txt

inicio = ()  # Coordenada inicio definido pelo professor
final = ()   # Coordenada final definido pelo professor

#inicio = (8,8)  # Testando outros valores
#final= (2,1)    # Testando outros valores

dicPosicoesCalculadas = {}    # Dicionario de posições que tiveram seus pesos calculados
                                #   {(coordenada) : ((coordenada),custo,heuristica,(posOrigem)), ...}

if __name__ == "__main__":
    main()

    