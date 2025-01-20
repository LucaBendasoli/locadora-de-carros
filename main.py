"""Projeto Locadora de Carros"""
# Autor: Luca Bendasoli

from utils import (
    monta_portifolio,
    escolhe_carro_para_alugar,
    escolhe_carro_para_devolver,
    escolha_invalida,
    limpar_terminal
)

def inicio():
    """Essa função chama a tela inicial do programa"""
    print("Bem vindo a Locadora de Carros!")
    print("O que deseja fazer?")
    print("0 - Mostrar Porifólio | 1 - Alugar um carro | 2 - Devolver um carro" )

def escolhe_opcao() -> None:
    """Pede que o usuário escolha uma opção e chama a função correspondente"""
    escolha = input()
    try:
        if int(escolha) == 0:
            monta_portifolio("carros_disponiveis", main_func=True)
        elif int(escolha) == 1:
            alugar_um_carro()
        elif int(escolha) == 2:
            devolver_um_carro()
        else:
            escolha_invalida()
    except:
        escolha_invalida()

def alugar_um_carro() -> None:
    """Aluga um carro para o usuário e remove o carro
    do portifólio e adicona aos carros alugados."""
    limpar_terminal()
    monta_portifolio("carros_disponiveis")
    escolhe_carro_para_alugar()

def devolver_um_carro() -> None:
    """Devolve um carro para o portifólio de carros 
    disponíveis e remove dos carros alugados."""
    limpar_terminal()
    monta_portifolio("carros_alugados")
    escolhe_carro_para_devolver()

if __name__ == '__main__':
    while True:
        inicio()
        escolhe_opcao()
