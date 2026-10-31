# ==========================================
# ENCAPSULAMENTO EM PYTHON
# ==========================================

# Encapsulamento organiza o acesso aos atributos
# e protege o estado interno dos objetos.


# ==========================================
# ATRIBUTOS PÚBLICOS
# ==========================================

class Pessoa:

    def __init__(self, nome):
        self.nome = nome


pessoa = Pessoa("Lucas")

print("Nome:", pessoa.nome)


# ==========================================
# ATRIBUTOS PROTEGIDOS (CONVENÇÃO)
# ==========================================

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario


funcionario = Funcionario("Ana", 3000)

# O underscore indica que o atributo é destinado
# ao uso interno da classe, mas não impede acesso.
print("\nSalário:", funcionario._salario)


# ==========================================
# ATRIBUTOS PRIVADOS (NAME MANGLING)
# ==========================================

class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, valor):

        if valor <= 0:
            print("Valor de depósito inválido.")
            return

        self.__saldo += valor
        print("Depósito realizado.")

    def sacar(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return

        self.__saldo -= valor
        print("Saque realizado.")


conta = ContaBancaria("Lucas", 1000)

print("\nSaldo:", conta.consultar_saldo())

conta.depositar(500)
conta.sacar(200)

print("Saldo atualizado:", conta.consultar_saldo())


# ==========================================
# PROPERTY
# ==========================================

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):

        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")

        self.__preco = valor


produto = Produto("Notebook", 3500)

print("\nProduto:", produto.nome)
print("Preço:", produto.preco)

produto.preco = 4000

print("Novo preço:", produto.preco)


# ==========================================
# PROPERTY COM ATRIBUTO CALCULADO
# ==========================================

class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura


retangulo = Retangulo(10, 5)

print("\nÁrea do retângulo:", retangulo.area)