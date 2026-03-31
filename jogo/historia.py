from funcoes import calcular_vida, curar, esta_vivo, upar_nivel

vida = 20
nivel = 1
itensRaros = 0
pocaoCura = 0
pocaoCuraGrande = 0

nomePersonagem = input("Digite o nome da sua personagem: ")

print(f"\n Olá {nomePersonagem}! Seja bem-vindo(a) à nossa mini jornada Heroica! É bom que você esteja preparado!\nVocê tem {vida} de vida\nVocê está no nível {nivel}")
print("")
print("")


def entrada_valida(texto, opcoes):
    while True:
        try:
            escolha = int(input(texto))
            if escolha in opcoes:
                return escolha
            print(f"Opção inválida. Digite {', '.join(map(str, opcoes))}.")
        except:
            print("Digite um número válido.")


escolha1 = entrada_valida(
    "Você deseja adentrar-se na Ruína? \n1-SIM \n2-NÃO \n", [1, 2]
)

if escolha1 == 2:
    print("Você saiu antes do game começar!")

elif escolha1 == 1:
    escolha2 = entrada_valida(
        "\n Muito bem! Você é um(a) aventureira(o) bem corajoso(a)! \nAssim que você entra na Ruína é possível ver uma poção de cura, deseja pegá-la? \n1-SIM \n2-NÃO \n",
        [1, 2],
    )

    if escolha2 == 1:
        pocaoCura += 1
        print(f"\n Poção coletada com sucesso! Você possui {pocaoCura} poção de cura.")

    print("")

    escolha3 = entrada_valida(
        "\nVocê continua andando pela Ruína e se depara com uma Múmia, deseja enfrentá-la? \n1-SIM \n2-Tentar passar escondido \n3-Fugir da Ruína \n",
        [1, 2, 3],
    )

    if escolha3 == 1:
        print(f"\nVocê vai pra cima da Múmia e acaba pegando ela de surpresa, você consegue acertar um ataque nela, mas antes de matá-la, a Múmia acaba mordendo seu braço, causando 5 de dano.")
        vida = calcular_vida(vida, 5)

        if not esta_vivo(vida):
            print("\nVocê morreu")
            exit()

        print(f"\n Você está com {vida} de vida")

    elif escolha3 == 2:
        print("\n Você tenta passar por uma parte mais escura e afastada da Múmia, mas ela pega vc de surpresa. Vocês lutam bastante, mas antes de você conseguir matar a múmia, ela te morde e te arranha.\nVocê toma 10 de dano.")
        vida = calcular_vida(vida, 10)

        if not esta_vivo(vida):
            print("\nVocê morreu")
            exit()

        print(f"\nVocê está com {vida} de vida")

    elif escolha3 == 3:
        print("\nSe não quisesse jogar era melhor nem ter entrado nas Ruínas.")
        exit()

    if pocaoCura > 0:
        escolha4 = entrada_valida(
            "\nVocê possui uma poção de cura, deseja usar? \n1-SIM \n2-NÃO\n",
            [1, 2],
        )

        if escolha4 == 1:
            vida = curar(vida, 5)
            pocaoCura -= 1
            print(f"\nAgora você está com {vida} de vida")

    print("")
    nivel, vida = upar_nivel(nivel, vida)
    print(f"Parabéns, você upou de nível! Agora você é nível {nivel} e está com {vida} de vida.")
    print("")

    escolha5 = entrada_valida(
        "\nApós derrotar a Múmia, você encontra dois caminhos.\n1-Seguir pelo corredor da esquerda\n2-Seguir pelo corredor da direita\n3-Voltar e sair\n",
        [1, 2, 3],
    )

    if escolha5 == 1:
        print("\nVocê segue pelo corredor da esquerda e encontra uma sala antiga com um baú empoeirado no centro.")

        escolha6 = entrada_valida("\nDeseja abrir o baú?\n1-SIM\n2-NÃO\n", [1, 2])

        if escolha6 == 1:
            print("\nVocê abre o baú e encontra um Amuleto Fantasmagórico, um item raro envolto em energia azul, além de uma poção de cura grande.")
            itensRaros += 1
            pocaoCuraGrande += 1
            print(f"Agora você possui {itensRaros} item raro.")
            print(f"Agora você possui {pocaoCuraGrande} poção de cura grande.")

            escolhaPocao = entrada_valida(
                "Você deseja usar a poção de cura grande agora? \n1-SIM\n2-NÃO\n",
                [1, 2],
            )

            if escolhaPocao == 1:
                vida = curar(vida, 10)
                pocaoCuraGrande -= 1
                print(f"Agora você está com {vida} de vida.")

        else:
            print("Você esqueceu de pensar e seguiu sem abrir o baú da Ruína.")

    elif escolha5 == 2:
        print("Você segue pelo corredor da direita, mas pisa em uma armadilha escondida. Lâminas surgem da parede e atingem você.")
        vida = calcular_vida(vida, 4)

        if not esta_vivo(vida):
            print("Você morreu")
            exit()

        print(f"Você sobreviveu à armadilha e agora está com {vida} de vida.")

    elif escolha5 == 3:
        print("Você volta e sai da Ruína, perdendo uma grande aventura.")
        exit()

    print("")
    print("Depois de avançar mais um pouco, você chega ao salão principal da Ruína. \nNo centro do salão surge o Guardião Fantasma, protegendo a relíquia mais valiosa do lugar.")
    print("")

    escolha7 = entrada_valida(
        "O que você deseja fazer?\n1-Enfrentar o Guardião Fantasma\n2-Tentar conversar com ele\n3-Fugir\n",
        [1, 2, 3],
    )

    if escolha7 == 1:
        if itensRaros > 0:
            print("O Amuleto Fantasmagórico começa a brilhar e enfraquece o Guardião. \nVocê trava uma batalha intensa, mas consegue vencê-lo tomando apenas 4 de dano.")
            vida = calcular_vida(vida, 4)
        else:
            print("Sem nenhum item raro para ajudá-lo, o Guardião Fantasma mostra toda sua força. \nVocê consegue vencê-lo por pouco, mas sofre 14 de dano.")
            vida = calcular_vida(vida, 14)

        if not esta_vivo(vida):
            print("Você morreu")
            exit()

        print(f"Depois da batalha, você ficou com {vida} de vida.")

    elif escolha7 == 2:
        if itensRaros > 0:
            print("Ao ver o Amuleto Fantasmagórico em suas mãos, o Guardião reconhece sua coragem. \nEle se ajoelha diante de você e permite sua passagem sem lutar.")
        else:
            print("O Guardião não acredita em suas palavras e ataca você com uma rajada espiritual.")
            vida = calcular_vida(vida, 6)

            if not esta_vivo(vida):
                print("Você morreu")
                exit()

            print(f"Você sobreviveu ao ataque e está com {vida} de vida.")

    elif escolha7 == 3:
        print("Você foge da batalha final e abandona a Ruína sem descobrir seus segredos.")
        exit()

    print("")
    nivel, vida = upar_nivel(nivel, vida)
    
    print(f"Parabéns, você upou de nível novamente! Agora você é nível {nivel} e está com {vida} de vida.")
    print("")

    print("Com o Guardião derrotado ou convencido, você alcança o altar central da Ruína.\nSobre ele repousa a Relíquia Espectral, envolvida por uma névoa brilhante.")
    print("")
    
    print(f"Parabéns, {nomePersonagem}! Você concluiu a aventura da Ruína Fantasmagórica!")
    
    print(f"Status final:\nVida: {vida}\nNível: {nivel}\nItens raros: {itensRaros}\nPoções de cura: {pocaoCura}\nPoções de cura grande: {pocaoCuraGrande}")