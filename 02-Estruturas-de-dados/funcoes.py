# ==========================================
# FUNÇÕES EM PYTHON
# ==========================================

# Funções permitem organizar e reutilizar código.

# Criando uma função simples
def saudacao():
    print("Olá! Bem-vindo ao Python.")


# Chamando a função
saudacao()


# ==========================================
# FUNÇÕES COM PARÂMETROS
# ==========================================

def apresentar(nome):
    print(f"Olá, {nome}!")


apresentar("Lucas")
apresentar("Marina")


# ==========================================
# FUNÇÕES COM RETORNO
# ==========================================

def somar(a, b):
    return a + b


resultado = somar(10, 20)

print("\nResultado:", resultado)


# ==========================================
# FUNÇÕES COM MÚLTIPLOS RETORNOS
# ==========================================

def calcular(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b

    return soma, subtracao, multiplicacao


soma, subtracao, multiplicacao = calcular(10, 5)

print("\nSoma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)


# ==========================================
# VALORES PADRÃO
# ==========================================

def apresentar_pessoa(nome, cidade="Não informada"):
    print(f"{nome} mora em {cidade}.")


apresentar_pessoa("Lucas", "Lorena")
apresentar_pessoa("Ana")


# ==========================================
# FUNÇÕES COM CONDICIONAIS
# ==========================================

def verificar_idade(idade):

    if idade >= 18:
        return "Maior de idade"

    return "Menor de idade"


print("\n", verificar_idade(20))
print(verificar_idade(15))


# ==========================================
# FUNÇÕES COM LISTAS
# ==========================================

def calcular_media(notas):

    if not notas:
        return None

    return sum(notas) / len(notas)


notas = [8, 7, 9, 10]

media = calcular_media(notas)

print("\nMédia:", media)


# ==========================================
# ESCOPO DE VARIÁVEIS
# ==========================================

nome = "Lucas"


def mostrar_nome():
    nome_local = "Python"
    print("\nVariável local:", nome_local)
    print("Variável global:", nome)


mostrar_nome()


# ==========================================
# DOCSTRINGS
# ==========================================

def calcular_area(largura, altura):
    """
    Calcula a área de um retângulo.

    Args:
        largura: largura do retângulo.
        altura: altura do retângulo.

    Returns:
        Área calculada.
    """
    return largura * altura


print("\nÁrea:", calcular_area(5, 10))


# ==========================================
# MAIN
# ==========================================

def main():
    print("\nPrograma iniciado.")
    saudacao()


if __name__ == "__main__":
    main()