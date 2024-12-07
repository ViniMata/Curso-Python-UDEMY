class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Vinicius","Matareli")
# p1.nome = "Vinicius"
# p1.sobrenome = "Matareli"

print(p1.nome)
print(p1.sobrenome)