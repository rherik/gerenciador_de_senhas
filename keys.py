import random
import string
import json
from time import sleep

"""
Próximos passos:
- Criar um loop que encerra a aplicação apenas quando o usuário requisita
- Criar função para excluir uma senha por vez(método de dicionário: pop
  Ex:dicio_senhas.pop("nome do indice"))
- Criptografar as senhas ou o arquivo json
- Criar a classe Gerenciador
- Fazer interface gráfica com pyqt5
- Implementar um sistema de backup
"""


# Apaga o último arquivo json e cria um novo com um dicionário atualizado
def incluir_conteudo(conteudo):
    try:
        with open("senhas.json", 'w') as arquivo:
            json.dump(conteudo, arquivo, indent=4)
            print('Nova senha incluida com sucesso.')
            return True
    except Exception as E:
        print(f"Erro {E} ao incluir lista.")
        return False


# Cria um dicionário atualizado com a nova senha para uso da função incluir_conteudo
def trata_dicio(login, senha):
    with open("senhas.json", "r") as arquivo:
        dicio_nome = json.load(arquivo)
    dicio_nome[login] = senha
    return dicio_nome


def ler_arquivo():
    i = 1
    with open("senhas.json", 'r') as arquivo:
        dados = json.load(arquivo)
    for chave, valor in dados.items():
        sleep(1)
        print(f"\nO login da {i}º senha é:", chave, "\ne a senha é:", valor)
        i += 1


# Função fora da classe Gerenciador que será criada futuramente
def gerar_nova_senha(quantidade_digitos=int()):
    """
    Exige que o usuário insira o login da senha como chave para o dicionário.
    :return: Uma senha de oito dígitos será gerada.
    """
    try:
        letras = string.ascii_letters
        digitos = string.digits
        caracteres = '_-@#$%.*!'
        senha = ''.join(random.choices(letras + digitos +
                        caracteres, k=quantidade_digitos))
        return senha

    except Exception as e:
        print(f'Erro "{e}" ao criar a senha.')


def apagar_tudo():
    dicio_vazio = {}
    with open("senhas.json", "w") as arquivo:
        json.dump(dicio_vazio, arquivo)
