from classes import criar_personagem
from historia import iniciar_historia


def main():
    print("═" * 42)
    print("        🎮  RUÍNA FANTASMAGÓRICA  🎮")
    print("═" * 42)

    while True:
        # 1) Pessoa 1: cria o herói
        heroi = criar_personagem()

        # 2) Pessoa 2: conduz a narrativa, escolhas e inventário.
        #    Pessoa 3: o combate é chamado de dentro da história.
        try:
            iniciar_historia(heroi)
        except KeyboardInterrupt:
            print("\n\n  Jogo interrompido pelo jogador.")
            break

        # 3) Jogar novamente
        resposta = input("\n  Jogar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            print("\n  Obrigado por jogar. Até a próxima aventura!")
            break


if __name__ == "__main__":
    main()