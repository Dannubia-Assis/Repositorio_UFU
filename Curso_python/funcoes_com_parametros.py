"""
Funcoes com parâmetros sao funcoes que recebem dados para ser processados dentro da mesma

entrada -> processamento -> saida

#Refatorando uma funcao

def quadrado(numero): #Calcula o quadrado do numero que ela receber
    #return numero*numero
    return numero**2
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))


#Funcoes podem ter n parametros de entrada, separados por virgula

# Erro comum na utilizacao do return
#Funcao que soma os numeros impares em uma lista
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = input("Digite os numeros separados por espacos: ").split()

#A funcao split() separa o texto em strings separadas. Sem argumento ela 
#separa a cada espaco de um itens ao outro
# map(funcao, valor) aplica uma funcao para cada valor da lista
#Nesse caso converte as strings do input em inteiro
#o list() transforma o input em uma lista

lista = list(map(int, lista))

resultado = soma_impares(lista)

print(resultado)

"""
"""
Funcoes com parametro padrão

- funcoes onde a passagem de parâmetro seja opcional

def exponencial(numero, potencia=2):
    return numero**potencia

print(exponencial(2,3))
#OBS: se o usuario passar somente  1 argumento, este sera atribuido
#ao parametro numero e sera calculado o quadrado desse numero
# Se o usuario passar dois argumentos, o primeiro sera atribuido ao parametro 
# numero e segundo ao parametro potencia e entao sera calculada a pontecia


print(exponencial(3))
print(exponencial(3,5))

#Em funcoes python os parametros com valores default (padrao) DEVEM estar ao final da declaracao

# ERRO !

def test(num=2, potencia):
    return num**potencia


#Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Sthefany'))

#Porque utilizar parâmetros com valor default?
#Nos permite ser mais flexiveis nas funccoes
#Evita erros com parâmetros incorretos
#Nos permite trabalhar com exemplo mais legiveis do codigo
#Pode utilizar qualquer tipo de dado como default para paramentros
"""

#Escopo - Evitar problemas e confusoes

#Variaveis globais
#Variaveis locais

intrutor = 'Geek' #Variavel global

def diz_oi():
    instrutor = 'Python' #Variavel local
    return f'Ola {instrutor}'

#Se tivermos uma variavel local com o mesmo nome de uma variavel global
#local tera preferencia.

#Atencao com variaveis globais - Se puder evitar, evite!

"""
**kwargs

Chamados assim por convenção, o importante é manter **

Diferente do *args que coloca os valores extras em uma tupla
o **Kwargs exige que se utiliza parametros nomeados e transforma 
esses valores extras em um dicionário


#Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
    #Como kwargs é um transforma os valores em 
    #um dicionario pode usar items()
        print(f'A cor favorita de {pessoa.title()} é {cor}')

#Os parametros *args e **kwargs não são obrigatorios
cores_favoritas(Marcos='verde', Ana = 'Rosa', Vanessa = 'Branco')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento!'
    elif 'geek' in kwargs:
        return f'{kwargs['geek']} Oi!'
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek = 'Python'))
print(cumprimento_especial(geek = 'Você'))
print(cumprimento_especial(geek = 'Especial'))

#Nas funções podemos ter (nessa ordem):

- Parametro obrigatorios
- *args
- Parametros default (não obrigatorios)
- **kwargs

"""


