# Algoritmo A* (A estrela)  

Trabalho construído para a Disciplina de Inteligência Artificial

Alunos: [Maria Luiza](https://github.com/malufreitas) e [Tarcísio Bruni](https://github.com/tarcisiobruni)

## Explicação Teórica

O **Algoritmo A*** (lemos A-Estrela), se trata de um algoritmo cuja finalidade é de busca entre vértices para grafos baseado em heurísticas.
O objetivo em cada resolução de problema está em definir a heurística que retorna o menor custo de deslocamento de um ponto de origem A até o destino B.

A fórmula base para computação desse custo é dada por:
f(x) = g(x) + h(x), onde:
- g(x): Representa uma função de custo sobre uma posição de inicio até a posição atual
- h(x): Representa a heurística proposta para estimativa até a posição de destino
>  Quanto menor for o custo da heurística, mais próxima da distância real ela representará.

## Problema Proposto

![Imagem](https://github.com/malufreitas/a-estrela/blob/master/Imagens/Exemplo%20A_star.png)

O problema proposto para o trabalho tem como objetivo geral encontrar um caminho de um ponto A até um ponto B, utilizando uma implementação do Algoritmo **A Estrela**, baseado na definição de uma heurística. Como parte também dos objetivos específicos, espera-se que sejam definidos:
- Um arquivo de entrada nas especificações (definidas pelo professor) e que tal arquivo seja incorporado ao programa para o devido processamento;
- Uma função para a heurística ;
- Implementação do Algoritmo A Estrela
- Definição de um caminho, com base na heurística e função de custo
- Impressão interativa do caminho realizado pelo objeto do ponto inicial ao ponto final
  
 

## Implementação

  

### Trechos mais importantes da implementação

  

## Resultados
  

### Referências

- [Explicação do Algoritmo A Estrela](https://www.youtube.com/watch?v=o5_mqZKhTvw&t=674s)
- [A* Pathfinding para Iniciantes](http://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/trabalhos/t1/A%20%20%20Pathfinding%20para%20Iniciantes.pdf)
- [Algoritmo A Estrela](http://maratonapuc.wikidot.com/apostilas:a-star)
