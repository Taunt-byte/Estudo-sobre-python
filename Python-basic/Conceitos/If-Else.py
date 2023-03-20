# Exemplo 1
s = 0
for x in range(1, 100):
 s = s + x
print ( s )

# Exemplo 2

comida = 'pizza'

if comida=='pizza':
    print('Possui muitas calorias')

# Exemplo de Controle de fluxo

temp = int(input('Entre com a temperatura: '))

if temp < 0:
    print ('Congelando...')
elif 0 <= temp <= 20:
    print ('Frio')
elif 21 <= temp <= 25:
    print ('Normal')
elif 26 <= temp <= 35:
    print ('Quente')
else:
    print ('Muito quente!')