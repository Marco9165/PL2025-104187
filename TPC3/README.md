# TPC3 - Conversor de MarkDown para HTML

- **Data**: 27/02/2025
- **Nome** : Marco António Fernandes Brito
- **Numero** : a104187

 ![104187](/img/104187.png)

## 📌 Descrição
O TPC3 consiste em desenvolver um programa python em que será um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic
Syntax" da Cheat Sheet

## 📌 Funcionalidades
  Transformar:

  - Cabeçalhos (#, ##, ###) → <h{1,2,3}>texto<h{1,2,3}>
  - Negrito (texto → <b>texto</b>)
  - Itálico (texto → <i>texto</i>)
  - Listas numeradas (1. texto, 2.texto,3.texto)
  - Links (texto → <a href=URL>texto</a>)
  - Imagens (alt → <img src=URL alt=alt/>)



## 📌 Testar

Para testar as funcionalidades, foram utilizados os seguintes ficheiros:

  - ```input.md```: Arquivo Markdown.
  - ```fileOutput.html```: Arquivo HTML gerado após compilado programa de conversão

## 📌 Como compilar 

1. Altere, caso deseja, os exemplos do ```input.md``` para algo lhe possa agradar melhor.

2. Execute ```python main.py``` no caminho correto.

3. Observe o ```fileOutput.html``` que foi gerado após conversão.