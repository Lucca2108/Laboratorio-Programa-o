from classes import criar_personagem
from historia import iniciar_historia
from scores import salvar_score


def main():
    print("═" * 42)
    print("        🎮  RUÍNA FANTASMAGÓRICA  🎮")
    print("═" * 42)

    while True:
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

        resposta = input("\n  Jogar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            print("\n  Obrigado por jogar. Até a próxima aventura!")
            break


if __name__ == "__main__":
    main()
