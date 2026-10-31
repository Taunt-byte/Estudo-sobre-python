"""
EXERCÍCIO 01 — ANALISADOR DE INFORMAÇÕES PESSOAIS

ENUNCIADO:
Crie um programa que solicite nome, idade, altura e cidade do usuário.
O programa deverá apresentar essas informações, verificar se o usuário
é maior de idade e calcular quantos anos faltam para completar 100 anos.
"""

def analisar_pessoa(nome, idade, altura, cidade):
    """Analisa e apresenta os dados pessoais informados."""
    print("\n========== RELATÓRIO PESSOAL ==========")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura:.2f} m")
    print(f"Cidade: {cidade}")

    if idade >= 18:
        print("Situação: Maior de idade.")
    else:
        print("Situação: Menor de idade.")

    if idade < 100:
        print(f"Faltam {100 - idade} anos para completar 100 anos.")
    elif idade == 100:
        print("Você completou 100 anos!")
    else:
        print(f"Você já passou dos 100 anos há {idade - 100} anos.")


def main():
    try:
        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura em metros: "))
        cidade = input("Digite sua cidade: ").strip()

        if not nome or not cidade:
            raise ValueError("Nome e cidade não podem ficar vazios.")

        if idade < 0 or altura <= 0:
            raise ValueError("Idade e altura devem ser valores positivos.")

        analisar_pessoa(nome, idade, altura, cidade)

    except ValueError as erro:
        print(f"Entrada inválida: {erro}")


if __name__ == "__main__":
    main()