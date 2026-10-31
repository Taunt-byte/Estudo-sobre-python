# ==========================================
# MANIPULAÇÃO DE STRINGS EM PYTHON
# ==========================================

# Strings representam sequências de caracteres.
# São imutáveis.

texto = "Aprendendo Python"

print("Texto:", texto)

# ==========================================
# ACESSANDO CARACTERES
# ==========================================

print("\nPrimeiro caractere:", texto[0])
print("Último caractere:", texto[-1])

# ==========================================
# MAIÚSCULAS E MINÚSCULAS
# ==========================================

print("\nMaiúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Título:", texto.title())
print("Capitalizada:", texto.capitalize())
print("Troca maiúsculas/minúsculas:", texto.swapcase())

# ==========================================
# REMOVENDO ESPAÇOS
# ==========================================

frase = "   Aprender Python é interessante!   "

print("\nOriginal:", repr(frase))
print("Strip:", frase.strip())
print("Lstrip:", frase.lstrip())
print("Rstrip:", frase.rstrip())

# ==========================================
# SUBSTITUINDO CARACTERES
# ==========================================

frase = "Eu estudo Java"

nova_frase = frase.replace("Java", "Python")

print("\nOriginal:", frase)
print("Modificada:", nova_frase)

# ==========================================
# DIVIDINDO E JUNTANDO STRINGS
# ==========================================

frase = "Python Java JavaScript C"

linguagens = frase.split()

print("\nLista:", linguagens)

nova_frase = " - ".join(linguagens)

print("Texto:", nova_frase)

# ==========================================
# LOCALIZANDO CARACTERES E PALAVRAS
# ==========================================

texto = "Programação com Python"

print("\nPosição de Python:", texto.find("Python"))
print("Contém Python?", "Python" in texto)
print("Quantidade de letras 'o':", texto.count("o"))

# ==========================================
# VERIFICANDO CONTEÚDO
# ==========================================

print("\nÉ alfanumérico?", "Python123".isalnum())
print("É alfabético?", "Python".isalpha())
print("É numérico?", "12345".isdigit())
print("Está em maiúsculas?", "PYTHON".isupper())
print("Está em minúsculas?", "python".islower())
print("Começa com Pro?", texto.startswith("Pro"))
print("Termina com Python?", texto.endswith("Python"))

# ==========================================
# FATIAMENTO (SLICING)
# ==========================================

linguagem = "Python"

print("\nPrimeiros três caracteres:", linguagem[:3])
print("Últimos três caracteres:", linguagem[-3:])
print("Do segundo ao quinto:", linguagem[1:5])
print("Texto invertido:", linguagem[::-1])

# ==========================================
# F-STRINGS
# ==========================================

nome = "Lucas"
idade = 25
altura = 1.75

mensagem = f"Meu nome é {nome}, tenho {idade} anos e {altura:.2f}m."

print("\n" + mensagem)

# ==========================================
# CONTAGEM DE PALAVRAS
# ==========================================

frase = "Python é uma linguagem de programação muito interessante"

palavras = frase.split()

print("\nQuantidade de palavras:", len(palavras))
print("Palavra mais longa:", max(palavras, key=len))

# ==========================================
# INVERSÃO DE TEXTO
# ==========================================

palavra = "radar"

if palavra == palavra[::-1]:
    print("\nA palavra é um palíndromo.")
else:
    print("\nA palavra não é um palíndromo.")