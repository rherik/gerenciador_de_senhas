import random
import string
import json
from time import sleep


class Gerenciador:
    '''
    Tarefas:
    - Incluir ao método apagar chave se o login informado existe no arquivo
    - Criptografar o arquivo json.(pyAesCrypt)
    '''
    
    def incluir_conteudo(self, arq, conteudo):
        '''
        Apaga o último arquivo json e cria um novo com um dicionário atualizado
        '''
        try:
            with open(arq, 'w') as arquivo:
                json.dump(conteudo, arquivo, indent=4)
                return True
        except Exception as E:
            print(f"Erro {E} ao incluir lista.")
            return False

    def trata_dicio(self, arq, login, senha):
        '''
        Armazena um dicionário a partir do conteúdo do arquivo, inclui os novos login e senha
        :return: Um novo dicionário para atualizar o arquivo
        '''
        with open(arq, "r") as arquivo:
            dicio_nome = json.load(arquivo)
        dicio_nome[login] = senha
        return dicio_nome


    def ler_arquivo(self, arq):
        i = 1
        with open(arq, 'r') as arquivo:
            dados = json.load(arquivo)
        for chave, valor in dados.items():
            sleep(1)
            print(f"\nO login da {i}º senha é:", chave, "\ne a senha é:", valor)
            i += 1


    def gerar_nova_senha(self, quantidade_digitos=int()):
        """
        Exige que o usuário insira o login da senha como chave para o dicionário.
        :return: A senha de oito dígitos que foi gerada.
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
            
    def apagar_chave(self, arq, login):
        '''
        Armazena um dicionário a partir do conteúdo do arquivo, apaga uma chave do dicionário por vez
        :return: Um novo dicionário para atualizar o arquivo
        '''
        with open(arq, "r") as arquivo:
            dicio_nome = json.load(arquivo)
        dicio_nome.pop(login)
        return dicio_nome

    def apagar_tudo(self, arq):
        '''
        Apaga todo o conteúdo do arquivo
        '''
        dicio_vazio = {}
        with open(arq, "w") as arquivo:
            json.dump(dicio_vazio, arquivo)
            print("Conteúdo apagado com sucesso.")
            