import random, string, json

"""
Próximos passos:
- Corrigir escrita de conteúdo
- Projetar uma interface de terminal mais amigável
- Função para criar novo arquivo(.json) de senhas
- Implementar um sistema de backup
"""


def incluir_conteudo(arq, conteudo):
    try:
        with open(arq, 'w+') as arquivo:
            arquivo.write(conteudo)
            arquivo.write('\n')
            arquivo.seek
        '''with open(arq, 'w+') as arquivo:
            arquivo.write(conteudo)
            arquivo.write('\n')
            arquivo.seek
        print('Incluido com sucesso.')
        return True'''
    except Exception as E:
        print(f"Erro {E} ao incluir lista.")
        return False


def ler_arquivo(arq):
    with open(arq, 'r') as arquivo:
        for n in arquivo:
            print(n, end='')


def gerar_nova_senha(quantidade_digitos=int()):
    """
    Crie uma variável para guardar o resultado dessa função.
    Exige que o usuário
    :return: Uma senha de oito dígitos será gerada.
    """
    try:
        letras = string.ascii_letters
        digitos = string.digits
        caracteres = '_-@#$%.*!'
        senha = ''.join(random.choices(letras + digitos + caracteres, k=quantidade_digitos))
        return senha

    except Exception as e:
        print(f'Erro "{e}" ao criar a senha.')


print("Olá, bem vindx ao seu gerenciador de senhas em Python.")
opcao = input("O que você quer fazer? "
              "\n- Gerar nova senha(Digite 1) "
              "\n- Listar senhas(Digite 2) \n")
if opcao == "1":
    qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
    '''while qnt != int(qnt):
        qnt = int(input("Digite a quantidade de dígitos que você precisa na sua senha: "))
        if qnt == int(qnt):
            break'''
    nome_senha = input("Qual é o nome da nova senha? ")
    senha = gerar_nova_senha(qnt)
    senhas = {nome_senha: senha,}
    incluir_conteudo("senhas.json", str(senhas))
    if incluir_conteudo == True:
        print(f"Sua nova senha gerada é: {senha}")
    else:
        print("O arquivo .json não existe")
elif opcao == "2":
    nome_arquivo = input("Digite o nome completo do seu arquivo(Incluindo a extenção): ")
    ler_arquivo(nome_arquivo)
else:
    print("Digite uma opção válida.")
