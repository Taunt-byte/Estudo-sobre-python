# ==========================================
# OPERADORES EM PYTHON
# ==========================================

# ==========================================
# OPERADORES ARITMÉTICOS
# ==========================================

a = 20
b = 5

print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Resto da divisão:", a % b)
print("Potenciação:", a ** b)

# ==========================================
# OPERADORES DE COMPARAÇÃO
# ==========================================

x = 10
y = 20

print("\nIgual:", x == y)
print("Diferente:", x != y)
print("Maior:", x > y)
print("Menor:", x < y)
print("Maior ou igual:", x >= y)
print("Menor ou igual:", x <= y)

# ==========================================
# OPERADORES LÓGICOS
# ==========================================

idade = 22
possui_documento = True

print("\nAND:", idade >= 18 and possui_documento)
print("OR:", idade < 18 or idade >= 60)
print("NOT:", not possui_documento)

# ==========================================
# OPERADORES DE ATRIBUIÇÃO
# ==========================================

numero = 10

numero += 5
print("\nSoma e atribuição:", numero)

numero -= 3
print("Subtração e atribuição:", numero)

numero *= 2
print("Multiplicação e atribuição:", numero)

numero /= 4
print("Divisão e atribuição:", numero)

# ==========================================
# OPERADORES DE IDENTIDADE
# ==========================================

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print("\nlista_a is lista_b:", lista_a is lista_b)
print("lista_a is lista_c:", lista_a is lista_c)
print("lista_a == lista_c:", lista_a == lista_c)

# ==========================================
# OPERADORES DE PERTENCIMENTO
# ==========================================

linguagens = ["Python", "JavaScript", "C"]

print("\nPython está na lista?", "Python" in linguagens)
print("Java está na lista?", "Java" in linguagens)
print("Java não está na lista?", "Java" not in linguagens)