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
        lista_dos_arquivos = []
        for root, subfolder, files in os.walk(self.dir):
            for filename in files:
                if '.json' in filename:
                    lista_dos_arquivos.append(filename)
                    
        if len(lista_dos_arquivos) == 0:
            print("Você não possui arquivo de armazenamento de senhas.")
            sleep(1)
            novo_arquivo = input(
                    "Insira o nome do seu arquivo de senhas: ")
            arquivo = self.verifica_json(novo_arquivo)
            return arquivo
        
        elif len(lista_dos_arquivos) == 1:
            for n in lista_dos_arquivos:
                arquivo_da_funcao = n
            print(f"Seu arquivo de senhas atual é:\n{arquivo_da_funcao}")
            arquivo = arquivo_da_funcao
            return arquivo
        
        else:
            self.listar_arquivos(lista_dos_arquivos)
            novo_arquivo = input(
                    "Insira o nome do seu arquivo de senhas: ")
            arquivo = self.verifica_json(novo_arquivo)
            return arquivo


class Aplicacao(Gerenciador):
    def __init__(self):
        super().__init__(dir)
        self.dir = dir
        # self.nome_arq = self.encontra_arquivo()
        self.arq = "D:\\Users\\hcunha.ciee\\Downloads\\Tarefas\\" + Gerenciador.encontra_arquivo()
    
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
            
    def apagar_chave(self, login):
        '''
        Armazena um dicionário a partir do conteúdo do arquivo, apaga uma chave do dicionário por vez
        :return: Um novo dicionário para atualizar o arquivo
        '''
        with open(self.arq, "r") as arquivo:
            dicio_nome = json.load(arquivo)
        dicio_nome.pop(login)
        return dicio_nome

    def apagar_tudo(self):
        '''
        Apaga todo o conteúdo do arquivo
        '''
        dicio_vazio = {}
        with open(self.arq, "w") as arquivo:
            json.dump(dicio_vazio, arquivo)
            print("Conteúdo apagado com sucesso.")
            