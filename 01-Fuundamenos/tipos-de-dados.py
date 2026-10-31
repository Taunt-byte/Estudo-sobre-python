# ==========================================
# TIPOS DE DADOS EM PYTHON
# ==========================================

# STRING (str) - Texto
nome = "Python"
linguagem = "Programação"

# INTEGER (int) - Números inteiros
idade = 25
ano = 2026

# FLOAT (float) - Números decimais
altura = 1.75
preco = 29.90

# BOOLEAN (bool) - Verdadeiro ou falso
estudante = True
aprovado = False

# NONE - Ausência de valor
resultado = None

# Exibindo os valores e seus tipos
print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(estudante, type(estudante))
print(resultado, type(resultado))

# ==========================================
# CONVERSÃO DE TIPOS (CASTING)
# ==========================================

# String para inteiro
numero = "100"
numero_convertido = int(numero)

print("\nString convertida:", numero_convertido)
print("Resultado:", numero_convertido + 50)

# String para float
valor = "19.90"
valor_convertido = float(valor)

print("Float convertido:", valor_convertido)

# Inteiro para string
idade = 25
idade_texto = str(idade)

print("Idade como texto:", idade_texto)

# Inteiro para float
numero = 10
numero_decimal = float(numero)

print("Número decimal:", numero_decimal)

# ==========================================
# OPERAÇÕES COM TIPOS DE DADOS
# ==========================================

nome = "Lucas"
sobrenome = "Neves"

nome_completo = nome + " " + sobrenome

print("\nNome completo:", nome_completo)

# Concatenação de strings
print("Python " * 3)

# Verificando valores booleanos
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))