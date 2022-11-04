import os
from gerenciador.classes import *
from time import sleep

# Se não houver um arquivo de senhas neste diretório o app cria um arquivo .json sem nome. 
# caminho_usuario = os.path.expanduser(r"~")
# caminho = "{caminho_usuario}/Documents/Pessoas/Herik/Documentos/senhas/"
# caminho_usuario = os.path.expanduser(r"~")
# caminho = r"D:\\Users\\hcunha.ciee\\Downloads\\Tarefas\\"


def app():
    caminho_usuario = os.path.expanduser(r"~")
    caminho = r"D:\\Users\\hcunha.ciee\\Downloads\\Tarefas\\"
    
    interface = Interface(True)
    gerenciador = Gerenciador(caminho)
    aplicacao = Aplicacao()
    
    interface.introducao()

    while True:
        if arquivo_usuario == "0":
            sleep(1)
            print("Encerrando...")
            sleep(1)
            break
        
        else:
            """
            if not os.path.isfile(arquivo_usuario):
                dict_inicial = {}
                with open(arquivo_usuario, "w") as arquivo:
                    json.dump(dict_inicial, arquivo)
            """
            sleep(1)
            opcao = input("\nO que você quer fazer? "
                        "\n- Digite 0 para encerrar o app;\n"

                        "\n- Digite 1 para gerar uma nova senha;\n"

                        "\n- Digite 2 para incluir uma senha existente;\n"

                        "\n- Digite 3 para listar todas as senhas;\n"

                        "\n- Digite 4 para criar ou alterar de usuário;\n"

                        "\n- Digite 5 para listar os arquivos de senhas;\n"

                        "\n- Digite 6 para exluir um login;\n"

                        "\n- Digite 7 para excluir todo o conteúdo do arquivo; \n"

                        "\n- Digite 8 para excluir um arquivo. \n")

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
                senha = aplicacao.gerar_nova_senha(qnt)
                nova_senha = aplicacao.trata_dicio(arquivo_usuario, login, senha)

                if aplicacao.incluir_conteudo(arquivo_usuario, nova_senha):
                    sleep(1)
                    print(f"Sua nova senha gerada é: {senha}")
                else:
                    print("Erro na função incluir_conteudo")

            elif opcao == "2":
                login = input("Qual é o novo login? ")
                senha = input("Qual é a nova senha? ")
                nova_senha = aplicacao.trata_dicio(arquivo_usuario, login, senha)

                if aplicacao.incluir_conteudo(nova_senha):
                    print("Novo login incluído com sucesso.")
                else:
                    print("Erro na função incluir_conteudo")

            elif opcao == "3":
                aplicacao.ler_arquivo()

            elif opcao == "4":
                arquivo_usuario = input(
                    "Insira o nome do seu arquivo de senhas: ")

            elif opcao == "5":
                gerenciador.listar_arquivos()

            elif opcao == "6":
                login = input("Qual login você quer excluir? ")

                login_apagado = aplicacao.apagar_chave(login)

                if aplicacao.incluir_conteudo(login_apagado):
                    print("Login e senha apagados com sucesso.")
                else:
                    print("Erro na função incluir_conteudo")

            elif opcao == "7":
                while True:
                    questao = input(f"Todo o conteúdo será perdido e essa alteração não poderá ser desfeita!"
                                    f"\nTem certeza que deseja apagar todo o conteudo do arquivo {arquivo_usuario} (s/n)? ")
                    # questao = questao.lower
                    if questao == "s":
                        aplicacao.apagar_tudo()
                        break
                    elif questao == "n":
                        break
                    else:
                        print("Digite s para Sim e n para Não.")

            elif opcao == "8":
                arquivo = input("Qual é o nome do arquivo que você quer excluir? ")
                arquivo = gerenciador.verifica_json(arquivo)
                if arquivo == arquivo_usuario:
                    arquivo_usuario = ""
                try:
                    os.remove(arquivo)
                    print("Arquivo excluído com sucesso.")
                except Exception as e:
                    print(f"Erro {e} ao excluír arquivo. Tente novamente.")

            else:
                print("Insira uma opção válida.")
                sleep(1)


if __name__ == "__main__":
    app()
