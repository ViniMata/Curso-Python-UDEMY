class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando') 

fusca = Carro("Fusca")
print(fusca.nome)
print(fusca.acelerar())

celta = Carro("Celta")
print(celta.nome)