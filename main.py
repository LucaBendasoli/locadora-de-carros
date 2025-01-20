# Projeto Locadora de Carros
import os

def inicio():
    print("Bem vindo a Locadora de Carros!")
    print("O que deseja fazer?")
    print("0 - Mostrar Porifólio | 1 - Alugar um carro | 2 - Devolver um carro" )

def escolhe_opcao() -> None:
    escolha = input()
    try:
        if int(escolha) == 0:
            mostrar_portifolio()
        elif int(escolha) == 1:
            alugar_um_carro()
        elif int(escolha) == 2:
            devolver_um_carro()
        else:
            limpar_terminal()
            print("Escolha inválida, tente novamente")    
    except:
        limpar_terminal()
        print("Escolha inválida, tente novamente")
    
def mostrar_portifolio() -> None:
    limpar_terminal()
    print(carros_disponiveis)
    input("Pressione enter para voltar")
    limpar_terminal()
    
def alugar_um_carro() -> None:
    limpar_terminal()
    print("Carro alugado")
    input("Pressione enter para voltar")
    limpar_terminal()
    
def devolver_um_carro() -> None:
    limpar_terminal()
    print("Carro devolvido")
    input("Pressione enter para voltar")
    limpar_terminal()

def limpar_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__ == '__main__':
    carros_disponiveis = {
        "Chevrolet Tracker" : "R$ 120/dia",
        "Chevrolet Onix" : "R$90/dia",
        "Chevrolet Spin" : "R$150/dia",
        "Hyundai HB20" : "R$85/dia",
        "Hyundai Tucson" : "R$120/dia",
        "Fiat Uno" : "R$60/dia",
        "Fiat Mobi" : "R$70/dia",
        "Fiat Pulse" : "R$130/dia"        
    }
    while True:
        inicio()
        escolhe_opcao()