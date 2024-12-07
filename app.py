class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.combustivel = 0

    def acelerar(self):
        if self.combustivel == 0:
            print("Sem gasolina")
        else: 
            self.velocidade += 10
            self.combustivel -= 5
    def frear (self):
        self.velocidade = max(0, self.velocidade - 10)

    def abastecer (self):
        if self.combustivel == 20:
            print("Combustivel maximo")
        else:
            self.combustivel += 10

    def mostrar_info (self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nVelocidade: {self.velocidade}\nCombustivel: {self.combustivel} ")

meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.abastecer()
meu_carro.abastecer()
meu_carro.acelerar()
meu_carro.mostrar_info()
