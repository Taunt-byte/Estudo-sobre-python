# ==========================================
# ESCRITA DE ARQUIVOS EM PYTHON
# ==========================================

from pathlib import Path

arquivo = Path("anotacoes.txt")


# ==========================================
# MODO W - ESCREVER
# ==========================================

# Cria o arquivo ou substitui seu conteúdo.

with open(arquivo, "w", encoding="utf-8") as arquivo_aberto:

    arquivo_aberto.write("Primeira anotação.\n")
    arquivo_aberto.write("Estudando Python.\n")

print("Arquivo criado.")


# ==========================================
# MODO A - ADICIONAR
# ==========================================

# Adiciona conteúdo sem apagar o anterior.

with open(arquivo, "a", encoding="utf-8") as arquivo_aberto:

    arquivo_aberto.write("Nova anotação adicionada.\n")

print("Conteúdo adicionado.")


# ==========================================
# WRITELINES()
# ==========================================

linhas = [
    "Aprender Python.\n",
    "Praticar exercícios.\n",
    "Desenvolver projetos.\n"
]

with open(arquivo, "w", encoding="utf-8") as arquivo_aberto:

    arquivo_aberto.writelines(linhas)

print("Linhas gravadas.")


# ==========================================
# PATHLIB
# ==========================================

# Forma mais moderna de trabalhar com arquivos.

novo_arquivo = Path("novo_arquivo.txt")

novo_arquivo.write_text(
    "Arquivo criado usando pathlib.",
    encoding="utf-8"
)

conteudo = novo_arquivo.read_text(encoding="utf-8")

print("\nConteúdo:", conteudo)


# ==========================================
# VERIFICANDO ARQUIVOS
# ==========================================

print("\nExiste?", arquivo.exists())
print("É arquivo?", arquivo.is_file())
print("Tamanho:", arquivo.stat().st_size, "bytes")


# ==========================================
# TRATAMENTO DE ERROS
# ==========================================

try:

    with open("pasta/arquivo.txt", "w", encoding="utf-8") as arquivo_aberto:
        arquivo_aberto.write("Conteúdo")

except OSError as erro:

    print("\nErro ao escrever arquivo:", erro)