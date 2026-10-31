# ==========================================
# VARIÁVEIS EM PYTHON
# ==========================================

# Variáveis armazenam referências para valores.

nome = "Lucas"
idade = 25
altura = 1.75
estudante = True

# Exibindo os valores
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É estudante?", estudante)

# Alterando o valor de uma variável
idade = 26

print("\nIdade atualizada:", idade)

# Variáveis podem ser utilizadas em cálculos
preco_produto = 49.90
quantidade = 3

total = preco_produto * quantidade

print(f"Valor total: R$ {total:.2f}")

# Atribuindo valores a múltiplas variáveis
a, b, c = 10, 20, 30

print("\nValores:")
print(a, b, c)

# Atribuindo o mesmo valor a várias variáveis
x = y = z = 100

print(x, y, z)

# Verificando o tipo de uma variável
print("\nTipo de nome:", type(nome))
print("Tipo de idade:", type(idade))
print("Tipo de altura:", type(altura))
print("Tipo de estudante:", type(estudante))