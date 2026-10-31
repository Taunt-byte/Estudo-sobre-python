# ==========================================
# PARÂMETROS E ARGUMENTOS EM PYTHON
# ==========================================

# Parâmetros são variáveis declaradas na definição da função.
# Argumentos são os valores enviados durante a chamada.


# ==========================================
# ARGUMENTOS POSICIONAIS
# ==========================================

def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")


apresentar("Lucas", 25)


# ==========================================
# ARGUMENTOS NOMEADOS
# ==========================================

def cadastrar(nome, cidade, profissao):
    print(f"\nNome: {nome}")
    print(f"Cidade: {cidade}")
    print(f"Profissão: {profissao}")


cadastrar(
    profissao="Programador",
    nome="Lucas",
    cidade="Lorena"
)


# ==========================================
# PARÂMETROS COM VALORES PADRÃO
# ==========================================

def criar_usuario(nome, nivel="iniciante"):
    print(f"\nUsuário: {nome}")
    print(f"Nível: {nivel}")


criar_usuario("Lucas")
criar_usuario("Ana", "intermediário")


# ==========================================
# *ARGS
# ==========================================

# *args recebe vários argumentos posicionais em uma tupla.

def somar(*numeros):
    return sum(numeros)


print("\nSoma:", somar(1, 2, 3))
print("Soma:", somar(10, 20, 30, 40))


# ==========================================
# **KWARGS
# ==========================================

# **kwargs recebe vários argumentos nomeados em um dicionário.

def exibir_informacoes(**informacoes):

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")


print("\nInformações:")
exibir_informacoes(
    nome="Lucas",
    idade=25,
    cidade="Lorena",
    profissao="Desenvolvedor"
)


# ==========================================
# COMBINANDO *ARGS E **KWARGS
# ==========================================

def registrar_pedido(produto, *quantidades, **detalhes):

    print("\nProduto:", produto)
    print("Quantidades:", quantidades)
    print("Detalhes:", detalhes)


registrar_pedido(
    "Notebook",
    1,
    2,
    cor="Preto",
    marca="Dell"
)


# ==========================================
# DESEMPACOTAMENTO DE ARGUMENTOS
# ==========================================

def multiplicar(a, b, c):
    return a * b * c


valores = [2, 3, 4]

print("\nMultiplicação:", multiplicar(*valores))


dados = {
    "a": 5,
    "b": 10,
    "c": 2
}

print("Multiplicação:", multiplicar(**dados))


# ==========================================
# PARÂMETROS SOMENTE POSICIONAIS E NOMEADOS
# ==========================================

def calcular_area(largura, /, *, altura):
    return largura * altura


print("\nÁrea:", calcular_area(5, altura=10))

# largura é somente posicional.
# altura é somente nomeado.