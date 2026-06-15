"""
Faca um programa que tenha uma funcao que recebe uma data no formato string exemplo 01/01/2026 e 
imprima ela por extenso como 1 de janeiro de 2026
"""

def muda_formato_data(data):
    
    meses = {
            '01': 'janeiro', 
            '02': 'fevereiro',  
            '03': 'marco', 
            '04': 'abril', 
            '05': 'maio', 
            '06': 'junho', 
            '07': 'julho', 
            '08': 'agosto', 
            '09': 'setembro', 
            '10': 'outubro', 
            '11': 'novembro', 
            '12': 'dezembro', }
    
    """"dia = int(data[0])
    mes = data[1]
    ano = data[2]"""

    #unpacking
    dia, mes, ano = data

    return f"{dia} de {meses[mes]} de {ano}" #meses procura a chave mes no dicionario e retorna o valor \
                                             #correspondente da chave                   


data = input('Digite uma data com o formato "xx/xx/xxxx": ').split('/')

novo_formato = muda_formato_data(data)

print(novo_formato)
