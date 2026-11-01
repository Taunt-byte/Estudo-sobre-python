"""
EXERCÍCIO 08 — ANALISADOR DE PALAVRAS

ENUNCIADO:
Solicite uma frase ao usuário e desenvolva um analisador textual.
O programa deverá apresentar a quantidade de palavras, caracteres,
vogais, consoantes, palavra mais longa e palavras repetidas.
Também deverá apresentar as palavras em ordem alfabética.
"""

from collections import Counter
import re
import unicodedata


def remover_acentos(texto):
    """Remove acentos para facilitar a identificação das vogais."""
    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(
        caractere for caractere in normalizado
        if unicodedata.category(caractere) != "Mn"
    )


def analisar_frase(frase):
    palavras = re.findall(r"\b\w+\b", frase.lower(), flags=re.UNICODE)
    caracteres = [c for c in remover_acentos(frase.lower()) if c.isalpha()]

    vogais = sum(c in "aeiou" for c in caracteres)
    consoantes = len(caracteres) - vogais

    frequencia = Counter(palavras)
    repetidas = {
        palavra: quantidade
        for palavra, quantidade in frequencia.items()
        if quantidade > 1
    }

    print("\n========== ANÁLISE TEXTUAL ==========")
    print(f"Caracteres totais: {len(frase)}")
    print(f"Palavras: {len(palavras)}")
    print(f"Vogais: {vogais}")
    print(f"Consoantes: {consoantes}")

    if palavras:
        maior = max(palavras, key=len)
        print(f"Palavra mais longa: {maior}")
        print(f"Ordem alfabética: {sorted(palavras)}")
    else:
        print("Nenhuma palavra encontrada.")

    print(f"Palavras repetidas: {repetidas or 'Nenhuma'}")


def main():
    frase = input("Digite uma frase: ").strip()

    if not frase:
        print("A frase não pode ficar vazia.")
        return

    analisar_frase(frase)


if __name__ == "__main__":
    main()
    