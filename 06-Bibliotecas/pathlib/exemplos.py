# ==========================================
# BIBLIOTECA PATHLIB
# ==========================================

from pathlib import Path

# Criando um caminho
caminho = Path("documentos")

print("Caminho:", caminho)


# ==========================================
# DIRETÓRIO ATUAL
# ==========================================

print("\nDiretório atual:", Path.cwd())


# ==========================================
# CRIANDO PASTAS
# ==========================================

pasta = Path("documentos")

pasta.mkdir(exist_ok=True)

print("\nPasta criada.")


# Criando pastas aninhadas
subpasta = Path("documentos/estudos/python")

subpasta.mkdir(parents=True, exist_ok=True)


# ==========================================
# CRIANDO ARQUIVOS
# ==========================================

arquivo = pasta / "anotacoes.txt"

arquivo.write_text(
    "Estudando a biblioteca pathlib.",
    encoding="utf-8"
)


# ==========================================
# LENDO ARQUIVOS
# ==========================================

conteudo = arquivo.read_text(encoding="utf-8")

print("\nConteúdo:")
print(conteudo)


# ==========================================
# INFORMAÇÕES DO CAMINHO
# ==========================================

print("\nNome:", arquivo.name)
print("Extensão:", arquivo.suffix)
print("Nome sem extensão:", arquivo.stem)
print("Diretório pai:", arquivo.parent)


# ==========================================
# VERIFICANDO EXISTÊNCIA
# ==========================================

print("\nExiste?", arquivo.exists())
print("É arquivo?", arquivo.is_file())
print("É pasta?", pasta.is_dir())


# ==========================================
# LISTANDO ARQUIVOS
# ==========================================

print("\nArquivos TXT:")

for item in Path(".").glob("*.txt"):
    print(item)


# Busca recursiva
print("\nTodos os arquivos Python:")

for item in Path(".").rglob("*.py"):
    print(item)


# ==========================================
# TAMANHO DE ARQUIVO
# ==========================================

print("\nTamanho:", arquivo.stat().st_size, "bytes")


# ==========================================
# RENOMEANDO E MOVENDO
# ==========================================

# Descomente para testar:
# arquivo.rename(pasta / "novo_nome.txt")


# ==========================================
# REMOVENDO ARQUIVOS
# ==========================================

# Descomente para testar:
# arquivo.unlink()