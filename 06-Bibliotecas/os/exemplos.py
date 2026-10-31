# ==========================================
# BIBLIOTECA OS
# ==========================================

import os

# Diretório atual
print("Diretório atual:")
print(os.getcwd())


# ==========================================
# LISTANDO ARQUIVOS
# ==========================================

print("\nArquivos e pastas:")

for item in os.listdir("."):
    print(item)


# ==========================================
# CRIANDO DIRETÓRIOS
# ==========================================

os.makedirs("pasta_teste/subpasta", exist_ok=True)

print("\nDiretório criado.")


# ==========================================
# VERIFICANDO ARQUIVOS
# ==========================================

print("\nExiste pasta_teste?", os.path.exists("pasta_teste"))
print("É diretório?", os.path.isdir("pasta_teste"))
print("É arquivo?", os.path.isfile("exemplo.txt"))


# ==========================================
# INFORMAÇÕES DE ARQUIVOS
# ==========================================

arquivo = "exemplo.txt"

if os.path.isfile(arquivo):

    informacoes = os.stat(arquivo)

    print("\nTamanho:", informacoes.st_size, "bytes")


# ==========================================
# CAMINHOS
# ==========================================

caminho = os.path.join("pasta_teste", "arquivo.txt")

print("\nCaminho:", caminho)
print("Nome:", os.path.basename(caminho))
print("Diretório:", os.path.dirname(caminho))


# ==========================================
# VARIÁVEIS DE AMBIENTE
# ==========================================

print("\nSistema operacional:", os.name)

print("Diretório HOME:", os.environ.get("HOME"))
print("Usuário:", os.environ.get("USERNAME") or os.environ.get("USER"))


# ==========================================
# REMOVENDO ARQUIVOS E DIRETÓRIOS
# ==========================================

# Descomente para testar:

# os.remove("arquivo.txt")
# os.rmdir("pasta_vazia")