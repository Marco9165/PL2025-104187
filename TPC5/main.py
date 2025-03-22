import json
import os
import ply.lex as lex


COINS = {"2E":200,"1E": 100, "50C": 50, "20C": 20, "10C": 10, "5C": 5, "2C": 2, "1C": 1}

tokens = (
    'LISTAR', 'MOEDA', 'SELECIONAR',
    'SAIR', 'CODIGO', 'VALOR')

t_ignore = " \t"

def t_LISTAR(t):
     r'LISTAR'; 
     return t

def t_MOEDA(t):
     r'MOEDA'; 
     return t

def t_SELECIONAR(t):
     r'SELECIONAR'; 
     return t

def t_SAIR(t):
     r'SAIR'; 
     return t

def t_CODIGO(t):
     r'[A-Z]\d{2}'; 
     return t

def t_VALOR(t):
     r'\d+[EC]'; t.value = t.value.upper(); 
     return t

def t_error(t): t.lexer.skip(1)

lexer = lex.lex()

def load_stock():
    if os.path.exists("stock.json"):
        with open("stock.json", "r") as f:
            data = json.load(f)
        return data.get("stock", [])
    return []

def save_stock(stock):
    with open("stock.json", "w") as f:
        json.dump({"stock": stock}, f, indent=2)

def listar(stock):
    print("cod | nome | quantidade | preço\n" + "-" * 40)
    for p in stock:
        print(f"{p['cod']} {p['nome']} {p['quant']} {p['preco']}€")

def inserir_moedas(saldo, valores):
    return saldo + sum(COINS[v] for v in valores if v in COINS)

def selecionar(stock, saldo, codigo):
    for p in stock:
        if p["cod"] == codigo:
            if p["quant"] > 0 and saldo >= int(p["preco"] * 100):
                p["quant"] -= 1
                return saldo - int(p["preco"] * 100), f"maq: Pode retirar {p['nome']}"
            return saldo, "maq: Saldo insuficiente ou produto esgotado."
    return saldo, "maq: Produto inexistente."

def main():
    stock, saldo = load_stock(), 0
    print("maq: Stock carregado, Estado atualizado.\nmaq: Disponível para pedidos.")
    while True:
        lexer.input(input(">> ").strip().upper())
        tokens_list = list(lexer)
        if not tokens_list:
            print("maq: Comando inválido.")
            continue
        cmd = tokens_list[0].type
        if cmd == "LISTAR":
            listar(stock)
        elif cmd == "MOEDA":
            saldo = inserir_moedas(saldo, [t.value for t in tokens_list[1:]])
        elif cmd == "SELECIONAR" and len(tokens_list) > 1:
            saldo, msg = selecionar(stock, saldo, tokens_list[1].value)
            print(msg)
        elif cmd == "SAIR":
            print(f"maq: Troco = {saldo}c. Até à próxima!")
            save_stock({"stock": stock})
            break
        print(f"maq: Saldo = {saldo}c")

if __name__ == "__main__":
    main()
