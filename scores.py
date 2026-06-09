import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCORES_PATH = os.path.join(BASE_DIR, "scores.txt")


def salvar_score(nome, classe, nivel, pontuacao, resultado):
    """
    Salva o resultado final do jogador no arquivo txt.
    Se o arquivo já tiver conteúdo, adiciona uma quebra de linha antes
    do novo registro para evitar que os textos fiquem grudados.
    """
    precisa_quebra = os.path.exists(SCORES_PATH) and os.path.getsize(SCORES_PATH) > 0

    with open(SCORES_PATH, "a", encoding="utf-8") as arquivo:
        if precisa_quebra:
            arquivo.write("\n")
        linha = (
            f"Jogador: {nome} | "
            f"Classe: {classe.capitalize()} | "
            f"Nível: {nivel} | "
            f"Pontuação: {pontuacao} | "
            f"Resultado: {resultado}\n"
        )
        arquivo.write(linha)


def mostrar_scores():
    """
    Lê o arquivo de texto e exibe os resultados na tela.
    Caso o arquivo ainda não exista, captura o erro e avisa o jogador.
    """
    try:
        with open(SCORES_PATH, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

            print("\n=== SCORES SALVOS ===")
            if conteudo.strip() == "":
                print("Nenhum score foi registrado ainda.")
            else:
                print(conteudo)

    except FileNotFoundError:
        print("\n=== SCORES SALVOS ===")
        print("Ainda não existem scores salvos. Jogue a primeira partida para registrar!")
