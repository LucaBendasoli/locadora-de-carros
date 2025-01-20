"""Este arquivo contém funções e variáveis utilitárias para o programa principal"""

import os

carros_disponiveis = {
    "Chevrolet Tracker" : "R$ 120/dia",
    "Chevrolet Onix" : "R$ 90/dia",
    "Chevrolet Spin" : "R$ 150/dia",
    "Hyundai HB20" : "R$ 85/dia",
    "Hyundai Tucson" : "R$ 120/dia",
    "Fiat Uno" : "R$ 60/dia",
    "Fiat Mobi" : "R$ 70/dia",
    "Fiat Pulse" : "R$ 130/dia"        
}

def escolhe_carro() -> None:
    """Essa função permite que o usuário escolha um carro para alugar.
    A função irá validar a escolha do usuário e responder a sua solicitação."""
    escolha = input()
    try:
        escolha = int(escolha)
        if escolha < 0 or escolha >= len(carros_disponiveis):
            escolha_invalida()
        dias = int(input("Quantos dias você quer alugar este carro?\n"))
        chave = list(carros_disponiveis.keys())[escolha]
        valor_por_dia = list(carros_disponiveis.values())[escolha].split()[1]
        valor = int(valor_por_dia.split("/")[0])
        print(f"Você escolheu {chave} por {dias} dias.")
        print(f"O aluguel totalizaria R$ {valor * dias}.")
        print("Deseja alugar?")
        desistencia = input("0 - SIM | 1 - NÃO\n")
        if desistencia not in ['0', '1']:
            escolha_invalida()
            return
        if desistencia == '1':
            limpar_terminal()
            return
        carros_disponiveis.pop(chave, None)
        limpar_terminal()
        print(f"Parabéns você alugou o {chave} por {dias} dias.")
    except:
        escolha_invalida()

def escolha_invalida():
    """Essa função é chamada quando o usuário faz uma escolha inválida."""
    limpar_terminal()
    print("Escolha inválida, tente novamente")

def limpar_terminal() -> None:
    """Essa função limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
