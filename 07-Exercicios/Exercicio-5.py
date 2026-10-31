"""
EXERCÍCIO 05 — SIMULADOR DE CAIXA ELETRÔNICO

ENUNCIADO:
Desenvolva um caixa eletrônico que permita consultar saldo, depositar
dinheiro e realizar saques. Ao realizar um saque, o programa deverá
calcular a quantidade de cédulas necessárias utilizando notas de
R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

O sistema deverá impedir saques superiores ao saldo disponível.
"""

CEDULAS = [100, 50, 20, 10, 5, 2]


def calcular_cedulas(valor):
    """Calcula a quantidade de cada cédula necessária para o saque."""
    resultado = {}
    restante = valor

    for cedula in CEDULAS:
        quantidade = restante // cedula

        if quantidade > 0:
            resultado[cedula] = quantidade
            restante %= cedula

    if restante != 0:
        raise ValueError("Não é possível formar esse valor com as cédulas disponíveis.")

    return resultado


def main():
    saldo = 1000.00

    while True:
        print("\n========== CAIXA ELETRÔNICO ==========")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "2":
            try:
                valor = float(input("Valor do depósito: R$ "))

                if valor <= 0:
                    print("O depósito deve ser positivo.")
                    continue

                saldo += valor
                print(f"Depósito realizado. Novo saldo: R$ {saldo:.2f}")

            except ValueError:
                print("Digite um valor válido.")

        elif opcao == "3":
            try:
                valor = int(input("Valor do saque (inteiro): R$ "))

                if valor <= 0:
                    print("O saque deve ser positivo.")
                    continue

                if valor > saldo:
                    print("Saldo insuficiente.")
                    continue

                cedulas = calcular_cedulas(valor)

                saldo -= valor

                print("\nSaque realizado!")
                for cedula, quantidade in cedulas.items():
                    print(f"{quantidade} cédula(s) de R$ {cedula}")

                print(f"Saldo restante: R$ {saldo:.2f}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            print("Obrigado por utilizar nosso caixa eletrônico.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()