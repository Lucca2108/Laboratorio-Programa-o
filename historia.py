from combate import combate, criar_mumia, criar_guardiao_fantasma, criar_esqueleto
from funcoes import curar


def linha():
    print("─" * 42)


def titulo(texto):
    linha()
    print(f"  {texto}")
    linha()


def escolher(pergunta, opcoes):
    print(pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"  [{i}] {opcao}")
    while True:
        entrada = input("> ").strip()
        if entrada.isdigit():
            entrada = int(entrada)
            if 1 <= entrada <= len(opcoes):
                return opcoes[entrada - 1]
        print("  Escolha inválida. Tente de novo.")


def pausar():
    input("\n  [ENTER para continuar...]\n")


def iniciar_historia(heroi):
    inventario = {
        "pocao_cura": 0,
        "pocao_cura_grande": 0,
        "amuleto_fantasmagorico": False
    }
    pontuacao = 0

    titulo("A RUÍNA FANTASMAGÓRICA")
    print(f"""
  Uma névoa espessa envolve as antigas ruínas de Valdrim.
  Aventureiros desapareceram ao entrar nelas.
  Ninguém voltou para contar o que há lá dentro.

  {heroi.nome}, você veio descobrir a verdade.
    """)
    pausar()

    titulo("A ENTRADA")
    print("""
  Diante de você há três caminhos:
  uma porta de pedra coberta de musgo,
  uma janela quebrada no lado esquerdo,
  e uma passagem oculta atrás de uma pedra solta.
    """)

    caminho = escolher("  Por onde você entra?", [
        "Porta de pedra",
        "Janela quebrada",
        "Passagem oculta"
    ])

    if caminho == "Porta de pedra":
        print("""
  Você empurra a porta pesada. Ela abre com um estrondo.
  Uma armadilha de pedras cai sobre você!
        """)
        heroi.sofrer_dano(8)
        print(f"  Você sofreu 8 de dano! ({heroi.vida} PV restantes)")
    elif caminho == "Janela quebrada":
        print("""
  Você se esgueira pela janela com cuidado.
  Sem barulho. Sem problemas.
        """)
    else:
        print("""
  A passagem oculta te leva por um corredor secreto.
  Você encontra uma poção esquecida no chão!
        """)
        inventario["pocao_cura"] += 1
        pontuacao += 50
        print("  +1 Poção de Cura adicionada! (+50 pontos)")

    pausar()

    if not heroi.vivo():
        print(f"\n  {heroi.nome} foi esmagado pela armadilha. Fim.\n")
        return pontuacao, inventario

    titulo("O PRIMEIRO ANDAR")
    print("""
  O corredor está frio e silencioso.
  Tochas apagadas nas paredes. O cheiro de terra úmida.
  Ao fundo, dois caminhos se bifurcam.
    """)

    escolha1 = escolher("  Qual direção você segue?", [
        "Corredor da esquerda (parece mais escuro)",
        "Corredor da direita (tem luz fraca)"
    ])

    if escolha1 == "Corredor da esquerda (parece mais escuro)":
        titulo("EMBOSCADA!")
        print("""
  Das sombras surge uma Múmia!
  Suas bandagens estão ensanguentadas e seus olhos brilham.
        """)
        pausar()
        mumia = criar_mumia()
        venceu = combate(heroi, mumia)
        if not venceu:
            print(f"\n  {heroi.nome} foi derrotado pela Múmia. Fim.\n")
            return pontuacao, inventario
        pontuacao += 100
        print("  Você venceu a Múmia! (+100 pontos)")
        abrir = escolher("  Você encontra um baú. O que faz?", [
            "Abro o baú",
            "Ignoro e sigo em frente"
        ])
        if abrir == "Abro o baú":
            inventario["pocao_cura_grande"] += 1
            pontuacao += 50
            print("  +1 Poção de Cura Grande! (+50 pontos)")
    else:
        titulo("O CORREDOR DA LUZ")
        print("""
  Uma câmara iluminada. No centro, um altar com uma poção brilhante.
        """)
        pegar = escolher("  O que você faz?", [
            "Pego a poção do altar",
            "Desconfio e não toco"
        ])
        if pegar == "Pego a poção do altar":
            inventario["pocao_cura"] += 1
            pontuacao += 50
            print("  +1 Poção de Cura! (+50 pontos)")
        else:
            print("""
  Sábia decisão. O altar afundou — era uma armadilha.
            """)

    pausar()

    titulo("O SEGUNDO ANDAR")
    pausar()

    titulo("EMBOSCADA: ESQUELETO!")
    print("""
  Um Esqueleto Guerreiro surge brandindo uma lança enferrujada.
    """)
    pausar()
    esqueleto = criar_esqueleto()
    venceu = combate(heroi, esqueleto)
    if not venceu:
        print(f"\n  {heroi.nome} foi derrotado pelo Esqueleto. Fim.\n")
        return pontuacao, inventario
    pontuacao += 100
    print("  Você venceu o Esqueleto! (+100 pontos)")

    heroi.subir_nivel()
    pontuacao += 75
    print("  Você subiu de nível! (+75 pontos)")
    pausar()

    titulo("A CÂMARA DO AMULETO")
    print("""
  No pedestal central repousa o Amuleto Fantasmagórico,
  brilhando com uma luz espectral azul-esverdeada.
    """)

    pegar_amuleto = escolher("  O que você faz?", [
        "Pego o Amuleto Fantasmagórico",
        "Deixo o amuleto e sigo"
    ])

    if pegar_amuleto == "Pego o Amuleto Fantasmagórico":
        inventario["amuleto_fantasmagorico"] = True
        pontuacao += 50
        print("  +Amuleto Fantasmagórico equipado! (+50 pontos)")
    else:
        print("  Você deixa o amuleto para trás.")

    pausar()

    if inventario["pocao_cura"] > 0 or inventario["pocao_cura_grande"] > 0:
        titulo("ANTES DO CONFRONTO FINAL")
        print(f"  {heroi.nome} está com {heroi.vida} PV.")
        opcoes_pocao = []
        if inventario["pocao_cura"] > 0:
            opcoes_pocao.append("Usar Poção de Cura (recupera 20 PV)")
        if inventario["pocao_cura_grande"] > 0:
            opcoes_pocao.append("Usar Poção de Cura Grande (recupera 40 PV)")
        opcoes_pocao.append("Não usar nada")

        usar = escolher("  Usar alguma poção?", opcoes_pocao)
        if usar == "Usar Poção de Cura (recupera 20 PV)":
            heroi.vida = curar(heroi.vida, 20)
            inventario["pocao_cura"] -= 1
            print(f"  ({heroi.vida} PV)")
        elif usar == "Usar Poção de Cura Grande (recupera 40 PV)":
            heroi.vida = curar(heroi.vida, 40)
            inventario["pocao_cura_grande"] -= 1
            print(f"  ({heroi.vida} PV)")
        pausar()

    titulo("O GUARDIÃO FANTASMA")
    print(f"""
  Uma figura translúcida se materializa.
  "Nenhum mortal sai daqui vivo."

  {heroi.nome} ergue sua arma. A batalha final começa.
    """)
    pausar()

    guardiao = criar_guardiao_fantasma()

    if inventario["amuleto_fantasmagorico"]:
        print("""
  O Amuleto brilha! O Guardião está enfraquecido — perde 15 PV!
        """)
        guardiao.sofrer_dano(15)

    venceu = combate(heroi, guardiao)

    if venceu:
        pontuacao += 200
        pontuacao += heroi.vida * 2
        titulo("VITÓRIA!")
        print(f"""
  O Guardião se dissolve em névoa. A ruína desmorona.

  {heroi.nome} escapou! PV restantes: {heroi.vida}
  Pontuação final: {pontuacao}
        """)
        if inventario["amuleto_fantasmagorico"]:
            print("  O amuleto pulsa. Algo mudou em você para sempre.")
    else:
        titulo("DERROTA")
        print(f"""
  {heroi.nome} caiu diante do Guardião Fantasma.
  Pontuação final: {pontuacao}
        """)

    return pontuacao, inventario