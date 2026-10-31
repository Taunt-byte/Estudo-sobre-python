# ==========================================
# ENTRADA E SAÍDA EM PYTHON
# ==========================================

# ==========================================
# INPUT
# ==========================================

# input() permite receber informações do usuário.

nome = input("Digite seu nome: ")

print("Olá,", nome)


# ==========================================
# RECEBENDO NÚMEROS
# ==========================================

# input() sempre retorna uma string.
# Para trabalhar com números, precisamos converter.

numero1 = int(input("\nDigite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print("Resultado da soma:", soma)


# ==========================================
# RECEBENDO NÚMEROS DECIMAIS
# ==========================================

altura = float(input("\nDigite sua altura: "))

print("Sua altura é:", altura)


# ==========================================
# F-STRINGS
# ==========================================

nome = "Lucas"
idade = 25
salario = 2500.50

print(f"\nNome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")


# ==========================================
# FORMATAÇÃO DE SAÍDA
# ==========================================

pi = 3.14159265359

print("\nPi com duas casas decimais:", f"{pi:.2f}")

valor = 1234.5

print(f"Valor: R$ {valor:,.2f}")


# ==========================================
# TRATAMENTO DE ERROS COM TRY E EXCEPT
# ==========================================

try:

    numero = int(input("\nDigite um número inteiro: "))

    print("Dobro:", numero * 2)

except ValueError:

    print("Erro: você precisa digitar um número inteiro.")


# ==========================================
# INPUT COM STRIP
# ==========================================

cidade = input("\nDigite sua cidade: ").strip()

print(f"Você mora em {cidade}.")


# ==========================================
# INPUT COM SPLIT
# ==========================================

# Permite receber vários valores em uma única linha.

valores = input("\nDigite três números separados por espaço: ").split()

print("Valores recebidos:", valores)

# Convertendo os valores para inteiros.
numeros = [int(valor) for valor in valores]

print("Soma dos números:", sum(numeros))