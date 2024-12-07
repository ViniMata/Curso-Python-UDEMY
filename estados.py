class Camera:
    def __init__(self, nome, filmando = False):
       self.nome = nome
       self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando...")
        else:
            print(f"{self.nome} está filmando...")
            self.filmando = True
        
    def fotografar(self):
        if self.filmando:
          print("Ja esta filmando nao pode fotografar") 
        else:
            print("tirou foto") 

    def pararfilmar(self):
        if self.filmando:
            print(f"{self.nome} está parando de filmar...")
            self.filmando = False
        else:
            print(f"{self.nome} nao está filmando...")
c1 = Camera("Canon")
c2 = Camera("Sony")
c1.filmar()
c1.pararfilmar()
c1.fotografar()
