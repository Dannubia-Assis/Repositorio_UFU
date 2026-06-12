"""
Geradores

- Geradores sao iteradores

OBS: O contrario nao eh verdadeiro. Ou seja, nem todo iterator eh um generator

- Generators podem ser criados com funcoes geradoras
- Fucoes geradoras utilizam a palavra reservada yield
- Generators podem ser criados com expressoes geradoras
- Ideal utilizar quando se necessita de um baixo uso de memoria

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)
"""

#Exemplo de generator function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador #yield aguarda o next() chamar novamente e depois incrementa
        contador = contador + 1

#OBS: nao eh um generator ela gera um generator

gen = conta_ate(10)

