import json

from json_com_objeto import caminho_arquivo, Pessoa

with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)
    
    p1=Pessoa(**dados[0])
    p2=Pessoa(**dados[1])
    p3=Pessoa(**dados[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

    
