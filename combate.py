import time
from funcoes import esta_vivo, curar
from dados import atacar, ataque_mago
from classes import Personagem

# --- FUNÇÕES DE INTERFACE (Ajudantes de visualização) ---

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


# --- FUNÇÕES DE CRIAÇÃO DE INIMIGOS ---

def criar_mumia():
    return Personagem(
        nome="Múmia",
        classe="cavaleiro", # Classe base usada para definir o tipo de rolagem de ataque
        vida=30,
        armadura=5,
        velocidade=5,
        ca=12,
        modificador_ataque=3
    )

def criar_esqueleto():
    return Personagem(
        nome="Esqueleto Guerreiro",
        classe="arqueiro",
        vida=40,
        armadura=8,
        velocidade=10,
        ca=14,
        modificador_ataque=4
    )

def criar_guardiao_fantasma():
    return Personagem(
        nome="Guardião Fantasma",
        classe="mago",
        vida=70,
        armadura=10,
        velocidade=15,
        ca=16,
        modificador_ataque=6
    )


# --- LÓGICA PRINCIPAL DE COMBATE ---

def combate(heroi, inimigo):
    """
    Executa o loop de batalha entre o herói e um inimigo.
    Retorna True se o herói vencer (continuar vivo), False se perder.
    """
    titulo(f"COMBATE: {heroi.nome} vs {inimigo.nome}")
    rodada = 1

    while esta_vivo(heroi.vida) and esta_vivo(inimigo.vida):
        print(f"\n  Rodada {rodada}")
        print(f"  {heroi.nome}: {heroi.vida} PV  |  {inimigo.nome}: {inimigo.vida} PV")
        linha()

        # ==========================
        # TURNO DO HERÓI
        # ==========================
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
            # Classes Cavaleiro e Arqueiro usam ataque padrão
            heroi.atacar_inimigo(inimigo)
            time.sleep(1)

        # Verifica se o inimigo morreu com o golpe antes de ele tentar atacar de volta
        if not esta_vivo(inimigo.vida):
            break

        time.sleep(2) # Pausa dramática para o ataque do inimigo

        # ==========================
        # TURNO DO INIMIGO
        # ==========================
        dano_inimigo = atacar(inimigo.classe.lower(), inimigo.modificador_ataque, heroi.ca)

        if dano_inimigo > 0:
            dano_inimigo += 2   # Aumenta um pouco o dano base do inimigo

            # Verifica se o herói tem escudo ativo (Mago)
            if getattr(heroi, "_escudo_ativo", False):
                dano_inimigo = max(1, dano_inimigo // 2)
                print(f"  O Escudo Mágico absorveu parte do golpe! Dano reduzido para {dano_inimigo}.")
                heroi._escudo_ativo = False

            heroi.sofrer_dano(dano_inimigo)
            print(f"  {inimigo.nome} atacou {heroi.nome} por {dano_inimigo} de dano! ({heroi.vida} PV restantes)")
        else:
            print(f"  {inimigo.nome} errou o ataque!")

        rodada += 1
        time.sleep(1)

    # O loop termina quando alguém morre. Retorna True se a vida do herói for > 0.
    return esta_vivo(heroi.vida)