# Projeto Locadora de Carros
from utils import *

def inicio():
    print("Bem vindo a Locadora de Carros!")
    print("O que deseja fazer?")
    print("0 - Mostrar Porifólio | 1 - Alugar um carro | 2 - Devolver um carro" )

def escolhe_opcao() -> None:
    escolha = input()
    try:
        if int(escolha) == 0:
            mostrar_portifolio(True)
        elif int(escolha) == 1:
            alugar_um_carro()
        elif int(escolha) == 2:
            devolver_um_carro()
        else:
            escolha_invalida()  
    except:
        escolha_invalida()
        
def mostrar_portifolio(main_func: bool = False) -> None:
    limpar_terminal()
    for indice, (carro, valor) in enumerate(carros_disponiveis.items()):
        print(f"[{indice}] {carro} - {valor}")
    if main_func:
        input("Pressione enter para voltar")
        limpar_terminal()
        
def alugar_um_carro() -> None:
    limpar_terminal()
    mostrar_portifolio()
    print("Escolha o código do carro")
    escolhe_carro()
    
def devolver_um_carro() -> None:
    limpar_terminal()
    print("Carro devolvido")
    input("Pressione enter para voltar")
    limpar_terminal()
    
if __name__ == '__main__':
    while True:
        inicio()
        escolhe_opcao()