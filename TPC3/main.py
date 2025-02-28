import re


def main (file):
    try:
        with open (file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return 'File not find'

    
    #cabeçalhos 
    patterns = [  
        (r'^# (.+)$', r'<h1>\1</h1>'),  
        (r'^## (.+)$', r'<h2>\1</h2>'),  
        (r'^### (.+)$', r'<h3>\1</h3>')  
    ]  

    for pattern, replacement in patterns:  
        text = re.sub(pattern, replacement, text, flags=re.M)  


    #negrito
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
    #itálico
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)

    #listas
    text = re.sub(r'(?m)^\d+\. (.+)$', r'<li>\1</li>', text)
    text = re.sub(r'(?:<li>.+?</li>\n?)+', lambda m: f'<ol>\n{m.group(0)}\n</ol>', text, flags=re.DOTALL)


    #Link 
    text =re.sub(r'(^|\s)\[(.*?)\]\((.*?)\)', r'\1 <a href="\3">\2</a>', text)


    #Imagens
    text =re.sub(r'(.*?)\!\[(.*?)\]\((.*?)\)', r'\1 <img scr="\3" alt="\2" />', text)

    
    output_file_name= 'fileOutput.html'

    try:
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
    except Exception as exp:
        print("Fail to open file:", exp)


main('input.md')

