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
    escolha = input()
    try:
        escolha = int(escolha)
        if escolha < 0 or escolha >= len(carros_disponiveis):
            escolha_invalida()
        
        dias = int(input("Quantos dias você quer alugar este carro?\n"))
        chave = list(carros_disponiveis.keys())[escolha]
        valor_por_dia = list(carros_disponiveis.values())[escolha].split()[1]
        valor = int(valor_por_dia.split("/")[0])
        
        desistencia = input(f"Você escolheu {chave} por {dias} dias.\nO aluguel totalizaria R$ {valor * dias}. Deseja alugar?\n\n0 - SIM | 1 - NÃO\n") 
               
        if desistencia not in ['0', '1']:
            escolha_invalida()
            return
        elif desistencia == '1':
            limpar_terminal()
            return
              
        carros_disponiveis.pop(chave, None)
        limpar_terminal()
        print(f"Parabéns você alugou o {chave} por {dias} dias.")
    except Exception as e:
        print(e)
        escolha_invalida()

def escolha_invalida():
    limpar_terminal()
    print("Escolha inválida, tente novamente")
        

def limpar_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    