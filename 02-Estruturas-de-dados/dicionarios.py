# ==========================================
# DICIONÁRIOS EM PYTHON
# ==========================================

# Dicionários armazenam dados no formato chave: valor.
# São mutáveis e suas chaves devem ser únicas.

pessoa = {
    "nome": "Lucas",
    "idade": 25,
    "cidade": "Lorena",
    "profissao": "Programador"
}

print("Dicionário:", pessoa)

# Acessando valores
print("\nNome:", pessoa["nome"])
print("Idade:", pessoa["idade"])

# Método get()
print("Profissão:", pessoa.get("profissao"))
print("País:", pessoa.get("pais", "Não informado"))

# Adicionando informações
pessoa["pais"] = "Brasil"

# Modificando informações
pessoa["idade"] = 26

print("\nDicionário atualizado:", pessoa)

# Removendo elementos
pessoa.pop("cidade")

print("Após remoção:", pessoa)

# Removendo o último elemento inserido
ultimo = pessoa.popitem()

print("Elemento removido:", ultimo)

# Verificando existência de uma chave
print("\nNome existe?", "nome" in pessoa)

# Obtendo chaves
print("\nChaves:", pessoa.keys())

# Obtendo valores
print("Valores:", pessoa.values())

# Obtendo pares chave: valor
print("Itens:", pessoa.items())

# Percorrendo dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Dicionários aninhados
estudantes = {
    "aluno1": {
        "nome": "Ana",
        "nota": 9.0
    },
    "aluno2": {
        "nome": "Pedro",
        "nota": 7.5
    },
    "aluno3": {
        "nome": "Marina",
        "nota": 8.5
    }
}

print("\nNome do primeiro aluno:")
print(estudantes["aluno1"]["nome"])

# Percorrendo dicionários aninhados
for identificador, dados in estudantes.items():
    print(f"\n{identificador}")
    print("Nome:", dados["nome"])
    print("Nota:", dados["nota"])

# Contagem de frequência
palavras = ["python", "java", "python", "c", "java", "python"]

frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("\nFrequência:", frequencia)

# Dictionary comprehension
quadrados = {numero: numero ** 2 for numero in range(1, 6)}

print("\nQuadrados:", quadrados)

# Atualizando vários valores
pessoa.update({
    "cidade": "Guaratinguetá",
    "idade": 27
})

print("\nResultado final:", pessoa)