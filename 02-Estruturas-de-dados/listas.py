# ==========================================
# LISTAS EM PYTHON
# ==========================================

# Listas armazenam múltiplos valores.
# São ordenadas, mutáveis e aceitam duplicatas.

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

print("Lista:", frutas)

# Acessando elementos
print("\nPrimeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Modificando elementos
frutas[0] = "Morango"
print("Lista modificada:", frutas)

# Adicionando elementos
frutas.append("Abacaxi")
frutas.insert(1, "Melancia")

print("Após adicionar:", frutas)

# Removendo elementos
frutas.remove("Banana")
fruta_removida = frutas.pop()

print("Elemento removido:", fruta_removida)
print("Lista atual:", frutas)

# Tamanho da lista
print("\nQuantidade:", len(frutas))

# Verificando existência
print("Uva está na lista?", "Uva" in frutas)

# Percorrendo uma lista
for fruta in frutas:
    print("Fruta:", fruta)

# Ordenando elementos
numeros = [8, 2, 10, 1, 5]

numeros.sort()
print("\nOrdem crescente:", numeros)

numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)

# Funções úteis
print("\nMaior número:", max(numeros))
print("Menor número:", min(numeros))
print("Soma:", sum(numeros))

# Fatiamento (slicing)
linguagens = ["Python", "Java", "C", "JavaScript", "PHP"]

print("\nPrimeiros elementos:", linguagens[:3])
print("Últimos elementos:", linguagens[-2:])
print("Lista invertida:", linguagens[::-1])

# List comprehension
quadrados = [numero ** 2 for numero in range(1, 6)]

print("\nQuadrados:", quadrados)

pares = [numero for numero in range(1, 11) if numero % 2 == 0]

print("Números pares:", pares)

# Listas aninhadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nElemento da matriz:", matriz[1][2])

for linha in matriz:
    print(linha)

# Copiando listas
original = [10, 20, 30]
copia = original.copy()

copia.append(40)

print("\nOriginal:", original)
print("Cópia:", copia)