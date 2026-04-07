# =============================================================================
#  historia.py — A Fazenda Maldita
#  Projeto: RPG em Python
#
#  Este arquivo é o "coração" do jogo. Ele importa as funções e classes dos
#  outros três arquivos (dados.py, funcoes.py, classes.py) e monta a história,
#  o combate e as escolhas do jogador.
#
#  Como o projeto está organizado:
#    dados.py   → funções de sorteio (dados de RPG)
#    funcoes.py → funções matemáticas de jogo (vida, cura, nível, caminhos)
#    classes.py → classes dos personagens (Mago, Arqueiro, Cavaleiro)
#    historia.py → você está aqui! Une tudo em uma história jogável.
# =============================================================================


# -----------------------------------------------------------------------------
#  IMPORTAÇÕES
#
#  "from X import Y" significa: "do arquivo X, traga a função/classe Y".
#  Assim não precisamos escrever dados.atacar() — só atacar() já funciona.
# -----------------------------------------------------------------------------

from dados import atacar, ataque_mago
# atacar()     → resolve um turno de ataque (rola d20, calcula dano, acerto crítico)
# ataque_mago() → rola o dado de dano específico do mago (1d12)

from funcoes import calcular_vida, esta_vivo, curar
# calcular_vida() → subtrai dano da vida, nunca deixa ir abaixo de 0
# esta_vivo()     → retorna True se vida > 0, False caso contrário
# curar()         → soma pontos de vida ao personagem

from classes import Mago, Arqueiro, Cavaleiro, Personagem
# Mago, Arqueiro, Cavaleiro → subclasses prontas com atributos pré-definidos
# Personagem                → classe base, usada para criar inimigos customizados


# =============================================================================
#  FUNÇÕES UTILITÁRIAS
#
#  Funções pequenas que ajudam na formatação do texto do jogo.
#  Não têm lógica de RPG — só deixam o terminal mais legível.
# =============================================================================

def linha():
    """Imprime uma linha divisória para separar seções no terminal."""
    print("─" * 42)


def titulo(texto):
    """
    Imprime um título formatado entre duas linhas divisórias.

    Parâmetro:
        texto (str): o texto que aparecerá como título
    """
    linha()
    print(f"  {texto}")
    linha()


def escolher(prompt, opcoes):
    """
    Exibe uma lista numerada de opções e aguarda o jogador digitar
    o número correspondente. Repete até receber uma entrada válida.

    Parâmetros:
        prompt  (str):  pergunta exibida ao jogador
        opcoes  (list): lista de strings com as opções disponíveis

    Retorno:
        str: a opção escolhida pelo jogador (texto, não número)

    Exemplo de uso:
        classe = escolher("Escolha sua classe:", ["Mago", "Arqueiro"])
        # Se o jogador digitar "1", retorna "Mago"
    """
    print(prompt)
    for i, op in enumerate(opcoes, 1):
        # enumerate() gera pares (índice, valor); start=1 começa em 1 em vez de 0
        print(f"  [{i}] {op}")

    while True:
        # Loop infinito: só sai quando o jogador digitar algo válido
        entrada = input("> ").strip()  # .strip() remove espaços acidentais

        if entrada.isdigit() and 1 <= int(entrada) <= len(opcoes):
            # isdigit() garante que não vai quebrar ao converter para int
            return opcoes[int(entrada) - 1]  # -1 porque listas começam em 0

        print("  Escolha inválida. Tente de novo.")


def pausar():
    """
    Pausa o jogo e aguarda o jogador pressionar ENTER.
    Dá tempo para o jogador ler o texto antes de continuar.
    """
    input("\n  [ENTER para continuar...]\n")


# =============================================================================
#  CRIAÇÃO DO PERSONAGEM
#
#  Esta função é chamada uma vez no início do jogo.
#  Ela coleta as escolhas do jogador e retorna um objeto de personagem
#  já configurado, pronto para ser usado no combate e na história.
# =============================================================================

def criar_personagem():
    """
    Guia o jogador pela criação do personagem:
      1. Escolhe o nome (texto livre)
      2. Escolhe a classe (Mago, Arqueiro ou Cavaleiro)
      3. Se Mago: escolhe 3 magias de um pool de 5
      4. Se Cavaleiro: escolhe a arma (espada ou machado)

    Retorno:
        Personagem: objeto da classe escolhida (Mago, Arqueiro ou Cavaleiro),
                    já com nome e atributos configurados.
    """
    titulo("CRIAÇÃO DO PERSONAGEM")

    # --- Nome ---
    # Loop que impede nome vazio: .strip() remove espaços, not nome verifica se ficou vazio
    nome = ""
    while not nome:
        nome = input("  Qual é o nome do seu personagem?\n> ").strip()
        if not nome:
            print("  O nome não pode estar vazio.")

    # --- Classe ---
    classe = escolher("\n  Escolha sua classe:", ["Mago", "Arqueiro", "Cavaleiro"])

    # --- Configuração específica por classe ---
    if classe == "Mago":
        # Pool de todas as magias disponíveis
        todas_magias = ["Bola de Fogo", "Raio de Gelo", "Relâmpago", "Cura Arcana", "Escudo Mágico"]

        print("\n  Escolha 3 magias para o seu grimório:")
        magias_escolhidas = []
        opcoes_restantes = todas_magias[:]  # cópia da lista para não modificar o original

        # Repete até o jogador ter 3 magias; cada magia escolhida é removida das opções
        while len(magias_escolhidas) < 3:
            falta = 3 - len(magias_escolhidas)
            magia = escolher(f"  ({falta} restante(s)):", opcoes_restantes)
            magias_escolhidas.append(magia)
            opcoes_restantes.remove(magia)  # evita escolher a mesma magia duas vezes
            print(f"  ✓ {magia} adicionada!")

        # Cria o objeto Mago e substitui a lista padrão pelas magias escolhidas
        personagem = Mago(nome)
        personagem.magias = magias_escolhidas

    elif classe == "Arqueiro":
        # Arqueiro não tem customização extra — só cria o objeto
        personagem = Arqueiro(nome)

    else:  # Cavaleiro
        arma = escolher("\n  Escolha sua arma:", ["Espada", "Machado"])
        # .lower() converte para minúsculo porque Cavaleiro() espera "espada" ou "machado"
        personagem = Cavaleiro(nome, arma=arma.lower())

    print(f"\n  {nome} o(a) {classe} está pronto(a) para a aventura!")
    pausar()
    return personagem  # devolve o objeto para ser usado no resto do jogo


# =============================================================================
#  SISTEMA DE COMBATE
#
#  Esta é a função mais complexa do jogo. Ela simula turnos de combate
#  entre o herói e um inimigo até que um dos dois chegue a 0 de vida.
#
#  Estrutura de um turno:
#    1. Mostra os PV de ambos
#    2. Herói age (ataque ou magia, dependendo da classe)
#    3. Inimigo age (se ainda estiver vivo)
#    4. Repete até alguém cair
# =============================================================================

def combate(heroi, inimigo):
    """
    Executa o loop de combate turno a turno entre herói e inimigo.

    Parâmetros:
        heroi   (Personagem): o personagem do jogador
        inimigo (Personagem): o monstro ou oponente

    Retorno:
        bool: True se o herói vencer, False se o herói cair

    Observação sobre o Mago:
        Se o herói for um Mago, o jogador escolhe a ação a cada turno.
        Para as outras classes, o ataque é automático.
    """
    titulo(f"COMBATE: {heroi.nome} vs {inimigo.nome}")
    rodada = 1

    # O loop continua enquanto ambos estiverem vivos
    # esta_vivo() está em funcoes.py e retorna vida > 0
    while esta_vivo(heroi.vida) and esta_vivo(inimigo.vida):

        # Cabeçalho da rodada com PV atuais
        print(f"\n  Rodada {rodada}")
        print(f"  {heroi.nome}: {heroi.vida} PV  |  {inimigo.nome}: {inimigo.vida} PV")
        linha()

        # ── TURNO DO HERÓI ──────────────────────────────────────────────────

        if heroi.classe.lower() == "mago":
            # Mago tem escolha tática a cada rodada
            # A lista de opções é as magias do grimório + ataque básico
            acao = escolher("  O que você faz?", heroi.magias + ["Ataque básico"])

            if acao == "Ataque básico":
                # Usa o método herdado de Personagem — chama atacar() de dados.py internamente
                heroi.atacar_inimigo(inimigo)

            elif acao == "Cura Arcana":
                # curar() está em funcoes.py: soma o valor à vida atual
                cura = 15
                heroi.vida = curar(heroi.vida, cura)
                print(f"  {heroi.nome} usou Cura Arcana e recuperou {cura} de vida! ({heroi.vida} PV)")

            elif acao == "Escudo Mágico":
                # getattr() será usado no turno do inimigo para verificar este atributo
                # Usamos _escudo_ativo como atributo temporário (o _ indica que é interno)
                heroi._escudo_ativo = True
                print(f"  {heroi.nome} ergue um Escudo Mágico! O próximo golpe será reduzido à metade.")

            else:
                # Qualquer outra magia ofensiva (Bola de Fogo, Raio de Gelo, Relâmpago)
                # ataque_mago() está em dados.py: rola 1d12 e retorna o dano
                dano = ataque_mago(acao)
                inimigo.sofrer_dano(dano)  # sofrer_dano() está em classes.py, usa calcular_vida()
                print(f"  {heroi.nome} usou {acao} e causou {dano} de dano em {inimigo.nome}!")

        else:
            # Arqueiro e Cavaleiro atacam automaticamente
            # atacar_inimigo() está definido em classes.py e já lida com bônus de arma (Cavaleiro)
            heroi.atacar_inimigo(inimigo)

        # ── TURNO DO INIMIGO ────────────────────────────────────────────────

        if esta_vivo(inimigo.vida):  # só age se ainda estiver de pé
            # atacar() está em dados.py:
            #   - rola d20 + modificador_ataque
            #   - compara com a CA do herói
            #   - se acertar, rola o dado de dano da classe e retorna o valor
            #   - retorna 0 se errar
            dano_inimigo = atacar(inimigo.classe.lower(), inimigo.modificador_ataque, heroi.ca)

            if dano_inimigo > 0:
                # Verifica se o Escudo Mágico está ativo
                # getattr(obj, atributo, valor_padrão) — evita erro se o atributo não existir
                if getattr(heroi, "_escudo_ativo", False):
                    dano_inimigo = max(1, dano_inimigo // 2)  # // é divisão inteira (sem decimais)
                    print(f"  O Escudo Mágico absorveu parte do golpe! Dano reduzido para {dano_inimigo}.")
                    heroi._escudo_ativo = False  # o escudo se consome após bloquear um golpe

                heroi.sofrer_dano(dano_inimigo)
                print(f"  {inimigo.nome} atacou {heroi.nome} por {dano_inimigo} de dano! ({heroi.vida} PV restantes)")
            else:
                print(f"  {inimigo.nome} errou o ataque!")

        rodada += 1

    # Retorna True se o herói ainda estiver vivo ao sair do loop
    return esta_vivo(heroi.vida)


# =============================================================================
#  HISTÓRIA PRINCIPAL
#
#  Função que orquestra toda a narrativa: introdução, criação do personagem,
#  chegada à fazenda, escolha de abordagem e o combate final.
#  É chamada uma vez para iniciar — e pode se chamar de novo para reiniciar.
# =============================================================================

def jogar():
    """
    Função principal do jogo. Controla o fluxo da história do início ao fim:
      1. Introdução narrativa
      2. Criação do personagem (chama criar_personagem())
      3. Chegada à fazenda com escolha de abordagem
      4. Combate contra o Espantalho Amaldiçoado (chama combate())
      5. Desfecho baseado no resultado do combate
      6. Opção de reiniciar (recursão: jogar() chama jogar() novamente)
    """
    titulo("A FAZENDA MALDITA")
    print("""
  Uma névoa densa cobre os campos ao redor de Valdris.
  Viajantes desapareceram perto da Fazenda dos Holloway —
  abandonada há anos, dizem os aldeões.

  Ninguém sabe o que espreita lá dentro.
  Você veio descobrir.
    """)
    pausar()

    # Criação do personagem — retorna um objeto Mago, Arqueiro ou Cavaleiro
    heroi = criar_personagem()

    # ── CHEGADA À FAZENDA ──────────────────────────────────────────────────

    titulo("A CHEGADA")
    print(f"""
  A estrada de terra te leva até um portão enferrujado.
  Placas de madeira rangem com o vento.
  O celeiro ao fundo está com a porta aberta — escuro por dentro.

  "{heroi.nome}..." — uma voz rouca ecoa das sombras.
    """)
    pausar()

    # ── ESCOLHA DE ABORDAGEM ───────────────────────────────────────────────
    # A escolha afeta os PV do herói antes do combate começar
    abordagem = escolher(
        "  Como você entra na fazenda?",
        [
            "Entro direto pelo portão, espada em riste",
            "Contorno pelo celeiro, discretamente",
            "Grito para o que estiver lá dentro aparecer"
        ]
    )

    if "portão" in abordagem:
        # Abordagem neutra — nenhum bônus nem penalidade
        print("""
  Você empurra o portão com força.
  A névoa recua — como se soubesse que você veio lutar.
        """)

    elif "celeiro" in abordagem:
        # Furtividade recompensada com PV temporários
        # curar() em funcoes.py: nova_vida = vida + cura
        print("""
  Você se move pelas sombras. Surpresa é sua aliada.
  Você chega ao celeiro com a vantagem do primeiro ataque.
        """)
        heroi.vida = curar(heroi.vida, 10)
        print(f"  (Bônus furtivo: +10 PV temporários — {heroi.nome} tem {heroi.vida} PV)\n")

    else:
        # Gritar atrai atenção — pequena penalidade de PV
        # sofrer_dano() em classes.py usa calcular_vida() de funcoes.py
        print("""
  Silêncio. Depois — um rugido que faz o chão vibrar.
  Você chamou a atenção de algo que não deveria ter chamado.
        """)
        heroi.sofrer_dano(5)
        print(f"  (O susto drena 5 PV de {heroi.nome} — restam {heroi.vida} PV)\n")

    pausar()

    # ── CRIAÇÃO DO INIMIGO ─────────────────────────────────────────────────
    # Personagem é a classe base de classes.py — usamos ela para criar inimigos
    # sem precisar criar uma classe nova para cada monstro do jogo.
    #
    # Atributos escolhidos com equilíbrio para ~4-6 rodadas de combate:
    #   vida=70    → aguenta alguns golpes mas não é imortal
    #   ca=12      → relativamente fácil de acertar (bom para aprendizado)
    #   modificador_ataque=3 → ataca com moderação
    #   classe="arqueiro" → usa o dado d8 de dano, coerente com golpes de foice

    titulo("O HABITANTE DA FAZENDA")
    print("""
  Do interior do celeiro surge uma figura enorme:
  um Espantalho Amaldiçoado — palha e magia negra costuradas
  em forma humana, com olhos de brasa e mãos como foices.

  Ele protege algo. E não vai deixar você passar.
    """)
    pausar()

    espantalho = Personagem(
        nome="Espantalho Amaldiçoado",
        classe="arqueiro",      # define qual dado de dano ele usa (d8)
        vida=30,
        armadura=5,
        velocidade=10,
        ca=12,                  # Classe de Armadura: quanto precisa tirar no d20 para acertar
        modificador_ataque=3    # bônus somado à rolagem de ataque
    )

    # ── COMBATE ────────────────────────────────────────────────────────────
    # combate() retorna True se o herói vencer, False se cair
    vitoria = combate(heroi, espantalho)

    # ── DESFECHO ───────────────────────────────────────────────────────────
    titulo("DESFECHO")

    if vitoria:
        print(f"""
  O Espantalho desmorona. A palha se espalha pelo chão.
  Onde ele estava — uma caixa de madeira antiga.

  Dentro: um mapa com o símbolo do Senhor das Sombras.
  Isso é apenas o começo.

  {heroi.nome} saiu da Fazenda Maldita vivo(a).
  Com {heroi.vida} PV restantes — e muitas perguntas.
        """)
        # sobe de nível se ainda estiver no nível 1
        # upar_nivel() está em funcoes.py: nivel+1, vida+10
        if heroi.nivel < 2:
            heroi.subir_nivel()

        print(f"  Status final:")
        heroi.mostrar_status()  # método de Personagem em classes.py

    else:
        print(f"""
  {heroi.nome} caiu entre a palha e a sombra.
  A fazenda guarda seu segredo mais um dia.

  ... Fim.
        """)

    # ── REINICIAR ──────────────────────────────────────────────────────────
    # Recursão: jogar() chama a si mesma para reiniciar sem fechar o terminal.
    # Em projetos maiores, um loop while seria mais indicado para evitar
    # acúmulo de chamadas na memória (stack overflow em partidas longas).
    linha()
    jogar_novamente = input("  Jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        jogar()


# =============================================================================
#  PONTO DE ENTRADA
#
#  Esta estrutura é um padrão do Python:
#    if __name__ == "__main__"
#
#  Significa: "só execute o que está aqui se este arquivo for rodado diretamente".
#  Se outro arquivo importar historia.py, jogar() NÃO será chamada automaticamente.
#  Isso é uma boa prática para evitar execução acidental ao importar o módulo.
# =============================================================================

if __name__ == "__main__":
    jogar()