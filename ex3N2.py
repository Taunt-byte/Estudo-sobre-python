# Fazer um codigo que diga se o numero é igual ou impar


a = int (input('Entre com um valor'))
resto = a & 2
if resto == 0:
    print('numero é par')
else:
    print('numero é impar')