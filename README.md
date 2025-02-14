# Locadora de Carros

Este é um projeto de terminal simples simples de uma locadora de carros, desenvolvido em Python.
Durante o módulo de Python Basics do curso de machine learning que estou fazendo, foi sugerido a ideia deste projeto para praticar os fundamentos da linguagem Python.
O programa permite alugar, devolver, cadastrar e remover carros do portfólio.

## Estrutura do Projeto

- `main.py`: Contém a função principal do programa e o menu principal.
- `utils.py`: Contém funções utilitárias e variáveis para o programa principal.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/LucaBendasoli/locadora-de-carros.git
    cd locadora-de-carros
    ```

## Funcionalidades

- Mostrar portfólio de carros disponíveis
- Alugar um carro
- Cadastrar um novo carro
- Mostrar carros alugados
- Devolver um carro
- Remover um carro

## Uso

1. Execute o script main.py:
    ```sh
    python main.py
    ```

2. O programa exibirá o menu principal com as seguintes opções:
    ```
    Bem vindo a Locadora de Carros!

    O que deseja fazer?
    |    0 - Mostrar Porifólio    |  1 - Alugar um carro  | 2 - Cadastrar um novo carro |
    0=============================0=======================O=============================0
    | 3 - Mostrar carros alugados | 4 - Devolver um carro |    5 - Remover um carro     |
    ```

3. Digite o número correspondente à ação que deseja realizar e siga as instruções na tela.

## TODO

- Registrar todas as ações em um arquivo.
- Adicionar função para editar carros no registro.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-nova-funcionalidade`
3. Faça suas alterações e commit: `git commit -m 'Adiciona nova funcionalidade'`
4. Envie para o repositório remoto: `git push origin minha-nova-funcionalidade`
5. Abra um Pull Request.
