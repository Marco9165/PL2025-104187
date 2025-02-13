def contador_on_off(text):
    soma_total= 0
    soma_ativa= True
    num_atual=""
    i =0

    while i<len(text):
        char=text[i]

        if char.isdigit():
            num_atual += char
        
        else:
            if num_atual:
                if soma_ativa:
                    soma_total += int(num_atual)
                num_atual = ""  

            if text[i] == "=":
                print(soma_total)
        
        if text[i:i+3].lower()=="off":
            soma_ativa=False
            i +=2

        elif text[i:i+2].lower()=="on":
            soma_ativa=True
            i +=1

        elif char == "-":
            if i + 1 < len(text) and text[i + 1].isdigit():
                num_atual = "-"  

        i += 1
    
    if num_atual and num_atual not in ["-"] and soma_ativa:
        soma_total += int(num_atual)

    print(soma_total)

# hfy3hud=jdon52=hdoff3jon-2=f

text= input("Escreva frase pretendida: ")
contador_on_off(text)
                
