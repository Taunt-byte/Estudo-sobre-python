# Break em python

import time #Biblioteca relacionada a tempo

contdor = 0
while contador < 10:
    print("Ainda nao deu")
    contador = contador + 1
    if contador == 6:
        break
    time.sleep(1)
print("Agora Deu")