import random
import string
import json
import os
from time import sleep


class Interface:
    def __init__(self, nome):
        self.nome = nome

    def lacos(self, tempo, vezes):
        sleep(tempo)
        for n in range(vezes):
            sleep(tempo)
            print(".")

    def introducao(self):
        print("Olá,\nbem vindx ao seu gerenciador de senhas em Python.")
        self.lacos(1, 2)
        print("Digite 0 em qualquer etapa para excerrar")
        self.lacos(1, 2)
        print("Esta aplicação lhe permitirá criar um arquivo de senhas exclusivamente seu \npara que você possa manipula-lo individualmente da forma que desejar.")
        self.lacos(2, 3)
        print("Será criado um arquivo com extenção .json, visando compatibilidade e performace.")
        self.lacos(2, 3)
        print("Para tal, escolha um nome para seu arquivo de senhas, \nesse também será seu nome de usuário para futuros acessos ao seu arquivo.")


class Gerenciador:
    def __init__(self, dir='./'):
        self.dir = dir

    # Cria um novo arquivo de extenção .json para o usuário
    def verifica_json(self, arq):
        if not ".json" in arq:
            arq = arq + ".json"
        return arq

    # Seleciona o arquivo para a aplicação
    def encontra_arquivo(self):

        self.lista_dos_arquivos = [
            n for n in os.listdir(self.dir) if '.json' in n]

        if len(self.lista_dos_arquivos) == 0:
            print("Você não possui arquivo de armazenamento de senhas.")
            sleep(1)
            novo_arquivo = input(
                "Insira o nome do seu arquivo de senhas: ")
            arquivo = self.dir + self.verifica_json(novo_arquivo)
            return arquivo

        elif len(self.lista_dos_arquivos) == 1:
            arquivo = self.dir + self.lista_dos_arquivos[0]
            print(f"Seu arquivo de senhas atual é:\n{arquivo}")
            return arquivo

        else:
            self.listar_arquivos()
            novo_arquivo = input(
                "Insira o nome do seu arquivo de senhas: ")
            if novo_arquivo == "0":
                return
            arquivo = self.dir + self.verifica_json(novo_arquivo)
            return arquivo

    def listar_arquivos(self):
        print("Seus arquivos sao:")
        for arq_lista in self.lista_dos_arquivos:
            sleep(1)
            print(arq_lista)
            
    # Cria um novo arquivo vazio
    def cria_arq(self, arq):
        dicio_vazio = {}
        if not arq in os.listdir(self.dir):
            with open(arq, "w") as arquivo:
                json.dump(dicio_vazio, arquivo)
                print("Arquivo alterado com sucesso.")
            return arq
        else:
            print(f"Arquivo {arq} já existe.")
            return arq



class Aplicacao(Gerenciador):
    def __init__(self, arq):
        self.arq = arq

    def incluir_conteudo(self, conteudo):
        '''
        Apaga o último arquivo json e cria um novo com um dicionário atualizado
        '''
        try:
            # Fazer um laço for com os.walk aqui
            with open(self.arq, 'w') as arquivo:
                json.dump(conteudo, arquivo, indent=4)
                return True
        except Exception as E:
            print(f"Erro {E} ao incluir lista.")
            return False

    def trata_dicio(self, login, senha):
        '''
        Armazena um dicionário a partir do conteúdo do arquivo, inclui os novos login e senha
        :return: Um novo dicionário para atualizar o arquivo
        '''
        with open(self.arq, "r") as arquivo:
            dicio_nome = json.load(arquivo)
        dicio_nome[login] = senha
        return dicio_nome

    def ler_arquivo(self):
        i = 1
        with open(self.arq, 'r') as arquivo:
            dados = json.load(arquivo)
        if len(dados) == 0:
            print("Nenhuma senha nesse arquivo.")
        else:
            for chave, valor in dados.items():
                sleep(1)
                print(f"\nO login da {i}º senha é:",
                      chave, "\ne a senha é:", valor)
                i += 1

    def gerar_nova_senha(self, tipo, quantidade_digitos=int()):
        """
        Exige que o usuário insira o login da senha como chave para o dicionário.
        :return: A senha de oito dígitos que foi gerada.
        """
        letras = string.ascii_letters
        digitos = string.digits
        caracteres = '_-@#$%.*!'
        try:
            if tipo == '2':
                senha = ''.join(random.choices(letras + digitos +
                                caracteres, k=quantidade_digitos))
                return senha
            elif tipo == '1':
                senha = ''.join(random.choices(digitos, k=quantidade_digitos))
                return senha

        except Exception as e:
            print(f'Erro "{e}" ao criar a senha.')

    def apagar_chave(self, login):
        '''
        Armazena um dicionário a partir do conteúdo do arquivo, apaga uma chave do dicionário por vez
        :return: Um novo dicionário para atualizar o arquivo
        '''
        with open(self.arq, "r") as arquivo:
            dicio_nome = json.load(arquivo)
        dicio_nome.pop(login)
        return dicio_nome

    # Cria um arquivo vazio ou apaga o conteúdo do arquivo
    def arq_vazio(self, arq):
        '''
        Apaga todo o conteúdo do arquivo
        '''
        dicio_vazio = {}
        with open(self.arq, "w") as arquivo:
            json.dump(dicio_vazio, arquivo)
            print("Conteúdo apagado com sucesso.")

    def exclui_arquivo(self, arq):
        try:
            os.remove(arq)
            print("Arquivo excluído com sucesso.")
        except Exception as e:
            print(f"Erro {e} ao excluír o arquivo {arq}. Tente novamente.")

