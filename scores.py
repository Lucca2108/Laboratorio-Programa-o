# --- FUNÇÕES DE SALVAMENTO E LEITURA DE PONTUAÇÃO ---

def salvar_score(nome, classe, nivel, pontuacao, resultado):
    """
    Salva o resultado final do jogador no arquivo txt.
    O modo 'a' (append) garante que os novos scores sejam adicionados no final,
    sem apagar o histórico de quem jogou antes.
    """
    with open("scores.txt", "a", encoding="utf-8") as arquivo:
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
        with open("scores.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
            print("\n=== SCORES SALVOS ===")
            if conteudo.strip() == "":
                print("Nenhum score foi registrado ainda.")
            else:
                print(conteudo)
                
    except FileNotFoundError:
        print("\n=== SCORES SALVOS ===")
        print("Ainda não existem scores salvos. Jogue a primeira partida para registrar!")