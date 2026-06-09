<<<<<<< HEAD
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCORES_PATH = os.path.join(BASE_DIR, "scores.txt")

=======
# --- FUNÇÕES DE SALVAMENTO E LEITURA DE PONTUAÇÃO ---
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23

def salvar_score(nome, classe, nivel, pontuacao, resultado):
    """
    Salva o resultado final do jogador no arquivo txt.
<<<<<<< HEAD
    Se o arquivo já tiver conteúdo, adiciona uma quebra de linha antes
    do novo registro para evitar que os textos fiquem grudados.
    """
    precisa_quebra = os.path.exists(SCORES_PATH) and os.path.getsize(SCORES_PATH) > 0

    with open(SCORES_PATH, "a", encoding="utf-8") as arquivo:
        if precisa_quebra:
            arquivo.write("\n")
=======
    O modo 'a' (append) garante que os novos scores sejam adicionados no final,
    sem apagar o histórico de quem jogou antes.
    """
    with open("scores.txt", "a", encoding="utf-8") as arquivo:
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23
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
<<<<<<< HEAD
        with open(SCORES_PATH, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

=======
        with open("scores.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23
            print("\n=== SCORES SALVOS ===")
            if conteudo.strip() == "":
                print("Nenhum score foi registrado ainda.")
            else:
                print(conteudo)
<<<<<<< HEAD

    except FileNotFoundError:
        print("\n=== SCORES SALVOS ===")
        print("Ainda não existem scores salvos. Jogue a primeira partida para registrar!")
=======
                
    except FileNotFoundError:
        print("\n=== SCORES SALVOS ===")
        print("Ainda não existem scores salvos. Jogue a primeira partida para registrar!")
>>>>>>> e33e67579afdf2eae94dd35a02624a808dfcea23
