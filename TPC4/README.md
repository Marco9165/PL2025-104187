# TPC4 - Analisador Léxico

- **Data**: 05/03/2025
- **Nome** : Marco António Fernandes Brito
- **Numero** : a104187

 ![104187](/img/104187.png)

## 📌 Descrição
O TPC4 consiste em desenvolver um programa python em que servirá como um analisador léxico para uma linguagem de consulta, utilizando a biblioteca PLY.

## 📌 Funcionalidades

- Identificação de Tokens → Reconhece palavras-chave, variáveis, strings, números e símbolos.
- Análise Automática → Usa expressões regulares para processar a entrada.
- Tratamento de Erros → Detecta e ignora caracteres inválidos.
- Conversão de Números → Transforma valores numéricos em inteiros.
- Saída Estruturada → Exibe os tokens reconhecidos com tipo e valor.


## 📌 Input e output

A consulta de teste usada no código é:

```
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```
Após executar o lexer, a saída será uma lista de tokens reconhecidos, como:

```
LexToken(SELECT,'select',1,0)
LexToken(VAR,'?nome',1,7)
LexToken(VAR,'?desc',1,13)
LexToken(WHERE,'where',1,19)
LexToken(LBRACE,'{',1,25)
LexToken(VAR,'?s',2,27)
LexToken(A,'a',2,30)
LexToken(PREFIX,'dbo',2,32)
LexToken(COLON,':',2,35)
LexToken(IRI,'MusicalArtist',2,36)
LexToken(DOT,'.',2,49)
...
LexToken(NUMBER,1000,7,123)
```



## 📌 Como compilar 

1. Instalar biblioteca PLY ```pip install ply```.

2. Execute ```python main.py``` no caminho correto.

