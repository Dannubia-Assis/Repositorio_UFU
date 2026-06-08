""""
Any e All

all() - retorna true se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel esta vazio


#Exemplo all()

print(all([ 1, 2, 3, 4])) #Todos os numero sao verdadeiros? True

print(all([0, 1, 2, 3, 4])) #Todos os numero sao verdadeiros? False

#OBS: um iteravel vazio m boolean eh falso mas o all() entende como true

print(all([letra for letra in 'eio' if letra in 'fkp']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
"""
"""
Any() - retorna true se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio,
retorna False

"""
print(any([0, 1, 2, 3, 4])) #True

print(any([0, False, {}, ()])) #False


