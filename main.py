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
    
    
def devolver_um_carro() -> None:
    limpar_terminal()
    print("Carro devolvido")
    input("Pressione enter para voltar")
    limpar_terminal()

    
if __name__ == '__main__':
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
    while True:
        inicio()
        escolhe_opcao()