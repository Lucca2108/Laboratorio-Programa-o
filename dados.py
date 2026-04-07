import random

def d20(contexto: str = "") -> int:
    resultado = random.randint(1, 20)
    if contexto:
        print(f"[d20] {contexto}: {resultado}")
    return resultado

# dano base das classes
def ataque_mago(contexto: str = "") -> int:
    resultado = random.randint(1, 12)
    if contexto:
        print(f"[Mago] {contexto}: {resultado}")
    return resultado

def ataque_arqueiro(contexto: str = "") -> int:
    resultado = random.randint(1, 8)
    if contexto:
        print(f"[Arqueiro] {contexto}: {resultado}")
    return resultado

def ataque_cavaleiro(contexto: str = "") -> int:
    resultado = random.randint(1, 10)
    if contexto:
        print(f"[Cavaleiro] {contexto}: {resultado}")
    return resultado


def atacar(classe: str, modificador: int = 0, ca_alvo: int = 10) -> int:
    """
    Realiza a tentativa de ataque de uma criatura/ personagem.

    Parâmetros:
        classe (str): nome da classe que determina o dado de dano (mago, arqueiro, cavaleiro)
        modificador (int): bônus somado à rolagem do d20
        ca_alvo (int): Classe de Armadura do alvo (valor alvo para acertar)

    Retorno:
        int: dano causado (0 se errar)
    """

    rolagem = d20("rolagem de ataque")
    total = rolagem + modificador

    # Verifica acerto: total >= CA do alvo
    if total < ca_alvo:
        # Errou o ataque
        if rolagem == 1:
            print("Falha crítica!")
        return 0

    # Acertou: calcula dano conforme a classe
    if classe == "mago":
        dano = ataque_mago("dano do mago")
    elif classe == "arqueiro":
        dano = ataque_arqueiro("dano do arqueiro")
    elif classe == "cavaleiro":
        dano = ataque_cavaleiro("dano do cavaleiro")
    else:
        print("Classe inválida.")
        return 0

    # Acerto crítico natural (20) dobra o dano
    if rolagem == 20:
        dano *= 2
        print("Acerto crítico! Dano dobrado.")

    return dano

#classe mago precisa ter 3 magias, classe cavaleiro precisa escolher entre espada e machado
# CLasse de Armadura (CA) número minimo que precisa pra acertar o inimigo
# Nos ataques adicionar um modificador de rolagem pros ataques (1d20 + 8 >= CA inimiga) 