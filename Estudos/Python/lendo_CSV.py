"""
Lendo arquivos CSV

csv - Comma Separeted Values - Valores serparados por virgulas

# Separador por virgula
1, 2, 3, 4
#Separador por ponto e virgula
#Separador por espaco


# Utilizando esse recurso para mostrar onde o arquivo CSV estava:
import os

print(os.getcwd())
print(os.listdir())

#Forma possivel de se trabalhar mas trabalhoso
with open('Curso_python/lutadores.csv', encoding="utf-8") as arquivo:
    dados = arquivo.read()
    #Diz ao python que o separa um elemento do outro eh virgula
    dados = dados.split(',') 
    print(dados)

    
A linguagem python possui duas formas diferentes para ler dados em arquivo CSV
- reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
- DictReader -> Permite que iteremos sobre as linhas do arquivo CVS como OrderedDicts;

#Reader

from csv import reader

with open('Curso_python/lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Pula o cabecalho
    for linha in leitor_csv:
        #Cada linha eh uma lista
        print(f'{linha[0]} nasceu no {linha[1]} e mede {linha[2]} centimetros')

#DictReader

from csv import DictReader

with open('Curso_python/lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #Cada linha eh um OrderedDict
        print(f"{linha['Nome']} nasceu no {linha['País']} e mede {linha['Altura (em cm)']}")

        """

#DictReader com outro separador

from csv import DictReader

with open('Curso_python/lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        #Cada linha eh um OrderedDict
        print(f"{linha['Nome']} nasceu no {linha['País']} e mede {linha['Altura (em cm)']}")