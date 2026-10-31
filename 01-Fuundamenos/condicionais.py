# ==========================================
# ESTRUTURAS CONDICIONAIS EM PYTHON
# ==========================================

# ==========================================
# IF, ELIF E ELSE
# ==========================================

idade = 20

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# ==========================================
# VERIFICANDO NOTAS
# ==========================================

nota = 7.5

if nota >= 7:
    print("\nAprovado!")
elif nota >= 5:
    print("\nRecuperação!")
else:
    print("\nReprovado!")


# ==========================================
# MÚLTIPLAS CONDIÇÕES
# ==========================================

idade = 25
possui_carteira = True

if idade >= 18 and possui_carteira:
    print("\nPode dirigir.")
else:
    print("\nNão pode dirigir.")


# ==========================================
# OPERADORES LÓGICOS
# ==========================================

temperatura = 30

if temperatura >= 25 and temperatura <= 35:
    print("\nTemperatura agradável.")

if temperatura < 15 or temperatura > 35:
    print("Temperatura extrema.")


# ==========================================
# CONDICIONAL ANINHADA
# ==========================================

usuario = "admin"
senha = "123456"

if usuario == "admin":
    if senha == "123456":
        print("\nLogin realizado com sucesso!")
    else:
        print("\nSenha incorreta.")
else:
    print("\nUsuário não encontrado.")


# ==========================================
# OPERADOR TERNÁRIO
# ==========================================

numero = 10

resultado = "Par" if numero % 2 == 0 else "Ímpar"

print("\nO número é:", resultado)


# ==========================================
# MATCH CASE (PYTHON 3.10+)
# ==========================================

opcao = 2

match opcao:
    case 1:
        print("\nOpção selecionada: Cadastrar")
    case 2:
        print("\nOpção selecionada: Consultar")
    case 3:
        print("\nOpção selecionada: Excluir")
    case _:
        print("\nOpção inválida.")