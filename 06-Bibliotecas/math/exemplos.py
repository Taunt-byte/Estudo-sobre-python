# ==========================================
# BIBLIOTECA MATH
# ==========================================

import math

# ==========================================
# CONSTANTES MATEMÁTICAS
# ==========================================

print("Pi:", math.pi)
print("Euler:", math.e)
print("Infinito:", math.inf)


# ==========================================
# RAIZ QUADRADA
# ==========================================

numero = 25

print("\nRaiz quadrada:", math.sqrt(numero))


# ==========================================
# POTENCIAÇÃO
# ==========================================

print("\nPotência:", math.pow(2, 3))


# ==========================================
# ARREDONDAMENTO
# ==========================================

numero = 7.8

print("\nArredondamento para cima:", math.ceil(numero))
print("Arredondamento para baixo:", math.floor(numero))


# ==========================================
# VALOR ABSOLUTO
# ==========================================

print("\nValor absoluto:", math.fabs(-25))


# ==========================================
# FATORIAL
# ==========================================

print("\nFatorial:", math.factorial(5))


# ==========================================
# MDC E MMC
# ==========================================

print("\nMDC:", math.gcd(24, 36))
print("MMC:", math.lcm(24, 36))


# ==========================================
# LOGARITMOS
# ==========================================

print("\nLogaritmo natural:", math.log(10))
print("Logaritmo base 10:", math.log10(100))
print("Logaritmo base 2:", math.log2(8))


# ==========================================
# TRIGONOMETRIA
# ==========================================

angulo = math.radians(90)

print("\nSeno:", math.sin(angulo))
print("Cosseno:", math.cos(angulo))
print("Tangente:", math.tan(angulo))


# ==========================================
# DISTÂNCIA ENTRE PONTOS
# ==========================================

ponto_a = (0, 0)
ponto_b = (3, 4)

distancia = math.dist(ponto_a, ponto_b)

print("\nDistância:", distancia)


# ==========================================
# SOMA PRECISA
# ==========================================

valores = [0.1, 0.1, 0.1, 0.1, 0.1]

print("\nSoma precisa:", math.fsum(valores))