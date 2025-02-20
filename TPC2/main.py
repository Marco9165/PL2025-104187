def read_file(file):
    """Lê o arquivo CSV e retorna uma lista de dicionários, onde cada dicionário representa uma obra."""
    obras = []
    linha_temporaria = ""
    dentro_de_aspas = False

    with open(file, "r", encoding="utf-8") as f:
        cabecalho = f.readline().strip().split(';')

        for linha in f:
            linha = linha.strip()

            if dentro_de_aspas:
                linha_temporaria += " " + linha
                if linha.count('"') % 2 != 0:   
                    dentro_de_aspas = False
                    obras.append(read_line(linha_temporaria, cabecalho))
                    linha_temporaria = ""
                continue

            if linha.count('"') % 2 != 0:
                dentro_de_aspas = True
                linha_temporaria = linha
                continue

            if linha:
                obras.append(read_line(linha, cabecalho))

    return obras


def read_line(linha, cabecalho):
    """Processa uma linha do CSV, garantindo que os campos entre aspas sejam lidos corretamente."""
    campos = []
    campo_atual = ""
    dentro_de_aspas = False

    for char in linha:
        if char == '"':  
            dentro_de_aspas = not dentro_de_aspas
        elif char == ";" and not dentro_de_aspas:  
            campos.append(campo_atual.strip())
            campo_atual = ""
        else:
            campo_atual += char  

    campos.append(campo_atual.strip())  
    return {cabecalho[i]: campos[i] for i in range(len(cabecalho))}


def compositores_ordenados(obras):
    """Retorna uma lista ordenada alfabeticamente de compositores únicos."""
    return sorted({obra['compositor'] for obra in obras})


def contagem_musicasPeriodo(obras):
    """Retorna um dicionário com a contagem de quantas obras pertencem a cada período musical."""
    distribuicao = {}
    for obra in obras:
        periodo = obra['periodo']
        distribuicao[periodo] = distribuicao.get(periodo, 0) + 1
    return distribuicao


def titulos_por_periodo(obras):
    """Retorna um dicionário com períodos como chave e listas de títulos ordenadas como valores."""
    periodos = {}
    for obra in obras:
        periodo = obra['periodo']
        titulo = obra['nome']
        if periodo not in periodos:
            periodos[periodo] = []
        periodos[periodo].append(titulo)

    for periodo in periodos:
        periodos[periodo].sort()

    return periodos


def main():
    file = 'obras.csv'
    obras = read_file(file)

    print("1 - Lista ordenada alfabeticamente dos compositores musicais;")
    print("2 - Distribuição das obras por período: quantas obras catalogadas em cada período;")
    print("3 - Dicionário em que a cada período está associada uma lista alfabética dos títulos das obras desse período.")
    
    opcao = input("\nEscolha uma opção (1/2/3): ").strip()

    if opcao == "1":
        print("\nCompositores ordenados:\n")
        for compositor in compositores_ordenados(obras):
            print(compositor)
            
    elif opcao == "2":
        print("\nDistribuição de obras por período:\n")
        for periodo, quantidade in contagem_musicasPeriodo(obras).items():
            print(f"{periodo}: {quantidade} obras")
            
    elif opcao == "3":
        print("\nTítulos das obras organizados por período:\n")
        for periodo, titulos in titulos_por_periodo(obras).items():
            print(f"\n{periodo}:")
            for titulo in titulos:
                print(f"  - {titulo}")

    else:
        print("Opção inválida. Escolha entre 1, 2 ou 3.")

if __name__ == "__main__":
    main()
