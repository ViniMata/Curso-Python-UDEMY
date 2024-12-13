class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self._peso = peso  # Atributo privado

    @property
    def peso(self):
        # Getter: acessa o peso
        return self._peso

    @peso.setter
    def peso(self, novo_peso):
        # Setter: valida o peso antes de atribuir
        if novo_peso <= 0:
            raise ValueError("Peso deve ser maior que zero.")
        self._peso = novo_peso


# Teste
p1 = Pessoa("Carlos", 35, 75)
print(f"Peso inicial de {p1.nome}: {p1.peso} kg")

# Alterando o peso
p1.peso = 80
print(f"Novo peso de {p1.nome}: {p1.peso} kg")

# Tentativa de atribuir um peso inválido
try:
    p1.peso = -5
except ValueError as e:
    print(f"Erro ao alterar peso: {e}")

