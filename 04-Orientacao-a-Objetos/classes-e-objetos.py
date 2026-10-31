# ==========================================
# CLASSES E OBJETOS EM PYTHON
# ==========================================

# Classes são modelos para criar objetos.
# Objetos possuem atributos e métodos.


# ==========================================
# CRIANDO UMA CLASSE
# ==========================================

class Pessoa:

    def __init__(self, nome, idade):
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}.")

    def aniversario(self):
        self.idade += 1
        print(f"Agora tenho {self.idade} anos.")


# Criando objetos
pessoa1 = Pessoa("Lucas", 25)
pessoa2 = Pessoa("Ana", 22)

# Acessando atributos
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)

# Chamando métodos
pessoa1.apresentar()
pessoa1.aniversario()

pessoa2.apresentar()


# ==========================================
# ATRIBUTOS DE CLASSE
# ==========================================

class Carro:

    quantidade_rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"{self.marca} {self.modelo}")
        print(f"Rodas: {self.quantidade_rodas}")


carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

carro1.exibir_informacoes()


# ==========================================
# MÉTODOS DE CLASSE
# ==========================================

class Produto:

    desconto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco(self):
        return self.preco * (1 - self.desconto_padrao)


produto = Produto("Notebook", 3000)

print("\nPreço com desconto:", produto.calcular_preco())


# ==========================================
# MÉTODOS ESTÁTICOS
# ==========================================

class Calculadora:

    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def multiplicar(a, b):
        return a * b


print("\nSoma:", Calculadora.somar(10, 20))
print("Multiplicação:", Calculadora.multiplicar(5, 4))


# ==========================================
# REPRESENTAÇÃO DE OBJETOS
# ==========================================

class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


livro = Livro("Dom Casmurro", "Machado de Assis")

print("\nLivro:", livro)