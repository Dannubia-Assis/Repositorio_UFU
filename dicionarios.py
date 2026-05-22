"""
Dicionários 
- Em algumas linguagens são conhecidos por mapas
- São coleções do tipo chave e valor
- São representados por chaves {}
- Chave e valor são separados por dois pontos 'chave:valor'
- Chave e valor podem ser de qualquer tipo
- Dados podem ser misturados

#Criação de dicionários

#Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

#Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

#Acessando elementos

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Forma 1 - Acessando via chave da mesma forma que lista/tupla
print(paises['br'])

#Forma 2 - Acessando via get - Recomendado pois não gera erro e retorna o tipo None

print(paises.get('br'))
print(paises.get('ru')) # O tipo none em python representa o tipo sem tipo (vazio)
#Primeira letra sem maiuscula None, sempre é considerado como false

#Podemos definir um valor padrão para caso não encontremos o objeto com
#a chave informada  

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('ru', 'Não encontrado') #Se não encontrar mostra o segundo argumento

print(f'Encontrei o pais {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Podemos verificar se determinada chave se encontra em um dicionário

print('br'in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

#Pode ser utilizado qualquer tipo de dado
#Tuplas são interessantes para serem utilizadas em dicionarios por serem imutáveis

localidade = { 
    (32.58, 38.59): 'Escritório em Tókio',
    (96.58, 15.59): 'Escritório em São Paulo'
    }

print(localidade)
print(type(localidade))


#Adicionar elementos em um dicionário

receita = {'jan':100, 'fev': 120, 'mar':300}

print(receita)
print(type(receita))

#Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

#Forma 2 
receita = {'jan':100, 'fev': 120, 'mar':300}

mes = input("Digite o mês: ")
valor = int(input("Digite o valor: "))

#Colchetes [] servem para acessar uma chave, adicionar uma chave e atualizar uma chave
#Chaves {} criam o dicionário
#Também dá para usar o .update()

receita[mes]=valor

print(receita)

#A forma de atualizar ou adicionar novos elementos em um dicionário
#é a mesma
# Não pode existir chaves repetidas em dicionários


#Remover dados de um dicionário

receita = {'jan':100, 'fev': 120, 'mar':300}

#Forma 1 - mais comum

print(receita)
ret = receita.pop('mar')
print(ret)
print(receita) 

#Obs: aqui precisa sempre passar a chave,
#e caso não encontra o elemento um KeyError é retornado
#Obs: quando remove o objeto o valor é sempre retornado

#Forma 2

del receita['fev']  #del=deletar
print(receita)

#Neste caso o valor removido não é retornado
#Se tentar remover um elemento que não existe gera um KeyError
#Limpar dicionário (Zerar dados)

d.clear()
print(d)

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

#Copiando um dicionário para outro

#Forma 1 #Deep copy

novo = d.copy() 

print(novo)

novo['d'] = 4

print(d)
print(novo)


#Forma 2 Shallow Copy

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

#Forma não usual de criação de usuário

usuario = {}.fromkeys('teste', 'valor')
print(usuario)

#O método fromkeys recebe dois parâmetros: um interável e um valor
# Ele vai gerar para cada valor do interável uma chave
# e irá atribuir a esta chave o valor informado

"""




