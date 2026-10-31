"""
EXERCÍCIO 04 — ANALISADOR DE NÚMEROS

ENUNCIADO:
Solicite cinco números ao usuário e apresente:
- Maior e menor número;
- Média dos valores;
- Quantidade de números pares e ímpares;
- Lista dos números em ordem crescente;
- Soma dos números informados.
"""

def analisar_numeros(numeros):
    """Calcula estatísticas sobre uma lista de números."""
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print("\n========== ANÁLISE ==========")
    print(f"Números: {numeros}")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
    print(f"Média: {sum(numeros) / len(numeros):.2f}")
    print(f"Soma: {sum(numeros)}")
    print(f"Quantidade de pares: {len(pares)}")
    print(f"Quantidade de ímpares: {len(impares)}")
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
    print(f"Ordem crescente: {sorted(numeros)}")


def main():
    numeros = []

    for indice in range(5):
        while True:
            try:
                numero = int(input(f"Digite o {indice + 1}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Digite um número inteiro válido.")

    analisar_numeros(numeros)


if __name__ == "__main__":
    main()