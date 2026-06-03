from dados import atacar, ataque_mago
from funcoes import calcular_vida, esta_vivo, upar_nivel, curar


class Personagem:
    def __init__(self, nome, classe, vida, armadura, velocidade, ca, modificador_ataque, nivel=1):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.armadura = armadura
        self.velocidade = velocidade
        self.ca = ca
        self.modificador_ataque = modificador_ataque
        self.nivel = nivel

    def mostrar_status(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida}")
        print(f"Armadura: {self.armadura}")
        print(f"Velocidade: {self.velocidade}")
        print(f"CA: {self.ca}")
        print(f"Modificador de ataque: {self.modificador_ataque}")
        print(f"Nível: {self.nivel}")
        print("-" * 25)

    def sofrer_dano(self, dano):
        self.vida = calcular_vida(self.vida, dano)

    def vivo(self):
        return esta_vivo(self.vida)

    def subir_nivel(self):
        self.nivel, self.vida = upar_nivel(self.nivel, self.vida)
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def curar_personagem(self, valor_cura):
        self.vida = curar(self.vida, valor_cura)
        print(f"{self.nome} recuperou {valor_cura} de vida!")

    def atacar_inimigo(self, inimigo):
        dano = atacar(self.classe.lower(), self.modificador_ataque, inimigo.ca)

        if dano > 0:
            inimigo.sofrer_dano(dano)
            print(f"{self.nome} causou {dano} de dano em {inimigo.nome}!")
        else:
            print(f"{self.nome} errou o ataque em {inimigo.nome}!")


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            classe="mago",
            vida=30,
            armadura=10,
            velocidade=25,
            ca=12,
            modificador_ataque=8
        )
        self.magias = ["Bola de Fogo", "Raio de Gelo", "Cura Arcana"]

    def mostrar_magias(self):
        print(f"Magias de {self.nome}:")
        for magia in self.magias:
            print(f"- {magia}")

    def usar_magia(self, magia, inimigo=None):
        if magia == "Bola de Fogo":
            dano = ataque_mago("Bola de Fogo")
            if inimigo:
                inimigo.sofrer_dano(dano)
                print(f"{self.nome} usou {magia} e causou {dano} de dano em {inimigo.nome}!")

        elif magia == "Raio de Gelo":
            dano = ataque_mago("Raio de Gelo")
            if inimigo:
                inimigo.sofrer_dano(dano)
                print(f"{self.nome} usou {magia} e causou {dano} de dano em {inimigo.nome}!")

        elif magia == "Cura Arcana":
            self.curar_personagem(15)
            print(f"{self.nome} usou {magia}!")

        else:
            print("Magia inválida.")


class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(
            nome=nome,
            classe="arqueiro",
            vida=40,
            armadura=20,
            velocidade=30,
            ca=17,
            modificador_ataque=6
        )


class Cavaleiro(Personagem):
    def __init__(self, nome, arma):
        super().__init__(
            nome=nome,
            classe="cavaleiro",
            vida=55,
            armadura=50,
            velocidade=10,
            ca=16,
            modificador_ataque=5
        )

        self.arma = arma.lower()

        if self.arma == "espada":
            self.bonus_dano = 2
        elif self.arma == "machado":
            self.bonus_dano = 4
        else:
            raise ValueError("Arma inválida. Escolha entre espada ou machado.")

    def atacar_inimigo(self, inimigo):
        dano = atacar(self.classe.lower(), self.modificador_ataque, inimigo.ca)

        if dano > 0:
            dano += self.bonus_dano
            inimigo.sofrer_dano(dano)
            print(f"{self.nome} atacou com {self.arma} e causou {dano} de dano em {inimigo.nome}!")
        else:
            print(f"{self.nome} errou o ataque em {inimigo.nome}!")


# ─────────────────────────────────────────
# ADICIONADO: funções auxiliares e criar_personagem
# movidas do arquivo principal (jogo.py)
# ─────────────────────────────────────────

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