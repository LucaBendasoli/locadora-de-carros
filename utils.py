import os

def escolha_invalida():
    limpar_terminal()
    print("Escolha inválida, tente novamente")
        

def limpar_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    