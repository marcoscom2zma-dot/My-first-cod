
def count_words(text: str) -> int:
    """Conta o número de palavras em um texto."""
    return len(text.split())

def count_characters(text: str) -> int:
    """Conta o número de caracteres (incluindo espaços)."""
    return len(text)

def analyze_text(text: str):
    """Executa e exibe a análise completa do texto."""
    if not text.strip():
        print("⚠️ O texto fornecido está vazio.")
        return

