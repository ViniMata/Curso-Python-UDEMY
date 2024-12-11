class Livro:
    def __init__(self,titulo,autor,ano_de_publicacao, emprestado = False):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.emprestado = emprestado
    def dados_livro(self):
        print(f"Titulo: {self.titulo}.\nAutor: {self.autor}.\nAno de publicação: {self.ano_de_publicacao}.")
    def estado_livro(self):
        self.emprestado = not(self.emprestado)
class Usuario:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.lista_livros_usu = []

    def pegar_emprestado(self, livro):
        if livro.emprestado == False:
            livro.estado_livro()
            self.lista_livros_usu.append(livro)
        else:
            print (f"Esse livro não está disponível")
    def devolver(self, livro):
        if livro.emprestado == True:
            livro.estado_livro()
            self.lista_livros_usu.remove(livro)
        elif livro not in self.lista_livros_usu and livro.emprestado:
            print(f"Você não possui esse livro: {livro.titulo}")
        else:
            print (f"Esse livro não pode ser devolvido pois ele está disponivel aqui em nossa biblioteca.")
    def ver_lista(self):
        i = 0
        for livro in self.lista_livros_usu:
            i += 1
            print(f"{i}. {livro.titulo}.")


Harry_Potter = Livro("Harry Potter","J. K. Rowling", 1997)
# Harry_Potter.dados_livro()
livro_1984 = Livro("1984","George Orwell",1949)
# livro_1984.dados_livro()


vinicius = Usuario("Vinícius", 18)
joao = Usuario("Joao", 19)
vinicius.pegar_emprestado(Harry_Potter)
vinicius.devolver(livro_1984)
vinicius.ver_lista()
joao.pegar_emprestado(Harry_Potter)