# funções para o jogo
def calcular_vida(vida, dano):
    """
    Calcula a vida após receber dano.

    Parâmetros:
    vida (int): vida atual do personagem
    dano (int): dano recebido

    Retorno:
    int: nova vida (nunca menor que 0)
    """
    if dano < 0:
        raise ValueError("Dano não pode ser negativo")

    nova_vida = vida - dano
    if nova_vida < 0:
        nova_vida = 0

    return nova_vida


def esta_vivo(vida):
    """
    Verifica se o personagem está vivo.

    Parâmetros:
    vida (int): vida atual

    Retorno:
    bool: True se estiver vivo, False caso contrário
    """
    return vida > 0

 
def upar_nivel(nivel, vida):
    """
    Aumenta o nível do personagem e sua vida.

    Parâmetros:
    nivel (int): nível atual
    vida (int): vida atual

    Retorno:
    tuple: novo nível e nova vida
    """
    if nivel < 0:
        raise ValueError("Nível inválido")

    novo_nivel = nivel + 1
    nova_vida = vida + 10

    return novo_nivel, nova_vida


def curar(vida, cura):
    """
    Aplica cura ao personagem.

    Parâmetros:
    vida (int): vida atual
    cura (int): quantidade de cura

    Retorno:
    int: nova vida
    """
    if cura < 0:
        raise ValueError("Cura não pode ser negativa")

    return vida + cura


def caminho(lugar):
    """
    Retorna descrição do caminho escolhido.

    Parâmetros:
    lugar (str): nome do lugar

    Retorno:
    str: descrição do local
    """
    if lugar == "Floresta":
        return "Você entrou na floresta. A brisa é limpa e gostosa, mas cuidado com os barulhos estranhos e as plantas venenosas!"
    elif lugar == "Montanha":
        return "Você subiu a montanha. A vista é incrível! Mas cuidado com os penhascos e os animais selvagens!"
    elif lugar == "Caverna":
        return "Você entrou na caverna. Frio, escura e úmida... o que será que tem lá dentro?"

    raise ValueError("Lugar desconhecido")