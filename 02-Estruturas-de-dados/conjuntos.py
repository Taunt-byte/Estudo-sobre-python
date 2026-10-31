# ==========================================
# CONJUNTOS (SETS) EM PYTHON
# ==========================================

# Sets armazenam elementos únicos.
# Não possuem índices e não garantem ordem de exibição.

numeros = {1, 2, 3, 4, 5, 5, 5}

print("Conjunto:", numeros)

# Criando um conjunto vazio
conjunto_vazio = set()

print("\nConjunto vazio:", conjunto_vazio)

# Adicionando elementos
numeros.add(6)
numeros.add(7)

print("Após adicionar:", numeros)

# Adicionando múltiplos elementos
numeros.update([8, 9, 10])

print("Após update:", numeros)

# Removendo elementos
numeros.remove(3)

print("\nApós remove:", numeros)

# discard não gera erro se o elemento não existir
numeros.discard(100)

# Verificando existência
print("O número 5 existe?", 5 in numeros)

# Tamanho do conjunto
print("Quantidade de elementos:", len(numeros))

# Percorrendo conjunto
for numero in numeros:
    print("Número:", numero)

# ==========================================
# OPERAÇÕES ENTRE CONJUNTOS
# ==========================================

python = {"Lucas", "Ana", "Pedro", "Marina"}
javascript = {"Ana", "Carlos", "Marina", "João"}

# União
print("\nUnião:", python | javascript)

# Interseção
print("Interseção:", python & javascript)

# Diferença
print("Somente Python:", python - javascript)

# Diferença simétrica
print("Diferença simétrica:", python ^ javascript)

# Métodos equivalentes
print("\nUnião:", python.union(javascript))
print("Interseção:", python.intersection(javascript))

# ==========================================
# REMOVENDO DUPLICATAS
# ==========================================

lista = [1, 2, 2, 3, 3, 4, 5, 5]

lista_sem_duplicatas = list(set(lista))

print("\nLista original:", lista)
print("Sem duplicatas:", lista_sem_duplicatas)

# ==========================================
# FROZENSET
# ==========================================

# frozenset é um conjunto imutável.

dias = frozenset(["Segunda", "Terça", "Quarta"])

print("\nFrozenSet:", dias)

# Não é permitido adicionar ou remover elementos.
# dias.add("Quinta")  # Causaria AttributeError.