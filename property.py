class Caneta:
    def __init__(self, cor):
        #private protected
        self._cor = cor

    def get_cor(self):
        return self.cor
    
    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor



caneta = Caneta("Azul")
caneta.cor = "verde"
print(caneta.cor)
