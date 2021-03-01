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
                        print("{} foi cadastrado(a) com sucesso!".format(p_cadastrado))
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
                        print("A sala foi cadastrada com sucesso!")
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
                        print("O espaço foi cadastrado com sucesso!".format(c_cadastrado))
                    print("É possível cadastrar somente dois espaços para café.\n")
                elif dircad == str(4):  # Para voltar ao menu inicial
                    break
                else:  # Corrige número digitado errado
                    print("Você precisa digitar 1, 2, 3 ou 4!\n")

        participantes_pc = participantes[:]
        salast1_pc = deepcopy(salast1)
        cafes_pc = deepcopy(cafes)

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

                while participantes_pc:
                    for sala in salast1_pc:
                        for b in range(0, 1):
                            if not participantes_pc:
                                break
                            else:
                                sala.append(participantes_pc[0])
                                del participantes_pc[0]

                salast2 = deepcopy(salast1_pc)

                # Fim
                # Organização da sala no segundo tempo
                
                if n_salast1 >= 2:
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
                    for i in cafes_pc:
                        for k in range(0, 1):
                            if not participantes_c:
                                break
                            else:
                                i.append(participantes_c[0])
                                del participantes_c[0]

                # Fim
                # Fim das funções de consulta

                while True:
                    dircon = funcoes.menu_consulta()  # Menu de consulta
                    if dircon == str(1):  # Consulta de participante
                        consulta_nome = input("Digite o nome completo "
                                              "do participante que você deseja consultar, inserindo um espaço"
                                              " em branco entre os nomes:\n").upper()
                        for x in salast1_pc:
                            if consulta_nome in x:
                                print("Na primeira etapa, {} estará na sala {}.".format(consulta_nome, x[0]))
                        for y in salast2:
                            if consulta_nome in y:
                                print("Na segunda etapa, {} estará na sala {}.".format(consulta_nome, y[0]))
                        for z in cafes_pc:
                            if consulta_nome in z:
                                print("{} fará seus cafés no espaço {}.\n".format(consulta_nome, z[0]))

                    elif dircon == str(2):  # Consulta de sala
                        consulta_sala = input("Digite o nome da sala que você deseja consultar:\n").upper()
                        salast1_pcc = deepcopy(salast1_pc)
                        salast2_pcc = deepcopy(salast2)
                        for w in salast1_pcc:
                            if consulta_sala in w:
                                del w[0:2]
                                w = '\n '.join(w)
                                print("Na primeira etapa, a sala {} estará com "
                                      "os seguintes participantes:\n {}".format(consulta_sala, w))
                        for ww in salast2_pcc:
                            if consulta_sala in ww:
                                del ww[0:2]
                                ww = '\n '.join(ww)
                                print("Na segunda etapa, a sala {} estará com "
                                      "os seguintes participantes:\n {}\n".format(consulta_sala, ww))

                    elif dircon == str(3):  # Consulta de espaço para café
                        consulta_cafe = input("Digite o nome do café que você deseja consultar:\n").upper()
                        cafes_pcc = deepcopy(cafes_pc)
                        for z in cafes_pcc:
                            if consulta_cafe in z:
                                del z[0]
                                z = '\n '.join(z)
                                print("O espaço {} terá os seguintes participantes:\n {}\n".format(consulta_cafe, z))

                    if dircon == str(4):  # Lista de todos cadastros realizados
                        plcr = participantes[:]
                        s1lcr = deepcopy(salast1_pc)
                        s2lcr = deepcopy(salast2)
                        clcr = deepcopy(cafes_pc)
                        plcr = '\n'.join(plcr)
                        print("Participantes:\n{}\n".format(plcr))
                        print("Salas do primeiro período com seus respectivos participantes:")
                        for aaa in s1lcr:
                            print("{}: ".format(aaa[0]))
                            del aaa[0:2]
                            aaa = '\n'.join(aaa)
                            print("{}\n".format(aaa))
                        print("Salas do segundo período com seus respectivos participantes:")
                        for bbb in s2lcr:
                            print("{}: ".format(bbb[0]))
                            del bbb[0:2]
                            bbb = '\n'.join(bbb)
                            print("{}\n".format(bbb))
                        print("Ambientes de coffe break com seus respectivos participantes:")
                        for ccc in clcr:
                            print("{}: ".format(ccc[0]))
                            del ccc[0]
                            ccc = '\n'.join(ccc)
                            print("{}\n".format(ccc))

                    elif dircon == str(5):  # Volta ao menu inicial
                        break

                    else:  # Corrige número digitado errado
                        print("Você precisa digitar 1, 2, 3, 4 ou 5!\n")

        if direcao == str(3):  # Encerrar programa
            break


if __name__ == "__main__":
    inicia_programa()
