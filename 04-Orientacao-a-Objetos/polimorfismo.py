# ==========================================
# POLIMORFISMO EM PYTHON
# ==========================================

# Polimorfismo permite utilizar uma mesma interface
# com diferentes implementações.


# ==========================================
# POLIMORFISMO COM HERANÇA
# ==========================================

class Animal:

    def emitir_som(self):
        print("Som de animal.")


class Cachorro(Animal):

    def emitir_som(self):
        print("Au au!")


class Gato(Animal):

    def emitir_som(self):
        print("Miau!")


class Vaca(Animal):

    def emitir_som(self):
        print("Muuu!")


animais = [
    Cachorro(),
    Gato(),
    Vaca()
]

for animal in animais:
    animal.emitir_som()


# ==========================================
# POLIMORFISMO COM MÉTODOS
# ==========================================

class CalculadoraArea:

    def calcular(self):
        raise NotImplementedError("Implemente o método calcular.")


class Quadrado(CalculadoraArea):

    def __init__(self, lado):
        self.lado = lado

    def calcular(self):
        return self.lado ** 2


class Circulo(CalculadoraArea):

    def __init__(self, raio):
        self.raio = raio

    def calcular(self):
        return 3.14159 * self.raio ** 2


class Retangulo(CalculadoraArea):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular(self):
        return self.largura * self.altura


figuras = [
    Quadrado(5),
    Circulo(3),
    Retangulo(4, 6)
]

for figura in figuras:
    print("\nÁrea:", figura.calcular())


# ==========================================
# DUCK TYPING
# ==========================================

# Python permite trabalhar com objetos diferentes
# desde que eles ofereçam os métodos necessários.

class Impressora:

    def imprimir(self):
        print("Imprimindo documento...")


class Relatorio:

    def imprimir(self):
        print("Imprimindo relatório...")


class Documento:

    def imprimir(self):
        print("Imprimindo documento PDF...")


def executar_impressao(objeto):
    objeto.imprimir()


objetos = [
    Impressora(),
    Relatorio(),
    Documento()
]

for objeto in objetos:
    executar_impressao(objeto)


# ==========================================
# POLIMORFISMO COM CLASSES ABSTRATAS
# ==========================================

from abc import ABC, abstractmethod


class Pagamento(ABC):

    @abstractmethod
    def processar(self, valor):
        pass


class CartaoCredito(Pagamento):

    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} no cartão.")


class Pix(Pagamento):

    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} via Pix.")


pagamentos = [
    CartaoCredito(),
    Pix()
]

for pagamento in pagamentos:
    pagamento.processar(150)