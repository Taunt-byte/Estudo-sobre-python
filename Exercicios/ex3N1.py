# Fazer um codigo que diga qual o maior valor ?
# Desafio: fazer com 3 numeros


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print ('o maior numero é {}' . format(a))
elif b > a and b > c:
    print('o maior numero é {}'.format(b))
else:
    print('O maior numero é {}' .format(c))
print('final do programa')