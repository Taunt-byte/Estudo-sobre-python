# ==========================================
# BIBLIOTECA RANDOM
# ==========================================

import random

# ==========================================
# NÚMEROS ALEATÓRIOS
# ==========================================

# Número inteiro entre 1 e 10
numero = random.randint(1, 10)

print("Número aleatório:", numero)

# Número decimal entre 0 e 1
decimal = random.random()

print("Decimal aleatório:", decimal)

# Número decimal dentro de um intervalo
valor = random.uniform(10, 50)

print("Valor aleatório:", valor)


# ==========================================
# CHOICE()
# ==========================================

# Escolhe um elemento aleatório.

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

fruta = random.choice(frutas)

print("\nFruta escolhida:", fruta)


# ==========================================
# SAMPLE()
# ==========================================

# Seleciona vários elementos sem repetição.

numeros = list(range(1, 51))

sorteados = random.sample(numeros, 6)

print("\nNúmeros sorteados:", sorteados)


# ==========================================
# SHUFFLE()
# ==========================================

# Embaralha os elementos de uma lista.

cartas = ["Ás", "Rei", "Dama", "Valete"]

random.shuffle(cartas)

print("\nCartas embaralhadas:", cartas)


# ==========================================
# SEED()
# ==========================================

# Permite reproduzir uma sequência pseudoaleatória.

random.seed(42)

print("\nSequência reproduzível:")
print(random.randint(1, 100))
print(random.randint(1, 100))


# ==========================================
# DISTRIBUIÇÃO DE ESCOLHAS
# ==========================================

opcoes = ["Cara", "Coroa"]

resultado = random.choice(opcoes)

print("\nResultado do lançamento:", resultado)


# ==========================================
# SIMULANDO UM DADO
# ==========================================

dado = random.randint(1, 6)

print("\nResultado do dado:", dado)