"""
TODO: adicionar funcao para cadastrar carro e registro de tudo em arquivo
TODO: adicionar funcao para remover carro do registro
TODO: adicionar funcao para editar carro do registro
"""

# Projeto Locadora de Carros
# Autor: Luca Bendasoli

from utils import (
    monta_portifolio,
    escolhe_carro_para_alugar,
    escolhe_carro_para_devolver,
    escolha_invalida,
    limpar_terminal
)

def main() -> None:
    """Função principal do programa.
    Mostra o menu principal e chama as funções de acordo com a escolha do usuário.
    
    Options:
    | 0 - Mostrar Porifólio | 1 - Alugar um carro         |
    0=======================0=============================0
    | 2 - Devolver um carro | 3 - Mostrar carros alugados |
    """
    print("""
Bem vindo a Locadora de Carros!

O que deseja fazer?
| 0 - Mostrar Porifólio | 1 - Alugar um carro         |
0=======================0=============================O
| 2 - Devolver um carro | 3 - Mostrar carros alugados |\n
""")
    escolha = input()
    try:
        if int(escolha) == 0:
            monta_portifolio("carros_disponiveis", main_func=True)
        elif int(escolha) == 1:
            alugar_um_carro()
        elif int(escolha) == 2:
            devolver_um_carro()
        elif int(escolha) == 3:
            monta_portifolio("carros_alugados", main_func=True)
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
        main()
