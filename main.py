# Algoritmo A* : f(x) = g(x) + h(x)

# Codigo desenvolvido por Maria Luiza e Tarcisio Bruni

import time

listaAberta = []    # Lista com as coordenadas que não tiveram seus vizinhos verificados
listaFechada = []   # Lista com as coordenadas que tiveram seus vizinhos verificados

def desenhar(lista_coordenadas):
    #   TO DO:
    #       Implementar a funcao que exporta um aquivo de imagem com o percurso ate o destino

    print(f"### PERCURSO de {inicio} ate {final} ###")
    print(lista_coordenadas)

def recuperar_caminho(atual):
    global dicPosicoesCalculadas

    percurso = []
    if atual != inicio:
        pontoOrigem = dicPosicoesCalculadas[atual][3]
    else:
        pontoOrigem = inicio

    percurso.append(final)
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
        custo = distanciaManhattan(vizinho, inicio)

        dicPosicoesCalculadas[vizinho] = (vizinho, custo, heuristica, pai)

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
        # print("Lista aberta >> ",listaAberta)
        
        # Primeiro elemento da lista já ordenada
        atual = listaAberta[0]
        # print("Atual >> ",atual)

        # Pesquisa pelos elementos vizinhos elegiveis (nao é barreira) e não presentes na lista fechada
        vizinhos = encontra_vizinhos(atual)
        # print("Vizinhos >> ",vizinhos)
        
        if(final in vizinhos): # Achou o objetivo se o vizinho for coordenada final
            achou = True
            caminho = recuperar_caminho(atual) # Lista com as posicoes percorridas até o destino
            desenhar(caminho)
        else:
            calcula_custos(atual, vizinhos)  # Calculo de custo de cada vizinho

            for vizinho in vizinhos:# Verificando de um vizinho do atual ja nao esta presente na lista aberta
                if (vizinho not in listaAberta):
                    listaAberta.append(vizinho)
            
            # Remocao do primeiro elemento da lista aberta
            listaAberta.remove(atual)
            
            # Adicionando o elemento processado na lista fechada
            listaFechada.append(atual)  
            # print("Lista fechada >> ",listaFechada)

            # Ordenação dos elementos em ordem de custo crescente
            ordena_pelo_custo() 
    
    return 0


def main():
    if(inicio == final):
        print("Você já chegou na sua meta.\nJá pode dobrá-la! ")
    buscar()
    return 0

# Estutura de Dados de uma Célula na Matriz

# (a,b,c,d)
# a = Coordenada na Matriz
# b = Custo de Deslocamento do inicio até a Coordenada atual
# c = Distancia de Manhattan da Coordenada atual até o objetivo
# d = Coordenadas do ponto pai

mapa = []
mapa = criaMapa()       # Cria matriz com o mapa passado em .txt

inicio = (0, 0)      # Coordenada inicio definido pelo professor
final = (9, 0)       # Coordenada final definido pelo professor

dicPosicoesCalculadas = {}    # Dicionario de posições que tiveram seus pesos calculados
                                #   {(coordenada) : ((coordenada),custo,heuristica,(posOrigem)), ...}

if __name__ == "__main__":
    main()

    