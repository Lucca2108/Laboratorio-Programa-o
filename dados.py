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


def atacar(classe: str) -> int:
    rolagem = d20("rolagem de ataque")

    if classe == "mago":
        dano = ataque_mago("dano do mago")
    elif classe == "arqueiro":
        dano = ataque_arqueiro("dano do arqueiro")
    elif classe == "cavaleiro":
        dano = ataque_cavaleiro("dano do cavaleiro")
    else:
        print("Classe inválida.")
        return 0

    if rolagem == 20:
        dano *= 2
        print("Acerto crítico! Dano dobrado.")

    return dano

#classe mago precisa ter 3 magias, classe cavaleiro precisa escolher entre espada e machado
# CLasse de Armadura (CA) número minimo que precisa pra acertar o inimigo
# Nos ataques adicionar um modificador de rolagem pros ataques (1d20 + 8 >= CA inimiga) 