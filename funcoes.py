# Funções do menu inicial ---------------------------------------------------------------------------------------------

def imprimir_mensagem_inicial():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('-=-=-=-=-=ORGANIZADOR DE TREINAMENTOS=-=-=-=-=-')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()


def escolher_cadastro_ou_consulta():
    print("O que você quer fazer?")
    r = input("(1) Cadastro \n(2) Consulta \n(3) Encerrar o programa \n")
    return r

# Funções do menu de cadastros ----------------------------------------------------------------------------------------


def menu_cadastro():
    print("O que você quer cadastrar?")
    r = input("(1) Participantes \n(2) Salas \n(3) Espaços para café \n(4) Voltar para o menu inicial \n")
    return r


def cad_participantes():
    p_nome = input("Escreva apenas o primeiro nome do aluno: \n").upper()
    sobrenome = (input("Agora insira somente o sobrenome dele: \n").upper())
    espaco = ' '
    p_cadastrado = p_nome + espaco + sobrenome
    return p_cadastrado


def cad_salas():
    sala = input("Escreva o nome da sala: \n").upper().split()
    lotacao_s = (input("Agora escreva a lotação da sala: \n")).split()
    salac = sala + lotacao_s
    return salac


def continuar_cadastrando():
    resp = input("Continuar cadastrando nessa categoria? (s) para sim, (n) para não.\n").upper()
    return resp


def cad_cafes():
    cafe = (input("Escreva o nome do espaço de coffee break: \n").upper().split())
    return cafe

# Funções do menu de consulta ----------------------------------------------------------------------------------------


def menu_consulta():
    print("O que você quer consultar?")
    r = input("(1) Participantes \n(2) Salas \n(3) Espaços para café \n(4) Voltar para o menu inicial \n")
    return r
