# ==========================================
# MANIPULAÇÃO DE ARQUIVOS JSON
# ==========================================

import json
from pathlib import Path

arquivo = Path("dados.json")


# ==========================================
# DADOS PYTHON
# ==========================================

pessoa = {
    "nome": "Lucas",
    "idade": 25,
    "cidade": "Lorena",
    "linguagens": ["Python", "JavaScript", "C"],
    "estudante": True
}


# ==========================================
# JSON DUMP()
# ==========================================

# Salva os dados Python em um arquivo JSON.

with open(arquivo, "w", encoding="utf-8") as arquivo_aberto:

    json.dump(
        pessoa,
        arquivo_aberto,
        ensure_ascii=False,
        indent=4
    )

print("Arquivo JSON criado.")


# ==========================================
# JSON LOAD()
# ==========================================

# Lê um arquivo JSON e converte para estruturas Python.

with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:

    dados = json.load(arquivo_aberto)

print("\nDados carregados:")
print(dados)

print("Nome:", dados["nome"])
print("Idade:", dados["idade"])


# ==========================================
# JSON DUMPS()
# ==========================================

# Converte um objeto Python em uma string JSON.

json_texto = json.dumps(
    pessoa,
    ensure_ascii=False,
    indent=4
)

print("\nJSON como texto:")
print(json_texto)


# ==========================================
# JSON LOADS()
# ==========================================

# Converte uma string JSON em um objeto Python.

texto_json = '{"nome": "Ana", "idade": 22}'

dados_convertidos = json.loads(texto_json)

print("\nDados convertidos:")
print(dados_convertidos)


# ==========================================
# ATUALIZANDO UM ARQUIVO JSON
# ==========================================

dados["idade"] = 26
dados["profissao"] = "Desenvolvedor"

with open(arquivo, "w", encoding="utf-8") as arquivo_aberto:

    json.dump(
        dados,
        arquivo_aberto,
        ensure_ascii=False,
        indent=4
    )

print("\nJSON atualizado.")


# ==========================================
# TRATAMENTO DE ERROS
# ==========================================

try:

    with open("invalido.json", "r", encoding="utf-8") as arquivo_aberto:
        dados = json.load(arquivo_aberto)

except FileNotFoundError:

    print("\nErro: arquivo não encontrado.")

except json.JSONDecodeError:

    print("\nErro: conteúdo JSON inválido.")