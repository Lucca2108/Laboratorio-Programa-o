from classes import criar_personagem
from historia import iniciar_historia
<<<<<<< HEAD
from scores import salvar_score
=======
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23


def main():
    print("═" * 42)
    print("        🎮  RUÍNA FANTASMAGÓRICA  🎮")
    print("═" * 42)

    while True:
<<<<<<< HEAD
        heroi = criar_personagem()
        pontuacao = None

        try:
            pontuacao, _ = iniciar_historia(heroi)
        except KeyboardInterrupt:
            print("\n\n  Jogo interrompido pelo jogador.")
            break
        finally:
            if pontuacao is not None:
                resultado = "Venceu" if heroi.vivo() else "Derrota"
                salvar_score(heroi.nome, heroi.classe, heroi.nivel, pontuacao, resultado)

=======
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
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23
        resposta = input("\n  Jogar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            print("\n  Obrigado por jogar. Até a próxima aventura!")
            break


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23
