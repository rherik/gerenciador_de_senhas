# Tarefa: Criar uma lista 
# com os arquivos do diretório atual
import os
from gerenciador.classes import *
class Teste:
    def __init__(self):
        self.caminho_usuario = os.path.expanduser(r"~")
        self.caminho = fr"{self.caminho_usuario}\\Downloads\\Tarefas\\"

    def funcao_de_lista(self):
        lista_dos_arquivos = []
        for root, subfolder, files in os.walk(self.caminho):
            for filename in files:
                if '.docx' in filename:
                    lista_dos_arquivos.append(filename)
        return lista_dos_arquivos
        
   
caminho_usuario = os.path.expanduser(r"~") # /home/kurtz
caminho = caminho_usuario + "/Downloads/Tarefas/"   
udemy = Aplicacao(caminho)
     
