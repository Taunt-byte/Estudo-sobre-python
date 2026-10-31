# ==========================================
# LEITURA DE ARQUIVOS EM PYTHON
# ==========================================

from pathlib import Path

# Caminho do arquivo
arquivo = Path("exemplo.txt")

# Criando arquivo de exemplo caso não exista
if not arquivo.exists():
    arquivo.write_text(
        "Estudando Python.\n"
        "Aprendendo manipulação de arquivos.\n"
        "Praticando programação.\n",
        encoding="utf-8"
    )


# ==========================================
# OPEN() COM READ()
# ==========================================

with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:

    conteudo = arquivo_aberto.read()

print("Conteúdo completo:")
print(conteudo)


# ==========================================
# READLINE()
# ==========================================

with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:

    primeira_linha = arquivo_aberto.readline()

print("\nPrimeira linha:")
print(primeira_linha)


# ==========================================
# READLINES()
# ==========================================

with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:

    linhas = arquivo_aberto.readlines()

print("\nLista de linhas:")
print(linhas)


# ==========================================
# PERCORRENDO LINHA POR LINHA
# ==========================================

print("\nPercorrendo arquivo:")

with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:

    for numero, linha in enumerate(arquivo_aberto, start=1):
        print(f"Linha {numero}: {linha.strip()}")


# ==========================================
# CONTANDO INFORMAÇÕES
# ==========================================

with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:

    texto = arquivo_aberto.read()

quantidade_linhas = len(texto.splitlines())
quantidade_palavras = len(texto.split())
quantidade_caracteres = len(texto)

print("\nQuantidade de linhas:", quantidade_linhas)
print("Quantidade de palavras:", quantidade_palavras)
print("Quantidade de caracteres:", quantidade_caracteres)


# ==========================================
# TRATAMENTO DE ERROS
# ==========================================

try:

    with open("arquivo_inexistente.txt", "r", encoding="utf-8") as arquivo_aberto:
        print(arquivo_aberto.read())

except FileNotFoundError:

    print("\nErro: arquivo não encontrado.")