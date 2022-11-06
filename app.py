import os
from gerenciador.classes import *
from time import sleep

# Se não houver um arquivo de senhas neste diretório o app cria um arquivo .json sem nome. 

def app():
    # Declaracão dos caminhos
    caminho_usuario = os.path.expanduser(r"~")
    caminho = caminho_usuario + "/Downloads/Tarefas/"
            
    # Instanciando as classes
    interface = Interface(True)
    gerenciador = Gerenciador(caminho)

    interface.introducao()
    
    arq = gerenciador.encontra_arquivo()
    gerenciador.cria_arq(arq)
    
    aplicacao = Aplicacao(arq)
        
    opcao = ''
    
    while True:
        if opcao == "0":
            sleep(1)
            print("Encerrando...")
            sleep(0.5)
            break
        
        else:
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
                nova_senha = aplicacao.trata_dicio(login, senha)

                if aplicacao.incluir_conteudo(nova_senha):
                    sleep(1)
                    print(f"Sua nova senha gerada é: {senha}")
                else:
                    print("Erro na função incluir_conteudo")

            elif opcao == "2":
                login = input("Qual é o novo login? ")
                senha = input("Qual é a nova senha? ")
                nova_senha = aplicacao.trata_dicio(login, senha)

                if aplicacao.incluir_conteudo(nova_senha):
                    print("Novo login incluído com sucesso.")
                else:
                    print("Erro na função incluir_conteudo")

            elif opcao == "3":
                aplicacao.ler_arquivo()
            
            # Cria ou altera de usuário
            elif opcao == "4":
                cria_altera = gerenciador.encontra_arquivo()
                gerenciador.cria_arq(cria_altera)

            # Lista todos os arquivos .json
            elif opcao == "5":
                gerenciador.encontra_arquivo()

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
                                    f"\nTem certeza que deseja apagar todo o conteudo do arquivo {arq} (s/n)? ")
                    # questao = questao.lower
                    if questao == "s":
                        aplicacao.arq_vazio(arq)
                        break
                    elif questao == "n":
                        break
                    else:
                        print("Digite s para Sim e n para Não.")

            elif opcao == "8":
                gerenciador.listar_arquivos()
                arquivo = input("Qual é o nome do arquivo que você quer excluir? ")
                arquivo = gerenciador.verifica_json(arquivo)
                arquivo = caminho + arquivo
                aplicacao.exclui_arquivo(arquivo)
            else:
                print("Insira uma opção válida.")
                sleep(1)


if __name__ == "__main__":
    app()
