# TPC6 - Recursivo Descendente para expressões aritméticas

- **Data**: 22/03/2025
- **Nome** : Marco António Fernandes Brito
- **Numero** : a104187

 ![104187](/img/104187.png)

## 📌 Descrição
O TPC6 consiste em desenvolver um programa python  que utiliza um analisador léxico (com ply.lex) para tokenizar a entrada, um analisador sintático recursivo para construir uma árvore de sintaxe abstrata (AST) e uma avaliação semântica para calcular o resultado da expressão. Suporta operações básicas como adição, subtração, multiplicação e divisão, além de parênteses para controle de precedência.

## 📌 Funcionalidades 

- Suporte às operações: +, -, *, /
- Uso de parênteses para agrupar expressões
- Entrada de números inteiros
- Detecção de erros em expressões inválidas


## 📌 Exemplo de Uso
``` 
Escreva uma expressão: 2+4
2+4 = 6

Escreva uma expressão: 6*3
6*3 = 18

Escreva uma expressão: 6*(3+2*5)
6*(3+2*5) = 78

Escreva uma expressão: 5+4*13
5+4*13 = 57

```

## 📌 Como compilar 

1. Instalar biblioteca PLY ```pip install ply```.

2. Execute ```python main.py``` no caminho correto.

