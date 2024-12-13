class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("hey")
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


p1 = Pessoa('Joao', 34)
p2 = Pessoa.criar_com_50_anos("Daniel")
p3 = Pessoa("Anonima", 23)
print(p2.nome, p2.idade)
