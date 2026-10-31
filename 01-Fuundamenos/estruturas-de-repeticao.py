# ==========================================
# ESTRUTURAS DE REPETIÇÃO EM PYTHON
# ==========================================

# ==========================================
# FOR
# ==========================================

# Repetindo uma operação cinco vezes
for numero in range(1, 6):
    print("Número:", numero)


# ==========================================
# RANGE
# ==========================================

# range(início, fim, passo)

print("\nContagem de 0 até 10:")

for numero in range(0, 11):
    print(numero)


# Contagem regressiva
print("\nContagem regressiva:")

for numero in range(10, 0, -1):
    print(numero)


# ==========================================
# PERCORRENDO LISTAS
# ==========================================

linguagens = ["Python", "JavaScript", "C", "Java"]

for linguagem in linguagens:
    print("\nLinguagem:", linguagem)


# ==========================================
# WHILE
# ==========================================

contador = 1

while contador <= 5:
    print("\nContador:", contador)
    contador += 1


# ==========================================
# BREAK
# ==========================================

# Interrompe a repetição.

for numero in range(1, 10):

    if numero == 5:
        break

    print("\nBreak:", numero)


# ==========================================
# CONTINUE
# ==========================================

# Pula a repetição atual.

for numero in range(1, 6):

    if numero == 3:
        continue

    print("\nContinue:", numero)


# ==========================================
# LOOPS ANINHADOS
# ==========================================

for linha in range(1, 4):

    for coluna in range(1, 4):

        print(f"Linha {linha} | Coluna {coluna}")


# ==========================================
# ENUMERATE
# ==========================================

frutas = ["Maçã", "Banana", "Uva"]

for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice} - {fruta}")


# ==========================================
# ELSE EM ESTRUTURAS DE REPETIÇÃO
# ==========================================

for numero in range(1, 4):
    print("Executando:", numero)
else:
    print("Repetição concluída!")