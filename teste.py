# Função para calcular a vida restante após receber dano
def calcular_vida(vida, dano):
    nova_vida = vida - dano
    return nova_vida

# Função para calcular a vida total após curar
def curar(vida, cura):
    nova_vida = vida + cura
    return nova_vida

calcular_vida(10, 15)# Resultado: -5 (vida restante após receber dano)
curar(10, 5) # Resultado: 15 (vida total após curar