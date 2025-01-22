"""
TODO: registrar tudo em arquivo
TODO: adicionar funcao para editar carro do registro
"""

# Projeto Locadora de Carros
# Autor: Luca Bendasoli

from utils import (
    montar_portifolio,
    alugar_um_carro,
    devolver_um_carro,
    escolha_invalida,
    cadastrar_um_carro,
    remover_um_carro
)

def main() -> None:
    """Função principal do programa.
    Mostra o menu principal e chama as funções de acordo com a escolha do usuário.
    
    Options:
    |    0 - Mostrar Porifólio    |  1 - Alugar um carro  | 2 - Cadastrar um novo carro |
    0=============================0=======================O=============================0
    | 3 - Mostrar carros alugados | 4 - Devolver um carro |    5 - Remover um carro     |
    """
    print("""
Bem vindo a Locadora de Carros!

O que deseja fazer?
|    0 - Mostrar Porifólio    |  1 - Alugar um carro  | 2 - Cadastrar um novo carro |
0=============================0=======================O=============================0
| 3 - Mostrar carros alugados | 4 - Devolver um carro |    5 - Remover um carro     |\n
""")
    escolha = input()
    try:
        if int(escolha) == 0:
            montar_portifolio("carros_disponiveis", main_func=True)
        elif int(escolha) == 1:
            alugar_um_carro()
        elif int(escolha) == 2:
            cadastrar_um_carro()
        elif int(escolha) == 3:
            montar_portifolio("carros_alugados", main_func=True)
        elif int(escolha) == 4:
            devolver_um_carro()
        elif int(escolha) == 5:
            remover_um_carro()
        else:
            escolha_invalida()
    except:
        escolha_invalida()

if __name__ == '__main__':
    while True:
        main()
