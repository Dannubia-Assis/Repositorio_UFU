"""
Reduce
OBS: A partir do python3+ a funcao reduce() nao eh mais uma funcao
integrada (built-in). Agora temos que importar e utilizar esta funcao a partir do modulo 'functools'

Guido Van Rossum: Utilize a funcao reduce() se voce realmente precisar dela. Em
 todo caso quase sempre um loop for eh mais legivel.

 Para entender:

 #Imagine que voce tem uma colecao de dados:

 dados = [a1, a2, a3, ...., an]

 def funcao(x,y):
    return x * y

Assim com o map() e filter() a funcao reduce() recebe dois parametros: a funcao e o iteravel.

reduce(funcao,dados)

A funcao reduce(), funciona da seguinte forma:
    Passo 1: es1 = f(a1, a2) #Aplica a funcao nos dois primeiros elementos da colecao
    e guarda o resultado.

    Passo 2: res2 = f(res1, a3) #Aplica a funcao passando o resultado do passo 1 mais o terceiro elemento
    e guarda o res.

    Isso eh repetido ate o final.

    Ou seja, em cada passo ela aplica a funcao passando como primeiro argumento o 
    resultado da aplicacao anterior. No final reduce() ira retornar o resultado final.

    Alternativamente, poderiamos ver a funcao  reduce() como:

    funcao(funcao(funcao(a1, a2), a3))

    """

#Como funciona pratica

#Vamos utilizar a funcao reduce() para multiplicar todos os numeros de um lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

#Para utilizar o reduce() nos precisamos de uma funcao que receba dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)

print(res)

#utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)