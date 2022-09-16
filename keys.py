import random, string, json
from time import sleep
import os
import tempfile, shutil

"""
Próximos passos:
- Corrigir escrita de conteúdo
- Projetar uma interface de terminal mais amigável
- Função para criar novo arquivo(.json) de senhas
- Implementar um sistema de backup
- Conteudo de ajuda: https://pt.stackoverflow.com/questions/467031/atualizar-conte%c3%bado-de-arquivo-json
"""


def incluir_conteudo(arq, conteudo):
    if os.path.isfile(arq):
        try:
            with open(arq, 'r') as arquivo:
                tempfile.NamedTemporaryFile('w', delete=False) as out:
                conteudo = json.load(arq)
                conteudo = {nome_senha: senha}
                json.dump(conteudo, arquivo, indent=4)
            print('Incluido com sucesso.')
            return True
        except Exception as E:
            print(f"Erro {E} ao incluir lista.")
            return False
    else:
        print("Arquivo não existe.")
        return False


def ler_arquivo(arq):
    with open(arq, 'r') as arquivo:
        dados = json.load(arquivo)
    for chave, valor in dados.items():
        print("O nome da senha é:",chave, ", e a senha é:",valor)


def gerar_nova_senha(quantidade_digitos=int()):
    """
    Exige que o usuário insira o nome da senha como chave para o dicionário.
    :return: Uma senha de oito dígitos será gerada.
    """
    try:
        letras = string.ascii_letters
        digitos = string.digits
        caracteres = '_-@#$%.*!'
        senha = ''.join(random.choices(letras + digitos + caracteres, k=quantidade_digitos))
        return senha

    except Exception as e:
        print(f'Erro "{e}" ao criar a senha.')


def interface_de_terminal():
    print("Olá,\nbem vindx ao seu gerenciador de senhas em Python.")
    sleep(2)
    opcao = input("O que você quer fazer? "
                "\n- Gerar nova senha(Digite 1) "
                "\n- Listar senhas(Digite 2) \n")
    if opcao == "1":
        qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
        '''while qnt != int(qnt):
            qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
            if qnt == int(qnt):
                break'''
                
        nome_senha = input("Qual é o nome da nova senha? ")
        senha = gerar_nova_senha(qnt)
        nome_e_senha = {nome_senha: senha,}
        
        incluir_conteudo("senhas.json", nome_e_senha)
        if incluir_conteudo == True:
            print(f"Sua nova senha gerada é: {senha}")
        elif incluir_conteudo == False:
            print("Erro na função incluir_conteudo")
    elif opcao == "2":
        ler_arquivo("senhas.json")
    else:
        print("Digite uma opção válida.")


interface_de_terminal()
