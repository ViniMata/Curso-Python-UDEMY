import json

caminho_arquivo = 'json_com_objeto.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("joao", 22)
p2 = Pessoa("vitor", 51)
p3 = Pessoa("vinicius", 19)
bd = [vars(p1), vars(p2), vars(p3) ] 

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii = False, indent = 2)