"""
Decorator que força a mudança do tipo da váriavel
Decorator tambem pode receber parametros de entrada
zip() -> relaciona os elementos na mesma posição de duas listas
"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = [] #Cria uma lista vazia para as conversões
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg( 'Geek', '3')

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir('1', 5)