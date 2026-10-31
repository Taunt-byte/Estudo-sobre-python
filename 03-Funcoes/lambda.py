# ==========================================
# FUNÇÕES LAMBDA EM PYTHON
# ==========================================

# Lambda cria funções pequenas e anônimas.
# Sintaxe: lambda argumentos: expressão


# ==========================================
# LAMBDA SIMPLES
# ==========================================

dobrar = lambda numero: numero * 2

print("Dobro:", dobrar(5))


# ==========================================
# LAMBDA COM DOIS ARGUMENTOS
# ==========================================

somar = lambda a, b: a + b

print("\nSoma:", somar(10, 20))


# ==========================================
# LAMBDA COM CONDICIONAL
# ==========================================

verificar = lambda numero: "Par" if numero % 2 == 0 else "Ímpar"

print("\nNúmero 10:", verificar(10))
print("Número 7:", verificar(7))


# ==========================================
# LAMBDA COM MAP()
# ==========================================

# map aplica uma função a cada elemento de um iterável.

numeros = [1, 2, 3, 4, 5]

quadrados = list(map(lambda numero: numero ** 2, numeros))

print("\nQuadrados:", quadrados)


# ==========================================
# LAMBDA COM FILTER()
# ==========================================

# filter seleciona elementos que atendem a uma condição.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda numero: numero % 2 == 0, numeros))

print("\nNúmeros pares:", pares)


# ==========================================
# LAMBDA COM SORTED()
# ==========================================

pessoas = [
    {"nome": "Lucas", "idade": 25},
    {"nome": "Ana", "idade": 20},
    {"nome": "Pedro", "idade": 30}
]

ordenados = sorted(pessoas, key=lambda pessoa: pessoa["idade"])

print("\nPessoas por idade:")

for pessoa in ordenados:
    print(pessoa)


# ==========================================
# LAMBDA COM REDUCE()
# ==========================================

from functools import reduce

numeros = [1, 2, 3, 4, 5]

produto = reduce(lambda a, b: a * b, numeros)

print("\nProduto dos números:", produto)


# ==========================================
# LAMBDA COMO ARGUMENTO
# ==========================================

def executar_operacao(a, b, operacao):
    return operacao(a, b)


resultado = executar_operacao(10, 5, lambda a, b: a - b)

print("\nResultado:", resultado)


# ==========================================
# OBSERVAÇÃO
# ==========================================

# Prefira def quando a lógica for extensa.
# Lambda é mais indicada para expressões pequenas.