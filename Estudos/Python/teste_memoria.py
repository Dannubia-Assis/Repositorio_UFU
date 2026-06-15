"""
Teste de memoria com generators


#Teste 1 lista

for n in fib_list(100):
    print(n)
"""
#Sequencia de Fibonacci: 1, 1, 3, 5, 8, 13

#Funcao com lista - 449MB para 100000

def fib_list(max):
    nums = [] #Cria uma lista vazia
    a, b = 0, 1 #Inicia cada variavel
    while len(nums) < max:
        nums.append(b) #Adiona b na lista para iniciar em 1
        a, b = b, a+b
    return nums

#Funcoes com geradores 3MB para 100000

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

#Teste 2 geradores
for n in fib_gen(100): # O for chama a funcao next() automaticamente
    print(n)        