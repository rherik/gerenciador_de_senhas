import os
from keys import *
from interface import *
"""
Tarefas:
- Estudar uma possível implementação do kivy
- Fazer interface gráfica com pyqt5
- Implementar um sistema de backup
"""


def app():
    '''
    Tarefas:
    - Melhorar a trocar de arquivos
    '''
    introducao()
    while True:
        arq_usuario = input(
            "Insira o nome do seu arquivo de senhas: ")

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

        opcao = input("\nO que você quer fazer? "
                      "\n- Digite 0 para encerrar o app"
                      "\n- Digite 1 para gerar uma nova senha"
                      "\n- Digite 2 para incluir uma senha existente"
                      "\n- Digite 3 para listar todas as senhas"
                      "\n- Digite 4 para excluir todo o conteúdo do arquivo \n")
                    # Digite 5 para exluir um login
                    # Digite 6 para trocar de arquivo

        if opcao == "0":
            sleep(1)
            print("Encerrando...")
            sleep(1)
            break

        elif opcao == "1":
            # qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
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
