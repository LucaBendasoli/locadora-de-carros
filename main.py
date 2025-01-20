"""Projeto Locadora de Carros"""
# Autor: Luca Bendasoli

from utils import limpar_terminal, escolha_invalida, escolhe_carro_para_alugar, carros_disponiveis

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
    """Percorre um dicionário do portifolio e imprime os carros disponíveis
    
    Args:
        main_func (bool, optional): Se a função está
        sendo chamada pelo menu principal. Padrão é False."""
    limpar_terminal()
    for indice, (carro, valor) in enumerate(carros_disponiveis.items()):
        print(f"[{indice}] {carro} - {valor}")
    if main_func:
        input("Pressione enter para voltar")
        limpar_terminal()

def alugar_um_carro() -> None:
    """Aluga um carro para o usuário e remove o carro
    do portifólio e adicona aos carros alugados."""
    limpar_terminal()
    mostrar_portifolio()
    print("Escolha o código do carro")
    escolhe_carro_para_alugar()

def devolver_um_carro() -> None:
    """Devolve um carro para o portifólio de carros 
    disponíveis e remove dos carros alugados."""
    limpar_terminal()
    print("Carro devolvido")
    input("Pressione enter para voltar")
    limpar_terminal()

if __name__ == '__main__':
    while True:
        inicio()
        escolhe_opcao()
