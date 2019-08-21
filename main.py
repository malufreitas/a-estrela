# Estutura de Dados de uma Célula
# (a,b,c,d)
# a = coordenada na matriz
# b = Custo de Deslocamento até o atual (1)
# c = Distancia de Manhattan até o destino
# d = coordenadas do ponto pai

mapa = criaMapa()       # Cria matriz com o mapa passado em txt
for i in mapa:
    print(i)

inicio = (0, 0)      # Inicio definido pelo professor
final = (9, 8)       # Final definido pelo professor

custo = 1            # g(x)
listaAberta = []    # Lista de posições com as coordenadas que não tiveram seus vizinhos verificados
listaFechada = []   # Lista de posições com as coordenadas que tiveram seus vizinhos verificados

# Lista de posições que tiveram seus pesos calculados [((coordenada),1,17,(posOrigem)),...]
listaPosicoesCalculadas = []

def encontra_vizinhos(atual):
    '''
        vizinhos = 
        # Vizinhos (linha , coluna)
        (atual[0]-1) , (atual[1])   # Em cima
        (atual[0]+1) , (atual[1])   # Em baixo
        (atual[0]) , (atual[1]-1)   # Esquerda
        (atual[0]) , (atual[1]+1)   # Direita
    '''
    return []

def ordena_pelo_custo():
    sorted(listaAberta, key=lambda t: (t[1]+t[2]))

def calcula_custos(vizinho):
    pass

def criaMapa():
    matriz = []

    arquivo = open('mapa.txt', 'r')
    linha = arquivo.readline().strip().split()

    while (linha != []):
        matriz.append(linha)
        linha = arquivo.readline().strip().split()

    return matriz

# Heuristica escolhida, distância em linha reta. h(x)
def distanciaManhattan(atual, final):
    return (final[0] - atual[0]) + (final[1] - atual[1])

# Algoritmo A* : f(x) = g(x) + h(x)
def main():
    listaAberta.append(inicio)

    while listaAberta != []:
        # primeiro elemento da lista já ordenada
        atual = listaAberta[0]
        
        # Pesquisa pelos elementos vizinhos elegiveis (nao é barreira) e not in ListaFechada
        vizinhos = encontra_vizinhos(atual)
        
        listaAberta.extend(vizinhos)  # Adição desses elementos à lista
        calcula_custos(vizinhos)  # Calculo de custo de cada vizinho
        
        # Remocao do primeiro elemento da lista aberta
        listaAberta.remove(atual)
        
        # Adicionando o elemento processado na lista fechada
        listaFechada.append(atual)
        
        # Ordenação dos elementos em ordem de custo crescente
        ordena_pelo_custo()       
    return 0

if __name__ == "__main__":
    main()
