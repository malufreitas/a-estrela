def criaMapa():
    matriz = []

    arquivo = open('mapa.txt', 'r')
    linha = arquivo.readline().strip().split()

    while (linha != []):
        matriz.append(linha)
        linha = arquivo.readline().strip().split()

    return matriz


def distanciaManhattan(atual, final):   # Heuristica escolhida, distância em linha reta. h(x)
    return (final[0] - atual[0]) + (final[1] - atual[1])


# Algoritmo A* : f(x) = g(x) + h(x)
def main():
    mapa = criaMapa()       # Cria matriz com o mapa passado em txt
    for i in mapa:
        print(i)

    inicio = (0,0)      # Inicio definido pelo professor
    final = (9,8)       # Final definido pelo professor

    custo = 1            # g(x)
    listaAberta = []    # Lista de posições que não tiveram seus vizinhos verificados
    listaFechada = []   # Lista de posições que tiveram seus vizinhos verificados
    dic = {}            # Dicionario de posições que tiveram seus pesos calculados {(0,0): [1,17]}

    atual = inicio      # Começa no inicio
    listaAberta.append(atual)     

    while listaAberta != []:
        #dic[atual] = (custo, distanciaManhattan(atual, final))

        '''
        vizinhos = 
        # Vizinhos (linha , coluna)
        (atual[0]-1) , (atual[1])   # Em cima
        (atual[0]+1) , (atual[1])   # Em baixo
        (atual[0]) , (atual[1]-1)   # Esquerda
        (atual[0]) , (atual[1]+1)   # Direita
        '''

    return 0


if __name__ == "__main__":
    main()