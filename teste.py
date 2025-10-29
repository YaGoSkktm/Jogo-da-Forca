import random
import PerguntasShowDoMilhão
#lista de premios e variaveis
premios = [1000,2000,3000,4000,5000,
           10000,20000,30000,40000,50000,
           100000,200000,300000,400000,500000,1000000]
pulos = 3
ajudas = 3
ajuda_universitarios = 1
ajuda_garantida = 1
ajuda_eliminar = 1
valor_acumulado = 0
contador_perguntas = 0


# randomizador de perguntas e opções
while True:
    pergunta = random.choice(PerguntasShowDoMilhão.perguntasMilhão)
    print('-='*20)
    print(pergunta['pergunta'])

    for opcao in pergunta['opcoes']:
        print(opcao)

    #Perguntas, sistema de ajuda e pulos
    try:
        print('Você pode digitar PULAR para pular ou AJUDA para o mesmo')
        resposta_usuario = str(input('Digite Sua opção: ')).strip().upper()

        if resposta_usuario == 'PULAR' and pulos > 0:
            pulos -= 1
            continue

        elif resposta_usuario == 'AJUDA' and ajudas > 0:
            ajudas -= 1
            print('''-=-=-=-=-=-=-=-=-=-=
[1] ACERTO GARANTIDO
[2] UNIVERSITÁRIOS
[3] ELIMINAR DUAS ALTERNATIVAS
-=-=-=-=-=-=-=-=-=-=''')
            opcao = int(input('Qual você vai escolher? '))


            #primeiro tipo ajuda
            if opcao == 1 and ajuda_garantida == 1:
                ajuda_garantida -= 1
                print(f'A resposta é {pergunta["resposta"]}')
                resposta_usuario = str(input('Digite sua opcão: '))
            else:
                print('você não tem mais esse tipo de ajuda')


            #segundo tipo de ajuda
            if opcao == 2 and ajuda_universitarios == 1:
                ajuda_universitarios -= 1
                for i in range(0, 3):
                    ChanceAcerto = random.randint(1,100)

                    if ChanceAcerto <= 70:
                        resposta = pergunta['resposta']

                    else:
                        opcoes_erradas = ["1", "2", "3", "4"]
                        opcoes_erradas.remove(pergunta['resposta'])
                        resposta = random.choice(opcoes_erradas)
                    print(f'O universitário {i} acha que a resposta é: {resposta}')
                resposta_usuario = str(input('Digite Sua opção: ')).strip().upper()
            else:
                print('você não tem mais esse tipo de ajuda')


            #terceiro tipo de ajuda
            if opcao == 3 and ajuda_eliminar == 1:
                ajuda_eliminar -= 1
                erradas = [opcoes for opcoes in pergunta['opcoes'] if pergunta['resposta'] not in opcoes]
                eliminar = random.sample(erradas, 2)
                print("Eliminando alternativas:")
                for e in eliminar:
                    print(e)
                    pergunta['opcoes'].remove(e)
            else:
                print('você não tem mais esse tipo de ajuda')
            print("\nOpções restantes:")
            for opcoes in pergunta['opcoes']:
                print(opcoes)


            if opcao < 1 or opcao > 3:
                while True:
                    print('Escolha uma opcão válida')

                    opcao = int(input('Qual opção você vai escolher? '))
                    # primeiro tipo ajuda
                    if opcao == 1 and ajudas > 0:
                        if opcao == 1 and ajuda_garantida == 1:
                            ajuda_garantida -= 1
                            print(f'A resposta é {pergunta['resposta']}')
                            resposta_usuario = str(input('Digite sua opcão: '))
                        else:
                            print('você não tem mais esse tipo de ajuda')
                            continue
                    else:
                        print('Você não tem mais ajudas')
                        break


                    # segundo tipo de ajuda
                    if opcao == 2 and ajudas > 0:
                        if opcao == 2 and ajuda_universitarios == 1:
                            ajuda_universitarios -= 1
                            for i in range(0, 3):
                                ChanceAcerto = random.randint(1, 100)
                                if ChanceAcerto <= 70:
                                    resposta = pergunta['resposta']
                                else:
                                    opcoes_erradas = ["1", "2", "3", "4"]
                                    opcoes_erradas.remove(pergunta['resposta'])
                                    resposta = random.choice(opcoes_erradas)
                                print(f'O universitário {i} acha que a resposta é: {resposta}')
                            resposta_usuario = str(input('Digite Sua opção: ')).strip().upper()
                        else:
                            print('você não tem mais esse tipo de ajuda')
                            continue
                    else:
                        print('Você não tem mais ajudas')
                        break


                    if opcao == 3 and ajudas > 0:
                        if opcao == 3 and ajuda_eliminar == 1:
                            ajuda_eliminar -= 1
                            erradas = [opcoes for opcoes in pergunta['opcoes'] if pergunta['resposta'] not in opcoes]
                            eliminar = random.sample(erradas, 2)
                            print("Eliminando alternativas:")
                            for e in eliminar:
                                print(e)
                                pergunta['opcoes'].remove(e)
                        else:
                            print('você não tem mais esse tipo de ajuda')
                            continue
                    else:
                        print('Você não tem mais ajudas')
                        break


        elif resposta_usuario == 'PULAR' and pulos <=0:
            while True:
                print('Você não possui mais pulos;')
                resposta_usuario = str(input('Digite sua opção: ')).strip().upper()
                if resposta_usuario == 'PULAR':
                    continue
                elif resposta_usuario == 'AJUDA' and ajudas > 3:
                    print('-----')
                else:
                    break
        elif resposta_usuario == 'AJUDA' and ajudas <= 0:
            while True:
                print('Você não possui mais ajudas.')
                resposta_usuario = str(input('Digite sua opção: ')).strip().upper()
                if resposta_usuario == 'AJUDA':
                    continue
                elif resposta_usuario == 'PULAR' and pulos > 0:
                    pulos -= 1
                    break
                else:
                    break

    except:
        print('Houve um erro, tente novamente')
        continue
    if str(resposta_usuario) == str(pergunta['resposta']):
        print('Parabéns, você acertou!')
        contador_perguntas += 1

        PerguntasShowDoMilhão.perguntasMilhão.remove(pergunta)

        if contador_perguntas <= len(premios):
            valor_acumulado = premios[contador_perguntas - 1]
        else:
            valor_acumulado = premios[-1]

        print(f'O seu dinheiro atual é R$ {valor_acumulado:,}'.replace(',', '.'))

        if contador_perguntas == len(premios):
            print('Parabéns, você acertou todas as perguntas!!')
            break
    else:
        print(f'Você errou seu premio foi de: R${valor_acumulado:,}'.replace(',','.'))
        break



