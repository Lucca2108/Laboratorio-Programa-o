vida = 20
nivel = 1

# função para calcular a vida após receber dano
def calcular_vida(vida, dano):
    nova_vida = vida - dano
    if nova_vida<0:
        nova_vida = 0  # a vida não pode ser negativa
    return nova_vida

# função para verificar se o personagem está vivo
def esta_vivo(vida):
    if vida > 0:
        return True
    else:        
        return False

# função para upar a personagem junto com a vida dela    
def upar_nivel(nivel, vida):
    novo_nivel = nivel +1
    nova_vida = vida +10
    return novo_nivel, nova_vida

# função para calcular a vida total após curar
def curar(vida, cura):
    nova_vida = vida + cura
    return nova_vida

#não usei isso aqui não, mas se quiserem usar fiquem a vontade
def caminho(lugar):
    if lugar == "Floresta":
        return "Você entrou na floresta. A brisa é limpa e gostosa, mas cuidado com os barulhos estranhos e as plantas venenosas!"
    elif lugar == "Montanha":
        return "Você subiu a montanha. A vista é incrível! Mas cuidado com os penhascos e os animais selvagens!"
    elif lugar == "Caverna":
        return "Você entrou na caverna. Frio, escura e úmida... o que será que tem lá dentro?"  
    raise ValueError("Lugar desconhecido. Tente novamente.")