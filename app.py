import os
from keys import *

if not os.path.isfile("senhas.json"):
    dict_inicial = {}
    with open("senhas.json", "w") as arquivo:
        json.dump(dict_inicial, arquivo)


def app():
    print("Olá,\nbem vindx ao seu gerenciador de senhas em Python.")
    sleep(2)
    opcao = input("O que você quer fazer? "
                  "\n- Gerar nova senha (Digite 1) "
                  "\n- Incluir senha existente (Digite 2) "
                  "\n- Listar senhas(Digite 3) "
                  "\n- Excluir tudo (Digite 4) \n")

    if opcao == "1":
        qnt = int(
            input("Digite a quantidade de dígitos que você precisa na sua senha: "))
        '''while qnt != int(qnt):
            qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
            if qnt == int(qnt):
                break'''

        login = input("Qual é o login da nova senha? ")
        senha = gerar_nova_senha(qnt)
        nova_senha = trata_dicio(login, senha)

        if incluir_conteudo(nova_senha):
            print(f"Sua nova senha gerada é: {senha}")
        else:
            print("Erro na função incluir_conteudo")

    elif opcao == "2":
        login = input("Qual é o novo login? ")
        senha = input("Qual é a nova senha? ")
        nova_senha = trata_dicio(login, senha)

        if incluir_conteudo(nova_senha):
            print("Novo login incluído com sucesso.")
        else:
            print("Erro na função incluir_conteudo")

    elif opcao == "3":
        ler_arquivo()

    elif opcao == "4":
        apagar_tudo()
    else:
        print("Digite uma opção válida.")


if __name__ == "__main__":
    app()
