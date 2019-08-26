# Estutura de Dados de uma Célula

# (a,b,c,d)
# a = coordenada na matriz
# b = Custo de Deslocamento até o atual (1)
# c = Distancia de Manhattan até o destino
# d = coordenadas do ponto pai

import time

listaAberta = []    # Lista de posições com as coordenadas que não tiveram seus vizinhos verificados
listaFechada = []   # Lista de posições com as coordenadas que tiveram seus vizinhos verificados

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

    for pos_vizinho in range(len(vizinhos)):
        heuristica = distanciaManhattan(vizinhos[pos_vizinho], final)
        custo = distanciaManhattan(vizinhos[pos_vizinho], inicio)

        dicPosicoesCalculadas[vizinhos[pos_vizinho]] = (vizinhos[pos_vizinho], heuristica, custo, pai)

    return dicPosicoesCalculadas


def criaMapa():
    matriz = []

    arquivo = open('mapa.txt', 'r')
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
        print("Lista aberta >> ",listaAberta)
        
        # primeiro elemento da lista já ordenada
        atual = listaAberta[0]
        print("Atual >> ",atual)

        # Pesquisa pelos elementos vizinhos elegiveis (nao é barreira) e not in ListaFechada
        vizinhos = encontra_vizinhos(atual)
        print("Vizinhos >> ",vizinhos)
        
        if(final in vizinhos):
            print("Encontrou!")
            achou = True
        
        calcula_custos(atual, vizinhos)  # Calculo de custo de cada vizinho

        for vizinho in vizinhos:
            if ((vizinho not in listaAberta) ):
                listaAberta.append(vizinho)
        
        # Remocao do primeiro elemento da lista aberta
        listaAberta.remove(atual)
        
        # Adicionando o elemento processado na lista fechada
        listaFechada.append(atual)  

        # Ordenação dos elementos em ordem de custo crescente
        ordena_pelo_custo() 
        print("Lista aberta >> ",listaAberta)
        
        print("Quantidade de Elementos Calculados >> ",len(dicPosicoesCalculadas.keys()))
    
    return 0

# Algoritmo A* : f(x) = g(x) + h(x)
def main():
    for i in mapa:
        print(i)

    buscar()
    return 0

mapa = []
mapa = criaMapa()       # Cria matriz com o mapa passado em txt

inicio = (0, 0)      # Inicio definido pelo professor
final = (9, 8)       # Final definido pelo professor

dicPosicoesCalculadas = {}    # Lista de posições que tiveram seus pesos calculados [((coordenada),1,17,(posOrigem)),...]

if __name__ == "__main__":
    main()

    