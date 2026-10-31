# ==========================================
# HERANÇA EM PYTHON
# ==========================================

# Herança permite que uma classe reutilize
# atributos e métodos de outra classe.


# ==========================================
# CLASSE PAI
# ==========================================

class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome}.")

    def emitir_som(self):
        print("O animal emitiu um som.")


# ==========================================
# CLASSES FILHAS
# ==========================================

class Cachorro(Animal):

    def latir(self):
        print("Au au!")


class Gato(Animal):

    def miar(self):
        print("Miau!")


# Criando objetos
cachorro = Cachorro("Rex", 5)
gato = Gato("Mimi", 3)

# Métodos herdados
cachorro.apresentar()
gato.apresentar()

# Métodos próprios
cachorro.latir()
gato.miar()


# ==========================================
# SOBRESCRITA DE MÉTODOS
# ==========================================

class Veiculo:

    def __init__(self, marca):
        self.marca = marca

    def movimentar(self):
        print("O veículo está se movimentando.")


class Carro(Veiculo):

    def movimentar(self):
        print(f"O carro {self.marca} está andando.")


class Barco(Veiculo):

    def movimentar(self):
        print(f"O barco {self.marca} está navegando.")


carro = Carro("Toyota")
barco = Barco("Yamaha")

carro.movimentar()
barco.movimentar()


# ==========================================
# SUPER()
# ==========================================

# super() permite acessar métodos da classe pai.

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Departamento: {self.departamento}")


gerente = Gerente("Lucas", 5000, "Tecnologia")

print("\nDados do gerente:")
gerente.exibir_dados()


# ==========================================
# HERANÇA MÚLTIPLA
# ==========================================

class Nadador:

    def nadar(self):
        print("Está nadando.")


class Corredor:

    def correr(self):
        print("Está correndo.")


class Atleta(Nadador, Corredor):
    pass


atleta = Atleta()

print("\nAtleta:")
atleta.nadar()
atleta.correr()