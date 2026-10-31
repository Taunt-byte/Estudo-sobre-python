"""
EXERCÍCIO 02 — CALCULADORA INTELIGENTE

ENUNCIADO:
Desenvolva uma calculadora que realize adição, subtração, multiplicação,
divisão, potenciação e módulo. O usuário deverá escolher a operação e
informar dois números. Trate divisões por zero e entradas inválidas.
"""

def calcular(numero1, numero2, operacao):
    """Executa a operação matemática escolhida."""
    operacoes = {
        "1": lambda: numero1 + numero2,
        "2": lambda: numero1 - numero2,
        "3": lambda: numero1 * numero2,
        "4": lambda: numero1 / numero2,
        "5": lambda: numero1 ** numero2,
        "6": lambda: numero1 % numero2
    }

    if operacao not in operacoes:
        raise ValueError("Operação inexistente.")

    if operacao in ("4", "6") and numero2 == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")

    return operacoes[operacao]()


def main():
    while True:
        print("\n========== CALCULADORA ==========")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potenciação")
        print("6 - Módulo")
        print("0 - Sair")

        operacao = input("Escolha uma operação: ")

        if operacao == "0":
            print("Calculadora encerrada.")
            break

        try:
            numero1 = float(input("Primeiro número: "))
            numero2 = float(input("Segundo número: "))

            resultado = calcular(numero1, numero2, operacao)
            print(f"Resultado: {resultado:g}")

        except ValueError as erro:
            print(f"Erro: {erro}")

        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()