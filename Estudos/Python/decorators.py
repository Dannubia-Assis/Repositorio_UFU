"""
Decoradores (Decorators)
- Sao funcoes
- Decorators envolvem outras funcoes e aprimoram seus comportamentos
- Tambem sao exemplos de Higher Order Functions
- Tem um sintaxe propria, usando @ (Syntact Sugar)

#Decorators como funcoes (Sintaxe não recomendada)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce! ')
        funcao()
        print('Tenha um otimo dia! ')
    return sendo 

def saudacao():
    print('Seja bem vindo a geek university')


#Testando 1 

teste = seja_educado(saudacao)    #Saude a pessoa mas seja educado

teste() 

"""

#Decorators com syntact sugar

def seja_educado(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce! ')
        funcao()
        print('Tenha um excelente dia! ')
    return sendo_mesmo

@seja_educado
def apresentando():
    print('Meu nome eh Dannubia')


#Testando

apresentando()

#OBS nao confunda decorator com decorator function