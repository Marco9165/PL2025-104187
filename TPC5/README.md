# TPC5 - Vending Machine

- **Data**: 18/03/2025
- **Nome** : Marco António Fernandes Brito
- **Numero** : a104187

 ![104187](/img/104187.png)

## 📌 Descrição
O TPC5 consiste em desenvolver um programa python  que simula uma máquina de vendas interativa. Os utilizadores podem listar os produtos disponíveis, inserir moedas, selecionar produtos e sair, recebendo o troco adequado.

## 📌 Funcionalidades e Comandos 

- ```LISTAR```→ Lista os produtos disponíveis na máquina.

- ```MOEDA <valor>``` → Insere moedas na máquina. Exemplo: MOEDA 1E, 50C, etc

- ```SELECIONAR <código> ```→ Seleciona um produto pelo código. Exemplo: SELECIONAR A23

- ```SAIR``` → Finaliza a operação e devolve o troco.


## 📌 Estrutura do Arquivo JSON (stock.json)

Os produtos disponíveis são armazenados no arquivo stock.json, no seguinte formato:
```
{
  "stock": [
    {
      "cod": "A23",
      "nome": "Água 0.5L",
      "quant": 8,
      "preco": 0.7
    },
    {
      "cod": "B12",
      "nome": "Refrigerante Cola 0.33L",
      "quant": 10,
      "preco": 1.2
    }
  ]
}
``` 

## 📌 Exemplo de Uso
``` 
>> LISTAR
cod | nome | quantidade | preço
----------------------------------------
A23 Água 0.5L 8 0.7€
B12 Refrigerante Cola 0.33L 10 1.2€

>> MOEDA 1E 50C
maq: Saldo = 150c

>> SELECIONAR A23
maq: Pode retirar Água 0.5L
maq: Saldo = 80c

>> SAIR
maq: Troco = 80c. Até à próxima!
```

## 📌 Como compilar 

1. Instalar biblioteca PLY ```pip install ply```.

2. Execute ```python main.py``` no caminho correto.

