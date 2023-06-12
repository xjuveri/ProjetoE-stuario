comunidades='comunidades.csv'
log='login.csv'
cad='cadastro.csv'
import csv
def inicio():
    print('\033[0;36m-\033[m'*40)
    print('\033[0;34mBem-vinda ao E-stuário\033[m'.center(50))
    print('\033[0;36m-\033[m'*40)
    while True:
        resp_cad = input('Já possui Cadastro? [Sim/Não] \n').upper()
        if resp_cad == 'SIM':
            login()
            feed_sim()
            eventos()
            comunidade()
            break
        elif resp_cad == 'NÃO' or resp_cad == 'NAO':
            cadastro()
            feed_nao()
            eventos()
            comunidade()
            break
        else:
            print('Digite uma resposta válida.')

def login():
    while True:
        email = input('Digite o seu email: ')
        senha = input('Digite sua senha: ')
        arquivo = open('cadastro.csv', 'r')
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            if dados[2] == email and dados[3] == senha:
                print('\033[4mLogin bem sucedido!\033[m')
                arquivo.close()
                return
        print('\033[4mEmail ou senha incorretos.\033[m \033[4mTente novamente.\033[m')
        arquivo.close()

def cadastro():
    nome = ''
    sobrenome = ''
    email = ''
    senha = ''
    idd = ''
    while True:
        perfil = input('Seu perfil será pessoal ou uma comunidade? ').upper()
        if perfil == 'PESSOAL':
            while not nome:
                nome = input('Digite seu nome: ')
            while not sobrenome:
                sobrenome = input('Digite seu sobrenome: ')
            while not email:
                email = input('Digite o seu email: ')
            while not senha:
                senha = input('Crie sua senha: ')
            while not idd:
                idd = input('Digite a data do seu nascimento [DD/MM/AAAA]: ')
            while True:
                ocupacao = input('Qual sua ocupação: \n-\033[1m[1]\033[m Estudante \n-\033[1m[2]\033[m Profissional'
                                 ' \n-\033[1m[3]\033[m Professor(a) \n-\033[1m[4]\033[m Sem ocupação\n--> ')
                if int(ocupacao) =='1' or int(ocupacao) =='2' or int(ocupacao) =='3' or int(ocupacao) =='4':
                    print('Digite uma resposta válida.')
                else:
                    break
            arquivo = open('cadastro.csv', 'a')
            arquivo.write(f'{nome},{sobrenome},{email},{senha},{idd},{ocupacao}\n')
            arquivo.close()
            print('\033[0;34mParabéns, você concluiu seu cadastro!\033[m')
            break
        elif perfil == 'COMUNIDADE':
            nome = input('Digite o nome da comunidade: ')
            email = input('Digite o seu email: ')
            senha = input('Crie sua senha: ')
            arquivo = open('cadastro.csv', 'a')
            arquivo.write(f'{nome},{email},{senha}\n')
            arquivo.close()
            print('\033[0;34mParabéns, você concluiu o cadastro da comunidade!\033[m')
            break
        else:
            print('Digite uma resposta válida.')
            break

def feed_sim():
    print('\033[0;36m-\033[m'*40)
    print()
    print('\033[4;34mHome\033[m'.center(50))
    print()
    print('\033[0;36m-\033[m'*40)
    post()
    print('\033[0;36m-\033[m'*40)
    print()
    print()
    print('\033[4;34mPublicação\033[m'.center(50))
    print('\n\033[1;34m|\033[mCurtir\033[1;34m|\033[mComentar\033[1;34m|\033[mCompartilhar\033[1;34m|\033[mRepublicar\033[1;34m|\033[m')
    print('\033[0;36m-\033[m'*40)
    print()

def feed_nao():
    print('\033[0;36m-\033[m'*40)
    print()
    print('\033[4;34mHome\033[m'.center(50))
    print()
    print('\033[0;36m-\033[m'*40)
    post()
    print('\033[1m>Siga mais perfis para ver publicações<\033[m')
    print()
    print('\033[4;36mSugestões para seguir:\033[m')
    print('\033[0;34m*Perfis*\n*Perfis*\n*Perfis*\033[m')
    print()


def post():
    criacao = ''
    while criacao != 'SIM' and criacao != 'NAO':
        criacao = input('Deseja publicar algo? [Sim/Não]\n').strip().upper()
    if criacao == 'SIM':
        legenda = ''
        while not legenda:
            legenda = input('No que você está pensando?\n')
        arquivo = input('Deseja adicionar alguma mídia? [Sim/Não]\n').strip().upper()
        if arquivo == 'SIM':
            pub = f'\033[1;34m-->\033[m{legenda}\n\033[1;34m~\033[mMídia\033[1;34m~\033[m'
            print('\033[0;36m-\033[m' * 40)
            print()
            print(pub)
            print(
                '\n\033[1;34m|\033[mCurtir\033[1;34m|\033[mComentar\033[1;34m|\033[mCompartilhar\033[1;34m|\033[mRepublicar\033[1;34m|\033[m')
            print('\033[0;36m-\033[m' * 40)
        elif arquivo == 'NÃO' or arquivo == 'NAO':
            print('\033[0;36m-\033[m' * 40)
            print()
            pub = legenda
            print(f'\033[1;34m-->\033[m{pub}')
            print()
            print('\033[0;36m-\033[m' * 40)

def eventos():
    try:
        print('\033[4mEventos disponíveis:\033[m\n')
        print("\033[1m[1]\033[m-Recife,PE\n\033[1m[2]\033[m-Olinda,PE\n\033[1m[3]\033[m-Jaboatão dos Guararapes,PE\n"
              "\033[1m[4]\033[m-Caruaru,PE\n\033[1m[5]\033[m-Buenos Aires,PE")
        localizacao = int(input("-Qual sua localização? "))
        eventos_recife = ["Evento 1", "Evento 2", "Evento 3"]
        eventos_olinda = ["Evento 1", "Evento 2", "Evento 3"]
        eventos_jaboatao = ["Evento 1", "Evento 2", "Evento 3"]
        eventos_caruaru = ["Evento 1", "Evento 2", "Evento 3"]
        eventos_buenos_aires = ["Evento 1", "Evento 2", "Evento 3"]

        if localizacao == 1:
            print("\n\033[1;34mEventos em Recife,PE:\033[m")
            cont = 0
            for evento in eventos_recife:
                cont += 1
                print(f"\033[1m[{cont}]\033[m", evento)

        elif localizacao == 2:
            print("\n\033[1;34mEventos em Olinda,PE:\033[m")
            cont = 0
            for evento in eventos_olinda:
                cont += 1
                print(f"\033[1m[{cont}]\033[m", evento)

        elif localizacao == 3:
            print("\n\033[1;34mEventos em Jaboatão dos Guararapes,PE:\033[m")
            cont = 0
            for evento in eventos_jaboatao:
                cont += 1
                print(f"\033[1m[{cont}]\033[m", evento)

        elif localizacao == 4:
            print("\n\033[1;34mEventos em Caruaru,PE:\033[m")
            cont = 0
            for evento in eventos_caruaru:
                cont += 1
                print(f"\033[1m[{cont}]\033[m", evento)

        elif localizacao == 5:
            print("\n\033[1;34mEventos em Buenos Aires,PE:\033[m")
            cont = 0
            for evento in eventos_buenos_aires:
                cont += 1
                print(f"\033[1m[{cont}]\033[m", evento)

        else:
            print("Opção inválida!")

        escolha = int(input("Digite o número do evento escolhido: "))
        if localizacao == 1 and 1 <= escolha <= len(eventos_recife):
            evento_escolhido = eventos_recife[escolha - 1]
            print("Você escolheu o evento:", evento_escolhido)
            print('\033[0;36m-\033[m' * 40)
            print("\033[0;34m*INFORMAÇÕES DO EVENTO*\033[m".center(50))
            print('\033[0;36m-\033[m' * 40)

        elif localizacao == 2 and 1 <= escolha <= len(eventos_olinda):
            evento_escolhido = eventos_olinda[escolha - 1]
            print("Você escolheu o evento:", evento_escolhido)
            print('\033[0;36m-\033[m' * 40)
            print("\033[0;34m*INFORMAÇÕES DO EVENTO*\033[m".center(50))
            print('\033[0;36m-\033[m' * 40)

        elif localizacao == 3 and 1 <= escolha <= len(eventos_jaboatao):
            evento_escolhido = eventos_jaboatao[escolha - 1]
            print("Você escolheu o evento:", evento_escolhido)
            print('\033[0;36m-\033[m' * 40)
            print("\033[0;34m*INFORMAÇÕES DO EVENTO*\033[m".center(50))
            print('\033[0;36m-\033[m' * 40)

        elif localizacao == 4 and 1 <= escolha <= len(eventos_caruaru):
            evento_escolhido = eventos_caruaru[escolha - 1]
            print("Você escolheu o evento:", evento_escolhido)
            print('\033[0;36m-\033[m' * 40)
            print("\033[0;34m*INFORMAÇÕES DO EVENTO*\033[m".center(50))
            print('\033[0;36m-\033[m' * 40)

        elif localizacao == 5 and 1 <= escolha <= len(eventos_buenos_aires):
            evento_escolhido = eventos_buenos_aires[escolha - 1]
            print("Você escolheu o evento:", evento_escolhido)
            print('\033[0;36m-\033[m' * 40)
            print("\033[0;34m*INFORMAÇÕES DO EVENTO*\033[m".center(50))
            print('\033[0;36m-\033[m' * 40)

        else:
            print("Opção inválida!")
    except ValueError:
        print("Digite o número correspondente à sua localização.")

def carregar_dados():
    armazenar_dados = {}
    try:
        with open('comunidades.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            for linha in leitor:
                comunidade = linha[0]
                quantidade_pessoas = int(linha[1])
                membros = linha[2:] if len(linha) > 2 else []
                armazenar_dados[comunidade] = {
                    'Quantidade de Pessoas': quantidade_pessoas, 'Membros': membros}
        arquivo.close()
    except FileNotFoundError:
        pass
    return armazenar_dados

def salvar_dados(armazenar_dados):
    with open('comunidades.csv', 'w', newline='') as arquivo:
        escrita = csv.writer(arquivo)
        escrita.writerow(['Comunidade', 'Quantidade de Pessoas', 'Membros'])
        for comunidade, info in armazenar_dados.items():
            quantidade_pessoas = info['Quantidade de Pessoas']
            membros = info['Membros']
            escrita.writerow([comunidade, quantidade_pessoas] + membros)
    arquivo.close()


def exibir_menu(armazenar_dados):
    print('\n\033[1;34m-Comunidades:\033[m')
    linha = 1
    for comunidade in armazenar_dados:
        print(f'[{linha}] - {comunidade}')
        linha += 1
    print(f'\033[1m[{linha}]\033[m- Criar comunidade')
    print(f'\033[1m[{linha+1}]\033[m- Visualizar membros')


def visualizar_membros(armazenar_dados):
    comunidade_escolhida = int(input('Digite o número da comunidade: '))
    comunidades = list(armazenar_dados.keys())
    if 1 <= comunidade_escolhida <= len(comunidades):
        comunidade = comunidades[comunidade_escolhida - 1]
        membros = armazenar_dados[comunidade]['Membros']
        print(f'Membros da comunidade {comunidade}:')
        for membro in membros:
            print(membro)
    else:
        print('Número de comunidade inválido!')

def comunidade():
    armazenar_dados = carregar_dados()
    exibir_menu(armazenar_dados)

    opcao = int(input('Digite a opção desejada: '))
    if 1 <= opcao <= len(armazenar_dados):
        comunidades = list(armazenar_dados.keys())
        comunidade_escolhida = comunidades[opcao - 1]
        nome_pessoa = input('Digite o seu nome: ')
        print(
            f'{nome_pessoa}, você é um novo membro da comunidade {comunidade_escolhida}!')
        armazenar_dados[comunidade_escolhida]['Quantidade de Pessoas'] += 1
        armazenar_dados[comunidade_escolhida]['Membros'].append(nome_pessoa)
    elif opcao == len(armazenar_dados) + 1:
        nome_comunidade = input('Digite o nome da nova comunidade: ')
        if nome_comunidade not in armazenar_dados:
            armazenar_dados[nome_comunidade] = {'Quantidade de Pessoas': 1, 'Membros': []}
            print(f'Você é um novo membro da comunidade {nome_comunidade}!')
        else:
            print(f'A comunidade {nome_comunidade} já existe!')
    elif opcao == len(armazenar_dados) + 2:
        visualizar_membros(armazenar_dados)
    else:
        print('Opção inválida!')

    salvar_dados(armazenar_dados)


inicio()

