"""
EXERCÍCIO 03 — CONVERSOR DE UNIDADES

ENUNCIADO:
Crie um conversor que permita transformar:
- Celsius em Fahrenheit e Kelvin;
- Quilômetros em milhas;
- Metros em centímetros;
- Quilogramas em libras;
- Horas em minutos e segundos.

O usuário deverá escolher a conversão e informar o valor.
"""

def converter(opcao, valor):
    """Realiza a conversão de acordo com a opção escolhida."""
    conversoes = {
        "1": ("Fahrenheit", (valor * 9 / 5) + 32),
        "2": ("Kelvin", valor + 273.15),
        "3": ("Milhas", valor * 0.621371),
        "4": ("Centímetros", valor * 100),
        "5": ("Libras", valor * 2.20462),
        "6": ("Minutos", valor * 60),
        "7": ("Segundos", valor * 3600)
    }

    if opcao not in conversoes:
        raise ValueError("Opção inválida.")

    if opcao in ("1", "2") and valor < -273.15:
        raise ValueError("Temperatura abaixo do zero absoluto.")

    return conversoes[opcao]


def main():
    while True:
        print("\n========== CONVERSOR ==========")
        print("1 - Celsius para Fahrenheit")
        print("2 - Celsius para Kelvin")
        print("3 - Quilômetros para milhas")
        print("4 - Metros para centímetros")
        print("5 - Quilogramas para libras")
        print("6 - Horas para minutos")
        print("7 - Horas para segundos")
        print("0 - Sair")

        opcao = input("Escolha uma conversão: ")

        if opcao == "0":
            break

        try:
            valor = float(input("Digite o valor: "))

            if valor < 0 and opcao not in ("1", "2"):
                raise ValueError("O valor não pode ser negativo.")

            unidade, resultado = converter(opcao, valor)
            print(f"Resultado: {resultado:.2f} {unidade}")

        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()