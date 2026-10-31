# ==========================================
# MANIPULAÇÃO DE ARQUIVOS CSV
# ==========================================

import csv
from pathlib import Path

arquivo = Path("estudantes.csv")


# ==========================================
# ESCREVENDO UM CSV
# ==========================================

estudantes = [
    ["Nome", "Idade", "Nota"],
    ["Lucas", 25, 9.0],
    ["Ana", 22, 8.5],
    ["Pedro", 24, 7.0],
    ["Marina", 21, 9.5]
]

with open(arquivo, "w", newline="", encoding="utf-8") as arquivo_aberto:

    escritor = csv.writer(arquivo_aberto)

    escritor.writerows(estudantes)

print("CSV criado.")


# ==========================================
# LENDO UM CSV
# ==========================================

with open(arquivo, "r", newline="", encoding="utf-8") as arquivo_aberto:

    leitor = csv.reader(arquivo_aberto)

    print("\nConteúdo do CSV:")

    for linha in leitor:
        print(linha)


# ==========================================
# DICTREADER
# ==========================================

with open(arquivo, "r", newline="", encoding="utf-8") as arquivo_aberto:

    leitor = csv.DictReader(arquivo_aberto)

    print("\nEstudantes:")

    for estudante in leitor:
        print(
            f"Nome: {estudante['Nome']} | "
            f"Idade: {estudante['Idade']} | "
            f"Nota: {estudante['Nota']}"
        )


# ==========================================
# DICTWRITER
# ==========================================

arquivo_funcionarios = Path("funcionarios.csv")

funcionarios = [
    {"nome": "Carlos", "cargo": "Analista", "salario": 3500},
    {"nome": "Julia", "cargo": "Desenvolvedora", "salario": 5000}
]

campos = ["nome", "cargo", "salario"]

with open(
    arquivo_funcionarios,
    "w",
    newline="",
    encoding="utf-8"
) as arquivo_aberto:

    escritor = csv.DictWriter(arquivo_aberto, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(funcionarios)

print("\nArquivo de funcionários criado.")


# ==========================================
# CALCULANDO MÉDIA DAS NOTAS
# ==========================================

notas = []

with open(arquivo, "r", newline="", encoding="utf-8") as arquivo_aberto:

    leitor = csv.DictReader(arquivo_aberto)

    for estudante in leitor:
        notas.append(float(estudante["Nota"]))

if notas:
    media = sum(notas) / len(notas)
    print("\nMédia da turma:", round(media, 2))