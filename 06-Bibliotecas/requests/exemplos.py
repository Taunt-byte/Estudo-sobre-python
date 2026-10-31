# ==========================================
# BIBLIOTECA REQUESTS
# ==========================================

# Instalação:
# pip install requests

import requests


# ==========================================
# PRIMEIRA REQUISIÇÃO HTTP
# ==========================================

url = "https://jsonplaceholder.typicode.com/posts/1"

try:

    resposta = requests.get(url, timeout=10)

    print("Status HTTP:", resposta.status_code)

    resposta.raise_for_status()

    print("\nConteúdo:")
    print(resposta.text)

except requests.exceptions.RequestException as erro:

    print("Erro na requisição:", erro)


# ==========================================
# CONVERTENDO RESPOSTA JSON
# ==========================================

url = "https://jsonplaceholder.typicode.com/users/1"

try:

    resposta = requests.get(url, timeout=10)

    resposta.raise_for_status()

    usuario = resposta.json()

    print("\nInformações do usuário:")
    print("Nome:", usuario["name"])
    print("E-mail:", usuario["email"])
    print("Cidade:", usuario["address"]["city"])

except (requests.exceptions.RequestException, ValueError, KeyError) as erro:

    print("Erro ao obter usuário:", erro)


# ==========================================
# PARÂMETROS DE URL
# ==========================================

url = "https://jsonplaceholder.typicode.com/posts"

parametros = {
    "userId": 1
}

try:

    resposta = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    resposta.raise_for_status()

    publicacoes = resposta.json()

    print("\nPublicações:")

    for publicacao in publicacoes:
        print(publicacao["title"])

except requests.exceptions.RequestException as erro:

    print("Erro:", erro)


# ==========================================
# ENVIANDO DADOS COM POST
# ==========================================

url = "https://jsonplaceholder.typicode.com/posts"

dados = {
    "title": "Meu primeiro projeto Python",
    "body": "Estudando requisições HTTP.",
    "userId": 1
}

try:

    resposta = requests.post(
        url,
        json=dados,
        timeout=10
    )

    resposta.raise_for_status()

    resultado = resposta.json()

    print("\nPublicação criada:")
    print(resultado)

except requests.exceptions.RequestException as erro:

    print("Erro ao enviar dados:", erro)


# ==========================================
# HEADERS
# ==========================================

cabecalhos = {
    "Accept": "application/json",
    "User-Agent": "Python-Study-Project"
}

try:

    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=cabecalhos,
        timeout=10
    )

    resposta.raise_for_status()

    print("\nHeaders enviados com sucesso.")

except requests.exceptions.RequestException as erro:

    print("Erro:", erro)