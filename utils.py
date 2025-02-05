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

carros_alugados = {}

def montar_portifolio(portifolio: str, main_func: bool = False) -> None:
    """Percorre um dicionário do portifolio e imprime os carros disponíveis
    
    Args:
        main_func (bool, optional): Se a função está
        sendo chamada pelo menu principal. Padrão é False."""
    limpar_terminal()
    if portifolio == "carros_alugados":
        if len(carros_alugados) == 0:
            if main_func:
                input("""
Não há carros alugados no momento.
Pressione enter para voltar.""")
            limpar_terminal()
            return
        portifolio = carros_alugados
    if portifolio == "carros_disponiveis":
        if len(carros_disponiveis) == 0:
            if main_func:
                input("""
Não há carros disponíveis no momento.
Pressione enter para continuar.""")
                limpar_terminal()
            return
        portifolio = carros_disponiveis
    for indice, (carro, valor) in enumerate(portifolio.items()):
        print(f"[{indice}] {carro} - {valor}")
    if main_func:
        input("Pressione enter para voltar")
        limpar_terminal()
        
def alugar_um_carro() -> None:
    """Aluga um carro para o usuário e remove o carro
    do portifólio e adicona aos carros alugados."""
    limpar_terminal()
    montar_portifolio("carros_disponiveis")
    escolher_carro_para_alugar()

def devolver_um_carro() -> None:
    """Devolve um carro para o portifólio de carros 
    disponíveis e remove dos carros alugados."""
    limpar_terminal()
    montar_portifolio("carros_alugados")
    escolher_carro_para_devolver()

def escolher_carro_para_alugar() -> None:
    """Essa função permite que o usuário escolha um carro para alugar."""
    if len(carros_disponiveis) == 0:
        print("Não há carros disponíveis no momento.")
        input("Pressione enter para continuar.")
        limpar_terminal()
        return
    escolha = int(input("Escolha o código do carro\n"))
    try:
        if not validar_escolha_do_carro(escolha, carros_disponiveis):
            return
        dias = int(input("Quantos dias você quer alugar este carro?\n"))
        if not validar_dias_alugados(dias):
            return
        chave, valor = obter_info_do_carro_cadastrado(escolha, carros_disponiveis)
        if confirmar(chave, dias, valor):
            transferir_carro(carros_disponiveis, carros_alugados, chave)
            limpar_terminal()
            print(f"Parabéns você alugou o {chave} por {dias} dias.")
    except:
        escolha_invalida()

def escolher_carro_para_devolver() -> None:
    """"Essa função permite ao usuário escolher um carro para devolver."""
    if len(carros_alugados) == 0:
        print("Não há carros alugados no momento.")
        input("Pressione enter para continuar.")
        limpar_terminal()
        return
    escolha = input("Escolha o codigo do carro para devolve-lo\n")
    try:
        escolha = int(escolha)
        if not validar_escolha_do_carro(escolha, carros_alugados):
            return
        informacoes = obter_info_do_carro_cadastrado(escolha, carros_alugados)
        transferir_carro(carros_alugados, carros_disponiveis, informacoes[0])
        limpar_terminal()
        print(f"Obrigado por devolver o carro: {informacoes[0]}.")
        input("Pressione enter para continuar.")
        limpar_terminal()
    except:
        pass

def escolha_invalida() -> None:
    """Essa função é chamada quando o usuário faz uma escolha inválida."""
    limpar_terminal()
    print("Escolha inválida, tente novamente.")

def limpar_terminal() -> None:
    """Essa função limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_escolha_do_carro(escolha: int, portifolio: dict) -> bool:
    """Valida a escolha do usuário para alugar um carro.

    Args:
        escolha (int): codigo do carro escolhido
        portifolio (dict): dicionário de carros a ser escolhido

    Returns:
        bool: se o codigo escolhido é válido ou não
    """
    if escolha < 0 or escolha >= len(portifolio):
        escolha_invalida()
        return False
    return True

def validar_dias_alugados(dias: int) -> bool:
    """Valida a quantidade de dias que o usuário deseja alugar um carro.

    Args:
        dias (int): quantidade de dias escolhidos

    Returns:
        bool: se a quantidade de dias é válida ou não
    """
    if dias <=0:
        escolha_invalida()
        return False
    return True

def obter_info_do_carro_cadastrado(escolha: int, portifolio: dict) -> tuple:
    """Obtém informações do carro escolhido pelo usuário.

    Args:
        escolha (int): código do carro escolhido
        portifolio (dict): dicionário de carros a ser escolhido

    Returns:
        tuple: chave e valor do carro
    """
    chave = list(portifolio.keys())[escolha]
    valor_por_dia = list(portifolio.values())[escolha].split()[1]
    valor = int(valor_por_dia.split("/")[0])
    return chave, valor

def cadastrar_um_carro() -> None:
    """Adiciona um carro ao portifólio de carros disponíveis."""
    
    limpar_terminal()
    chave = input("""Você está prestes a cadastrar um novo carro.
Escreva o nome do carro para continuar.\n""")
    valor = input("""Qual o valor da diária deste carro?\n""")
    try:
        int(valor)
        limpar_terminal()
    except:
        escolha_invalida()
        return
    confirmacao = int(input(f"""Você está cadastrando {chave} pelo valor de R$ {valor}/dia.
| 1 - Confirmar | 0 - Cancelar |"""))
    if not confirmacao in [0, 1]:
        escolha_invalida()
        return
    if confirmacao == 0:
        limpar_terminal()
        return
    carros_disponiveis[chave] = f"R$ {valor}/dia"
    
def remover_um_carro() -> None:
    """Remove um carro do porifólio de carros disponíveis."""
    
    limpar_terminal()
    montar_portifolio("carros_disponiveis")
    escolha = int(input("Escolha o código do carro que quer remover do sistema.\n"))
    infos = obter_info_do_carro_cadastrado(escolha, carros_disponiveis)
    confirmacao = int(input(f"""Tem certeza que quer remover {infos[0]} do sistema?
1 - Confirmar | 0 - Cancelar\n"""))
    if not confirmacao in [0, 1]:
        escolha_invalida()
        return
    if confirmacao == 0:
        limpar_terminal()
        return
    carros_disponiveis.pop(infos[0])
    limpar_terminal()

def confirmar(chave: str, dias: int, valor: int) -> bool:
    """Pergunta ao cliente se ele deseja alugar o carro escolhido.

    Args:
        chave (str): nome do carro
        dias (int): quantidade de dias a ser alugado
        valor (int): valor por dia do carro

    Returns:
        bool: se usuário confirmou ou não
    """
    print(f"Você escolheu {chave} por {dias} dias.")
    print(f"O aluguel totalizaria R$ {valor * dias}.")
    print("Deseja alugar?")
    desistencia = input("1 - SIM | 0 - NÃO\n")
    if desistencia not in ['0', '1']:
        escolha_invalida()
        return False
    if desistencia == '0':
        limpar_terminal()
        return False
    return True

def transferir_carro(remetente: dict, destinatario:dict, chave:str) -> None:
    """Essa função passa um carro do dicionário carros_disponiveis
    para o dicionário carros_alugados."""
    try:
        valor = remetente.pop(chave, None)
        destinatario[chave] = valor
    except:
        limpar_terminal()
        input("Ocorreu um erro, pressione enter para continuar.")
