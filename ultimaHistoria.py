from dados import atacar, ataque_mago
from funcoes import calcular_vida, curar, esta_vivo, upar_nivel
from classes import Mago, Arqueiro, Cavaleiro, Personagem
import time

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


def criar_personagem():
    titulo("CRIAÇÃO DO PERSONAGEM")

    nome = ""
    while not nome:
        nome = input("  Qual é o nome do seu personagem?\n> ").strip()
        if not nome:
            print("  O nome não pode estar vazio.")

    classe = escolher("\n  Escolha sua classe:", ["Mago", "Arqueiro", "Cavaleiro"])

    if classe == "Mago":
        magias_disponiveis = [
            "Bola de Fogo",
            "Raio de Gelo",
            "Relâmpago",
            "Cura Arcana",
            "Escudo Mágico"
        ]

        print("\n  Escolha 3 magias para o seu grimório:")
        magias_escolhidas = []

        while len(magias_escolhidas) < 3:
            magia = escolher(
                f"  Escolha a magia {len(magias_escolhidas) + 1}:",
                magias_disponiveis
            )
            magias_escolhidas.append(magia)
            magias_disponiveis.remove(magia)
            print(f"  ✓ {magia} adicionada!")

        personagem = Mago(nome)
        personagem.magias = magias_escolhidas

    elif classe == "Arqueiro":
        personagem = Arqueiro(nome)

    else:
        arma = escolher("\n  Escolha sua arma:", ["Espada", "Machado"])
        personagem = Cavaleiro(nome, arma=arma.lower())

    print(f"\n  {personagem.nome} está pronto para a aventura!")
    pausar()
    return personagem


def turno_mago(heroi, inimigo):
    acao = escolher("\n  O que você faz?", heroi.magias + ["Ataque básico"])

    if acao == "Ataque básico":
        heroi.atacar_inimigo(inimigo)

    elif acao == "Cura Arcana":
        cura = 15
        heroi.vida = curar(heroi.vida, cura)
        print(f"  {heroi.nome} usou Cura Arcana e recuperou {cura} PV! ({heroi.vida} PV)")

    elif acao == "Escudo Mágico":
        heroi._escudo_ativo = True
        print(f"  {heroi.nome} ativou Escudo Mágico!")

    else:
        dano = ataque_mago(acao)
        inimigo.sofrer_dano(dano)
        print(f"  {heroi.nome} usou {acao} e causou {dano} de dano!")


def turno_inimigo(heroi, inimigo):
    dano = atacar(inimigo.classe.lower(), inimigo.modificador_ataque, heroi.ca)

    if dano <= 0:
        print(f"  {inimigo.nome} errou o ataque!")
        return

    if getattr(heroi, "_escudo_ativo", False):
        dano = max(1, dano // 2)
        heroi._escudo_ativo = False
        print(f"  O Escudo Mágico reduziu o dano para {dano}!")

    heroi.sofrer_dano(dano)
    print(f"  {inimigo.nome} atacou {heroi.nome} e causou {dano} de dano! ({heroi.vida} PV restantes)")


def combate(heroi, inimigo):
    titulo(f"COMBATE: {heroi.nome} vs {inimigo.nome}")
    rodada = 1

    while esta_vivo(heroi.vida) and esta_vivo(inimigo.vida):
        print(f"\n  Rodada {rodada}")
        print(f"  {heroi.nome}: {heroi.vida} PV  |  {inimigo.nome}: {inimigo.vida} PV")
        linha()

        if heroi.classe.lower() == "mago":
            acao = escolher("  O que você faz?", heroi.magias + ["Ataque básico"])

            if acao == "Ataque básico":
                heroi.atacar_inimigo(inimigo)

            elif acao == "Cura Arcana":
                cura = 15
                heroi.vida = curar(heroi.vida, cura)
                print(f"  {heroi.nome} usou Cura Arcana e recuperou {cura} de vida! ({heroi.vida} PV)")

            elif acao == "Escudo Mágico":
                heroi._escudo_ativo = True
                print(f"  {heroi.nome} ergue um Escudo Mágico! O próximo golpe será reduzido à metade.")

            else:
                dano = ataque_mago(acao)
                inimigo.sofrer_dano(dano)
                print(f"  {heroi.nome} usou {acao} e causou {dano} de dano em {inimigo.nome}!")

        else:
            heroi.atacar_inimigo(inimigo)
            time.sleep(3)   # pausa de 3 segundos antes do inimigo atacar

        if esta_vivo(inimigo.vida):
            dano_inimigo = atacar(inimigo.classe.lower(), inimigo.modificador_ataque, heroi.ca)

            if dano_inimigo > 0:
                dano_inimigo += 2   # aumenta o dano do inimigo

                if getattr(heroi, "_escudo_ativo", False):
                    dano_inimigo = max(1, dano_inimigo // 2)
                    print(f"  O Escudo Mágico absorveu parte do golpe! Dano reduzido para {dano_inimigo}.")
                    heroi._escudo_ativo = False

                heroi.sofrer_dano(dano_inimigo)
                print(f"  {inimigo.nome} atacou {heroi.nome} por {dano_inimigo} de dano! ({heroi.vida} PV restantes)")
            else:
                print(f"  {inimigo.nome} errou o ataque!")

        rodada += 1

    return esta_vivo(heroi.vida)


def introducao():
    titulo("A FAZENDA MALDITA")
    print("""
  Uma névoa densa cobre os campos ao redor de Valdris.
  Viajantes desapareceram perto da Fazenda dos Holloway.

  Ninguém sabe o que existe lá dentro.
  Você veio descobrir.
    """)
    pausar()


def chegada(heroi):
    titulo("A CHEGADA")
    print(f"""
  A estrada de terra te leva até um portão enferrujado.
  O celeiro ao fundo está aberto.

  "{heroi.nome}..." — uma voz ecoa das sombras.
    """)
    pausar()

    abordagem = escolher(
        "  Como você entra na fazenda?",
        [
            "Entro direto pelo portão",
            "Contorno pelo celeiro",
            "Grito para o inimigo aparecer"
        ]
    )

    if abordagem == "Contorno pelo celeiro":
        heroi.vida = curar(heroi.vida, 10)
        print(f"\n  Você entrou com vantagem. +10 PV ({heroi.vida} PV)")
    elif abordagem == "Grito para o inimigo aparecer":
        heroi.sofrer_dano(5)
        print(f"\n  O susto te machucou. -5 PV ({heroi.vida} PV)")
    else:
        print("\n  Você entra sem bônus nem penalidade.")

    pausar()


def criar_inimigo():
    titulo("O HABITANTE DA FAZENDA")
    print("""
  Do celeiro surge um Espantalho Amaldiçoado,
  feito de palha, magia negra e ódio.
    """)
    pausar()

    return Personagem(
        nome="Espantalho Amaldiçoado",
        classe="arqueiro",
        vida=50,
        armadura=5,
        velocidade=10,
        ca=15,
        modificador_ataque=4
    )


def desfecho(heroi, vitoria):
    titulo("DESFECHO")

    if vitoria:
        print(f"""
  O Espantalho caiu.

  {heroi.nome} sobreviveu à Fazenda Maldita
  com {heroi.vida} PV restantes.
        """)

        if heroi.nivel < 2:
            heroi.subir_nivel()

        print("  Status final:")
        heroi.mostrar_status()

    else:
        print(f"""
  {heroi.nome} caiu na fazenda.

  Fim.
        """)


def jogar():
    while True:
        introducao()
        heroi = criar_personagem()
        chegada(heroi)
        inimigo = criar_inimigo()
        vitoria = combate(heroi, inimigo)
        desfecho(heroi, vitoria)

        resposta = input("\n  Jogar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            break


if __name__ == "__main__":
    jogar()