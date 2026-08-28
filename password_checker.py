"""Verificador educacional de politica de senhas."""

from getpass import getpass


CARACTERES_MINIMOS = 8
CARACTERES_ESPECIAIS = "!@#$%&*()-_=+[]{};:,.?/"


def possui_minimo(senha):
    """Verifica se a senha possui a quantidade minima de caracteres."""
    return len(senha) >= CARACTERES_MINIMOS


def possui_letra_maiuscula(senha):
    """Verifica se existe pelo menos uma letra maiuscula."""
    for caractere in senha:
        if caractere.isupper():
            return True
    return False


def possui_letra_minuscula(senha):
    """Verifica se existe pelo menos uma letra minuscula."""
    for caractere in senha:
        if caractere.islower():
            return True
    return False


def possui_numero(senha):
    """Verifica se existe pelo menos um numero."""
    for caractere in senha:
        if caractere.isdigit():
            return True
    return False


def possui_caractere_especial(senha):
    """Verifica se existe pelo menos um caractere especial permitido."""
    for caractere in senha:
        if caractere in CARACTERES_ESPECIAIS:
            return True
    return False


def possui_repeticao_consecutiva(senha, limite=3):
    """Identifica um mesmo caractere repetido varias vezes seguidas."""
    if not senha:
        return False

    repeticoes = 1

    for indice in range(1, len(senha)):
        if senha[indice] == senha[indice - 1]:
            repeticoes += 1
            if repeticoes >= limite:
                return True
        else:
            repeticoes = 1

    return False


def classificar_senha(pontuacao):
    """Classifica a senha de acordo com a quantidade de criterios atendidos."""
    if pontuacao <= 2:
        return "Weak"
    if pontuacao <= 4:
        return "Medium"
    return "Strong"


def analisar_senha(senha):
    """Analisa a senha e retorna criterios, pontuacao e recomendacoes."""
    criterios = {
        "Minimum of 8 characters": possui_minimo(senha),
        "Uppercase letter": possui_letra_maiuscula(senha),
        "Lowercase letter": possui_letra_minuscula(senha),
        "Number": possui_numero(senha),
        "Special character": possui_caractere_especial(senha),
        "No three consecutive repeated characters": not possui_repeticao_consecutiva(senha),
    }

    recomendacoes = []

    if not criterios["Minimum of 8 characters"]:
        recomendacoes.append("Use at least 8 characters.")
    if not criterios["Uppercase letter"]:
        recomendacoes.append("Add an uppercase letter.")
    if not criterios["Lowercase letter"]:
        recomendacoes.append("Add a lowercase letter.")
    if not criterios["Number"]:
        recomendacoes.append("Add a number.")
    if not criterios["Special character"]:
        recomendacoes.append("Add a special character.")
    if not criterios["No three consecutive repeated characters"]:
        recomendacoes.append("Avoid repeating the same character three times in a row.")

    pontuacao = sum(criterios.values())

    return {
        "criteria": criterios,
        "score": pontuacao,
        "classification": classificar_senha(pontuacao),
        "recommendations": recomendacoes,
    }


def executar_cli():
    """Executa o verificador no terminal sem exibir a senha digitada."""
    print("=== PASSWORD POLICY CHECKER ===")
    senha = getpass("Enter a password to evaluate: ")
    resultado = analisar_senha(senha)

    print("\nCriteria:")
    for criterio, aprovado in resultado["criteria"].items():
        simbolo = "[PASS]" if aprovado else "[FAIL]"
        print(f"{simbolo} {criterio}")

    print(f"\nScore: {resultado['score']}/6")
    print(f"Classification: {resultado['classification']}")

    if resultado["recommendations"]:
        print("\nRecommendations:")
        for recomendacao in resultado["recommendations"]:
            print(f"- {recomendacao}")


if __name__ == "__main__":
    executar_cli()
