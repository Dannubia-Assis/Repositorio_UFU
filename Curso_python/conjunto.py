"""
Conjuntos

- Faz referência a teoria do conjuntos da matemática
- São chamados de sets
- Sets não possuem valores duplicados
- Não possuem valores ordenados
- Elementos não são acessados via índice
- Conjuntos não são indexados

- São bons para se utiizar quando precisamos armazenar
elementos mas não é importante a ordenação deles
- São referênciados com chave {}

Diferença entre conjuntos (sets) e mapas (dicionários)
    - Dicionário tem chave/valor
    - Conjunto tem apenas valor 

"""
#Definindo um conjunto:

#Forma 1

s = set({1,2,3,4,5,5,7,2,3}) #Repare nos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto caso seja adicionado um valor já existente
#o mesmo será ignorado sem gerar erros e não fará parte do conjunto

#Forma 2 - mais comum

s = {1,2,3,4,5,5}
print(s)
print(type(s))

#Podemos determinar se determinado elemento as contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')    