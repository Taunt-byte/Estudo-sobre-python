# ==========================================
# RECURSIVIDADE EM PYTHON
# ==========================================

# Recursividade acontece quando uma função chama a si mesma.
# Toda recursão precisa de um caso-base para terminar.


# ==========================================
# CONTAGEM REGRESSIVA
# ==========================================

def contagem_regressiva(numero):

    if numero == 0:
        print("Fim!")
        return

    print(numero)

    contagem_regressiva(numero - 1)


print("Contagem regressiva:")
contagem_regressiva(5)


# ==========================================
# FATORIAL
# ==========================================

# 5! = 5 * 4 * 3 * 2 * 1

def fatorial(numero):

    if numero < 0:
        raise ValueError("O fatorial não está definido para negativos.")

    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)


print("\nFatorial de 5:", fatorial(5))


# ==========================================
# FIBONACCI
# ==========================================

# Sequência: 0, 1, 1, 2, 3, 5, 8...

def fibonacci(numero):

    if numero < 0:
        raise ValueError("Informe um número não negativo.")

    if numero <= 1:
        return numero

    return fibonacci(numero - 1) + fibonacci(numero - 2)


print("\nFibonacci de 6:", fibonacci(6))


# ==========================================
# SOMA DE UMA LISTA
# ==========================================

def somar_lista(lista):

    if not lista:
        return 0

    return lista[0] + somar_lista(lista[1:])


numeros = [10, 20, 30, 40]

print("\nSoma da lista:", somar_lista(numeros))


# ==========================================
# POTENCIAÇÃO
# ==========================================

def potencia(base, expoente):

    if expoente < 0:
        return 1 / potencia(base, -expoente)

    if expoente == 0:
        return 1

    return base * potencia(base, expoente - 1)


print("\nPotência:", potencia(2, 5))


# ==========================================
# MÁXIMO DIVISOR COMUM (EUCLIDES)
# ==========================================

def mdc(a, b):

    if b == 0:
        return abs(a)

    return mdc(b, a % b)


print("\nMDC de 48 e 18:", mdc(48, 18))


# ==========================================
# OBSERVAÇÃO
# ==========================================

# Recursão pode deixar alguns algoritmos mais simples.
# Entretanto, muitas chamadas podem consumir memória
# e atingir o limite de profundidade de recursão do Python.