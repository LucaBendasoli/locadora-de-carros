"""
TODO: registrar tudo em arquivo
TODO: adicionar funcao para remover carro do registro
TODO: adicionar funcao para editar carro do registro
"""

# Projeto Locadora de Carros
# Autor: Luca Bendasoli

from utils import (
    montar_portifolio,
    escolher_carro_para_alugar,
    escolher_carro_para_devolver,
    escolha_invalida,
    limpar_terminal,
    cadastrar_um_carro
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
| 0 - Mostrar Porifólio |     1 - Alugar um carro     | 3 - Cadastrar um novo carro |
0=======================0=============================O=============================0
| 4 - Devolver um carro | 5 - Mostrar carros alugados |     Em desenvolvimento      |\n
""")
    escolha = input()
    try:
        if int(escolha) == 0:
            montar_portifolio("carros_disponiveis", main_func=True)
        elif int(escolha) == 1:
            alugar_um_carro()
        elif int(escolha) == 2:
            devolver_um_carro()
        elif int(escolha) == 3:
            montar_portifolio("carros_alugados", main_func=True)
        elif int(escolha) == 4:
            cadastrar_um_carro()
        else:
            escolha_invalida()
    except:
        escolha_invalida()



if __name__ == '__main__':
    while True:
        main()
