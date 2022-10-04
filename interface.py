from time import sleep
import os

"""
Tarefas:
- Informar quando o arquivo estiver vazio e listar arquivos
- Melhorar a troca de arquivos
"""


def lacos(tempo, vezes):
    sleep(tempo)
    for n in range(vezes):
        sleep(1)
        print(".")


def introducao():
    print("Olá,\nbem vindx ao seu gerenciador de senhas em Python.")
    lacos(1, 2)
    print("Digite 0 em qualquer etapa para excerrar")
    lacos(1, 2)
    print("Esta aplicação lhe permitirá criar um arquivo de senhas exclusivamente seu \npara que você possa manipula-lo individualmente da forma que desejar.")
    lacos(2, 3)
    print("Será criado um arquivo com extenção .json, visando compatibilidade e performace.")
    lacos(2, 3)
    print("Para tal, escolha um nome para seu arquivo de senhas, \nesse também será seu nome de usuário para futuros acessos ao seu arquivo.")


def lista_de_arquivos():
    arq_json = [n for n in os.listdir("./") if ".json" in n]
    return arq_json        

def listar_arquivos(arquivos_listados):
    print("Os arquivos são: ")
    for n in arquivos_listados:
        print(f"{n}\n")
        sleep(1)
        
        
def encontra_arquivo():
    lista_dos_arquivos = lista_de_arquivos()
    if len(lista_dos_arquivos) == 0:
        print("Você não possui arquivo de armazenamento de senhas.")
        arquivo = input(
                "Insira o nome do seu arquivo de senhas: ")
    elif len(lista_dos_arquivos) == 1:
        for n in lista_dos_arquivos:
            arquivo_da_funcao = n
        print(f"Seu arquivo de senhas atual é:\n {arquivo_da_funcao}")
        arquivo = arquivo_da_funcao
    else:
        listar_arquivos(lista_dos_arquivos)
        arquivo = input(
                "Insira o nome do seu arquivo de senhas: ")
    return arquivo

def verifica_json(arquivo_usuario):
    if ".json" not in arquivo_usuario:
        arquivo_usuario = arquivo_usuario + ".json"
    return arquivo_usuario
