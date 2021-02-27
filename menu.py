from copy import deepcopy
import funcoes

salast1 = []
participantes = []
cafes = []


def inicia_programa():
    funcoes.imprimir_mensagem_inicial()  # Imprime abertura
    while True:
        direcao = funcoes.escolher_cadastro_ou_consulta()  # Menu inicial
        if direcao == str(1):
            while True:
                dircad = funcoes.menu_cadastro()  # Menu de cadastro
                if dircad == str(1):  # Cadastro dos participantes
                    while True:
                        p_cadastrado = funcoes.cad_participantes()
                        participantes.append(p_cadastrado)
                        print("{} foi cadastrado(a) com sucesso!\n".format(p_cadastrado))
                        while True:
                            m_cadastros = funcoes.continuar_cadastrando()
                            if m_cadastros == str("S"):
                                break
                            elif m_cadastros == str("N"):
                                break
                            else:
                                print("Você deve digitar (S) para sim, ou (S) não.")
                                pass
                        if m_cadastros == str("S"):
                            pass
                        elif m_cadastros != str("S"):
                            break
                elif dircad == str(2):  # Cadastro das salas
                    while True:
                        s_cadastrada = funcoes.cad_salas()
                        salast1.append(s_cadastrada)
                        print("A sala {} foi cadastrada com sucesso!\n".format(s_cadastrada))
                        while True:
                            m_cadastros = funcoes.continuar_cadastrando()
                            if m_cadastros == str("S"):
                                break
                            elif m_cadastros == str("N"):
                                break
                            else:
                                print("Você deve digitar (S) para sim, ou (S) não.")
                                pass
                        if m_cadastros == str("S"):
                            pass
                        elif m_cadastros != str("S"):
                            break
                elif dircad == str(3):  # Cadastro dos espaços de cafés
                    cafes_disp = 1
                    while cafes_disp >= 0:
                        c_cadastrado = funcoes.cad_cafes()
                        cafes.append(c_cadastrado)
                        cafes_disp -= 1
                        print(cafes)
                        print("O espaço {} foi cadastrado com sucesso!\n".format(c_cadastrado))
                    print("É possível cadastrar somente dois espaços para café.")
                elif dircad == str(4):  # Para voltar ao menu inicial
                    break

        if direcao == str(2):
            if not participantes or not salast1 or not cafes:
                print("Antes de fazer consutas, você precisa as cadastrar salas, os participantes e os cafés.")
                pass
            else:
                # Funções de consulta - começo ------------------------------------------------------------------------

                participantesgeral = participantes[:]
                participantes_c = participantes[:]
                n_participantes = len(participantes)
                n_salast1 = len(salast1)
                n_trocados = (n_participantes / n_salast1) / 2
                n_trocados = round(n_trocados)

                # Organização da sala no primeiro tempo

                while participantes:
                    for sala in salast1:
                        for b in range(0, 1):
                            if not participantes:
                                break
                            else:
                                sala.append(participantes[0])
                                del participantes[0]

                salast2 = deepcopy(salast1)

                # Fim
                # Organização da sala no segundo tempo

                for i in range(0, n_trocados):
                    for sala in salast2:
                        if participantesgeral[0] not in sala:
                            sala.append(participantesgeral[0])
                            del participantesgeral[0]
                        elif participantesgeral[1] not in sala:
                            sala.append(participantesgeral[1])
                            del participantesgeral[1]
                    for sala in salast2:
                        del sala[2]

                # Fim
                # Organização dos espaços de café

                while participantes_c:
                    for i in cafes:
                        for k in range(0, 1):
                            if not participantes_c:
                                break
                            else:
                                i.append(participantes_c[0])
                                del participantes_c[0]

                while True:
                    dircon = funcoes.menu_consulta()  # Menu de consulta
                    if dircon == str(1):  # Consulta de participante
                        consulta_nome = input("Digite o nome completo "
                                              "do participante que você quer consultar:\n").upper()
                        for x in salast1:
                            if consulta_nome in x:
                                print("Na primeira etapa, {} estará na sala {}.".format(consulta_nome, x[0]))
                        for y in salast2:
                            if consulta_nome in y:
                                print("Na segunda etapa, {} estará na sala {}.".format(consulta_nome, y[0]))
                        for z in cafes:
                            if consulta_nome in z:
                                print("{} fará seus cafés no espaço {}.\n".format(consulta_nome, z[0]))

                    if dircon == str(2):  # Consulta de sala
                        consulta_sala = input("Digite o nome da sala que você quer consultar:\n").upper()
                        for w in salast1:
                            if consulta_sala in w:
                                print("Na primeira etapa, a sala {} estará com "
                                      "os seguintes participantes:\n {}".format(consulta_sala, w[2:]))
                        for ww in salast2:
                            if consulta_sala in ww:
                                print("Na segunda etapa, a sala {} estará com "
                                      "os seguintes participantes:\n {}\n".format(consulta_sala, ww[2:]))

                    if dircon == str(3):  # Consulta de espaço para café
                        print("Os cafés cadastrados são:\n{}\n".format(cafes))
                    if dircon == str(4):  # Para voltar ao menu inicial
                        break

        if direcao == str(3):
            break


if __name__ == "__main__":
    inicia_programa()
