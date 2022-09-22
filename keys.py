import random
import string
import json
from time import sleep

"""
Próximos passos:
- Criar um loop que encerra apenas quando o usuário requisita
- Criar função para excluir uma senha por vez
- Criptografar as senhas ou o arquivo json
- Criar uma classe gerenciadora
- Projetar uma interface de terminal mais amigável
- Implementar um sistema de backup
- Conteudo de ajuda: https://pt.stackoverflow.com/questions/467031/atualizar-conte%c3%bado-de-arquivo-json
"""


# Apaga o último arquivo json e cria um novo com um dicionário atualizado
def incluir_conteudo(conteudo):
    try:
        with open("senhas.json", 'w') as arquivo:
            json.dump(conteudo, arquivo, indent=4)
            print('Nova senha incluida com sucesso.')
            return True
    except Exception as E:
        print(f"Erro {E} ao incluir lista.")
        return False
    
# Cria um dicionário atualizado com a nova senha para uso da função incluir_conteudo
def trata_dicio(login, senha):
    with open("senhas.json", "r") as arquivo:
        dicio_senhas = json.load(arquivo)
    dicio_senhas[login] = senha
    return dicio_senhas
    

def ler_arquivo():
    i = 1
    with open("senhas.json", 'r') as arquivo:
        dados = json.load(arquivo)
    for chave, valor in dados.items():
        sleep(1)
        print(f"\nO login da {i}º senha é:", chave, "\ne a senha é:", valor)
        i += 1


# Função fora da classe Gerenciador que será criada futuramente
def gerar_nova_senha(quantidade_digitos=int()):
    """
    Exige que o usuário insira o login da senha como chave para o dicionário.
    :return: Uma senha de oito dígitos será gerada.
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


def app():
    print("Olá,\nbem vindx ao seu gerenciador de senhas em Python.")
    sleep(2)
    opcao = input("O que você quer fazer? "
                  "\n- Gerar nova senha (Digite 1) "
                  "\n- Listar senhas(Digite 2) \n")
    
    if opcao == "1":
        qnt = int(
            input("Digite a quantidade de dígitos que você precisa na sua senha: "))
        '''while qnt != int(qnt):
            qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
            if qnt == int(qnt):
                break'''

        login = input("Qual é o login da nova senha? ")
        senha = gerar_nova_senha(qnt)
        # nome_e_senha = {nome: senha}

        nova_senha = trata_dicio(login, senha)                
        
        if incluir_conteudo(nova_senha):
            print(f"Sua nova senha gerada é: {senha}")
            
        else:
            print("Erro na função incluir_conteudo")
            
    elif opcao == "2":
        ler_arquivo()
    else:
        print("Digite uma opção válida.")


if __name__ == "__main__":
    app()
