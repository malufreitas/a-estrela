# Algoritmo A* (A estrela)  

Trabalho desenvolvido para a Disciplina de Inteligência Artificial

Alunos: [Maria Luiza](https://github.com/malufreitas) e [Tarcísio Bruni](https://github.com/tarcisiobruni)

## Explicação Teórica

O **Algoritmo A*** (lemos A-Estrela), se trata de um algoritmo cuja finalidade é de busca entre vértices para grafos, baseado em funções heurísticas. O uso deste algoritmo representa a técnica de busca mais utlizada.
O objetivo em cada resolução de problema está na definição da função heurística que retorne um menor custo de deslocamento de um ponto de origem A até o destino B.

A fórmula de custo tem uma combinação total e é dada por:
f(x) = g(x) + h(x), onde:
- g(x): Representa uma função de custo sobre uma posição de inicio até a posição atual
- h(x): Representa a função heurística proposta para estimativa até a posição de destino

## Problema Proposto

<p align="center">
  <img src="https://github.com/malufreitas/a-estrela/blob/master/Imagens/Exemplo%20A_star.png">
</p>

O problema proposto para o trabalho tem como objetivo geral encontrar um caminho de um ponto A até um ponto B, utilizando uma implementação do Algoritmo **A Estrela**, usando a definição de heurística para traçar o melhor caminho. Como parte também dos objetivos específicos, espera-se que sejam definidos:
- Um arquivo de entrada nas especificações (definidas pelo professor) e que tal arquivo seja incorporado ao programa para o devido processamento;
- Uma heurística para composição da fórmula de custo;
- Implementação do Algoritmo A Estrela
- Definição de um caminho, com base na heurística e função de custo
- Impressão interativa do caminho realizado pelo objeto do ponto inicial ao ponto final. 
 

## Implementação

O algoritmo foi implementado utilizando a linguagem [Python](https://www.python.org/), devido a familiaridade da equipe com a sintaxe e por entender que essa provê os recursos necessários para a codificação. A implementação sugerida seguiu recomendações de duas referências (citadas abaixo).

O processmento se inicia com a leitura e incorporação do [arquivo de texto](https://github.com/malufreitas/a-estrela/blob/master/mapa.txt) definido para o problema e materializado em uma matriz, utilizando o conceito de lista de lista da linguagem.

Em seguida é realizado o processamento do algoritmo, onde já se tem pré-definidos os pontos iniciais e finais do percurso. Esse processo de busca é quebrado em outros pequenos cálculos, com as seguintes etapas:

    1- Inserção do elemento de origem dentro da lista de coordenadas a serem processadas
    2- Captura do primeito elemento da lista  e definição deste como o atual.
    3- Identificação dos elementos elegíveis à vizinhos para o ponto atual
    4- Inserção dos elementos vizinhos a essa mesma lista de coordenadas para computar
    5- Cálculo de custo dos elementos vizinhos, com base na definição da heurística
    6- Remoção desse elemento atual de pontos a calcular e, inserção em outra lista como já processado
    7- Ordenação dos pontos remanescentes na lista na ordem crescente de custo
    8- Loop ao tópico 2, enquanto a coordenada de destino não for processada e se todos os pontos ja foram processados. 
  
**Funções de Custo**
Para a implementação deste algoritmo as funções g(x) e h(x) citadas na composição de cálculo final do algoritmo foram definidas da seguinte forma:
- g(x): Representa a função de custo e será usada como constante 1.
- h(x): Representa a heurística, na qual utilizamos a função heurística de Manhattan.

A *heurística de Manhattan* tem esse nome pois define a menor distânia entre quarteirões numa malha urbana reticulada ortogonal, como na pópria zona da Cidade de Manhattan.

<p align="center">
  <img src="">
</p>

**Definições das Variáveis:**
- mapa: Representa a matriz do arquivo de texto, formato como lista de lista.
- listaAberta: Guarda os elementos que ainda não tiveram seus vizinhos calculados.
- listaFechada: Guarda os elementos que já tiveram seus vizinhos calculados.
- dicPosicoesCalculadas: Dicionario de posições que tiveram seus pesos calculados na seguinte estrutura:
> **{(coordenada) : ((coordenada),custo,heuristica,(posOrigem)), ...}**

### Trechos mais importantes da implementação

**Identificação dos Elementos Elegíveis a vizinhos, citado no Tópico 3**

<p align="center">
  <img src="https://github.com/malufreitas/a-estrela/blob/master/Imagens/Encontra%20vizinhos.PNG">
</p>

**Cálculo de custo, citado no Tópico 5**

<p align="center">
  <img src="https://github.com/malufreitas/a-estrela/blob/master/Imagens/Calculo%20de%20custo.PNG">
</p>

**Função da Heurística de Manhattan, citado no Tópico 5**

<p align="center">
  <img src="https://github.com/malufreitas/a-estrela/blob/master/Imagens/Heuristica%20escolhida.PNG">
</p>

## Resultados

Exemplificação da execução do programa
<p align="center">
  <img src="https://github.com/malufreitas/a-estrela/blob/master/Imagens/Exemplo%20de%20execu%C3%A7%C3%A3o.PNG">
</p>


### Referências

- Aulas e Materiais de Aula
- [Explicação do Algoritmo A Estrela](https://www.youtube.com/watch?v=o5_mqZKhTvw&t=674s)
- [A* Pathfinding para Iniciantes](http://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/trabalhos/t1/A%20%20%20Pathfinding%20para%20Iniciantes.pdf)
- [Algoritmo A Estrela](http://maratonapuc.wikidot.com/apostilas:a-star)
