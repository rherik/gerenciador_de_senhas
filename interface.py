from time import sleep
import os


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
        print(n)
        
