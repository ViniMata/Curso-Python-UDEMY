import json
caminho = "dados_banco.json"

class Conta:
    def __init__(self, nome,sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.saldo = 0

    def dados(self):
        print(f"Nome: {self.nome} {self.sobrenome}\nIdade: {self.idade}\nSaldo: {self.saldo}")
    
    def depositar(self, depositado):
        self.saldo += depositado

    def sacar(self, sacado):
        if sacado> self.saldo:
            print(f"Você está retirando um valor maior do que possui. Saldo: {self.saldo}")
        else:
            self.saldo -= sacado

def decisao():
    decisao_usu = int(input("Digite o que deseja fazer.\n1. Cadastrar nova conta.\n2.Visualizar os dados da sua conta.\n3.Depositar em sua conta.\n4.Sacar dinheiro de sua conta.\n"))
    return decisao_usu 

def processar_decisao(decisao_usu):
    match decisao_usu:
        case 1:           
            conta = iniciando_uma_conta()
        case 2:
            print("2")
        case 3:
            conta.dados()
        case 4:
            print("4")

def iniciando_uma_conta():
#criar uma lista para adicionar os dados e atribuir o valor em cada objeto
    lista_usuario = []
    nome = input("Qual seu nome?")
    lista_usuario.append(nome)
    sobrenome = input("Qual seu sobrenome?")
    lista_usuario.append(sobrenome)
    idade = int(input("Qual sua idade?"))
    lista_usuario.append(idade)
    print(lista_usuario)
    
    conta = Conta(*lista_usuario)
    return conta
def main():
    decisao_usu = decisao()
    processar_decisao(decisao_usu,)
    

def criar_conta(bd):
        with open(caminho, 'w') as arquivo:
            json.dump(bd, arquivo, ensure_ascii= False, indent = 2)

main()