import os
from keys import *
from interface import *
from time import sleep
"""
Tarefas:
- Armazenar a variável opcao em uma função no arquivo interface
- Informar quando o arquivo estiver vazio
- Estudar uma possível implementação do kivy ou fazer interface gráfica com pyqt5
- Implementar um sistema de backup
- Listar arquivos 
"""


def app():
    '''
    Tarefas:
    - Melhorar a troca de arquivos
    '''
    #introducao()
    lista_dos_arquivos = lista_de_arquivos()
    if len(lista_dos_arquivos) == 0:
        print("Você não possui arquivo de armazenamento de senhas.")
        arq_usuario = input(
                "Insira o nome do seu arquivo de senhas: ")
    elif len(lista_dos_arquivos) == 1:
        # Consertar: Nome fica com .json duas vezes
        for n in lista_dos_arquivos:
            arquivo_da_funcao = n[-5]
        print(f"Seu arquivo de senhas será:\n {arquivo_da_funcao}")
        arq_usuario = arquivo_da_funcao
    else:
        listar_arquivos(lista_dos_arquivos)
        arq_usuario = input(
                "Insira o nome do seu arquivo de senhas: ")
    
    while True:
        if arq_usuario == "0":
            sleep(1)
            print("Encerrando...")
            sleep(1)
            break

        usuario = Gerenciador()
        # usuario.nome = arq_usuario
  
        arquivo_usuario = arq_usuario + ".json"

        if not os.path.isfile(arquivo_usuario):
            dict_inicial = {}
            with open(arquivo_usuario, "w") as arquivo:
                json.dump(dict_inicial, arquivo)
                
        sleep(1)
        opcao = input("\nO que você quer fazer? "
                      "\n- Digite 0 para encerrar o app"
                      "\n- Digite 1 para gerar uma nova senha"
                      "\n- Digite 2 para incluir uma senha existente"
                      "\n- Digite 3 para listar todas as senhas"
                      "\n- Digite 4 para criar ou alterar de usuário"
                      "\n- Digite 5 para listar os arquivos de senhas"
                      "\n- Digite 6 para exluir um login"
                      "\n- Digite 7 para excluir todo o conteúdo do arquivo \n")
                
        if opcao == "0":
            sleep(1)
            print("Encerrando...")
            sleep(1)
            break

        elif opcao == "1":
            while True:
                qnt = input(
                    "Digite a quantidade de dígitos que você precisa na sua senha: ")
                try:
                    qnt = int(qnt)
                    if qnt == int(qnt):
                        break
                except:
                    print("Erro! Insira um valor numérico válido.")

            login = input("Qual é o login da nova senha? ")
            senha = usuario.gerar_nova_senha(qnt)
            nova_senha = usuario.trata_dicio(arquivo_usuario, login, senha)

            if usuario.incluir_conteudo(arquivo_usuario, nova_senha):
                sleep(1)
                print(f"Sua nova senha gerada é: {senha}")
            else:
                print("Erro na função incluir_conteudo")

        elif opcao == "2":
            login = input("Qual é o novo login? ")
            senha = input("Qual é a nova senha? ")
            nova_senha = usuario.trata_dicio(arquivo_usuario, login, senha)

            if usuario.incluir_conteudo(arquivo_usuario, nova_senha):
                print("Novo login incluído com sucesso.")
            else:
                print("Erro na função incluir_conteudo")

        elif opcao == "3":
            usuario.ler_arquivo(arquivo_usuario)
            
        elif opcao == "4":
            arq_usuario = input(
            "Insira o nome do seu arquivo de senhas: ")

        elif opcao == "5":
            listar_arquivos()
            
        elif opcao == "6":
            login = input("Qual login você quer excluir? ")
            
            login_apagado= usuario.apagar_chave(arquivo_usuario, login)
            
            if usuario.incluir_conteudo(arquivo_usuario, login_apagado):
                print("Login e senha apagados com sucesso.")
            else:
                print("Erro na função incluir_conteudo")

        elif opcao == "7":
            while True:
                questao = input(f"Todo o conteúdo será perdido e essa alteração não poderá ser desfeita!"
                                f"\nTem certeza que deseja apagar todo o conteudo do arquivo {arquivo_usuario} (s/n)? ")
                # questao = questao.lower
                if questao == "s":
                    usuario.apagar_tudo(arquivo_usuario)
                    break
                elif questao == "n":
                    break
                else:
                    print("Digite s para Sim e n para Não.")
        else:
            print("Insira uma opção válida.")
            sleep(1)


if __name__ == "__main__":
    app()
