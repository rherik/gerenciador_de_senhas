from keys import *
qnt = int(
            input("Digite a quantidade de dígitos que você precisa na sua senha: "))
nome = input("Qual é o nome da nova senha? ")
senha = gerar_nova_senha(qnt)
nova_senha = trata_dicio(nome, senha)
# print(f"A nova senha é {nova_senha}")
incluir_conteudo(nova_senha)
