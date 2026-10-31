# ==========================================
# TUPLAS EM PYTHON
# ==========================================

# Tuplas armazenam múltiplos valores.
# São ordenadas e imutáveis.

coordenadas = (23.18, 45.88)

print("Tupla:", coordenadas)

# Acessando elementos
print("\nLatitude:", coordenadas[0])
print("Longitude:", coordenadas[1])

# Tupla com diferentes tipos
pessoa = ("Lucas", 25, 1.75, True)

print("\nPessoa:", pessoa)

# Desempacotamento
nome, idade, altura, estudante = pessoa

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudante:", estudante)

# Contando elementos
numeros = (1, 2, 3, 2, 4, 2, 5)

print("\nQuantidade de elementos:", len(numeros))
print("Quantidade de números 2:", numeros.count(2))

# Localizando elementos
print("Índice do número 4:", numeros.index(4))

# Percorrendo uma tupla
for numero in numeros:
    print("Número:", numero)

# Verificando existência
print("\nO número 3 existe?", 3 in numeros)

# Fatiamento
linguagens = ("Python", "Java", "C", "JavaScript")

print("\nPrimeiros elementos:", linguagens[:2])
print("Últimos elementos:", linguagens[-2:])

# Tupla com um único elemento
unico_elemento = ("Python",)

print("\nTipo:", type(unico_elemento))

# Convertendo lista em tupla
lista = [10, 20, 30]

tupla = tuple(lista)

print("\nLista:", lista)
print("Tupla:", tupla)

# Convertendo tupla em lista
nova_lista = list(tupla)

nova_lista.append(40)

print("Lista modificada:", nova_lista)

# Tuplas aninhadas
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("\nElemento:", matriz[1][1])

for linha in matriz:
    print(linha)