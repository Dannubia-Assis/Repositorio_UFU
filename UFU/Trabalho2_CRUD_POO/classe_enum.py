from enum import Enum

#Uso do Enum para classificar a cada ativos cadastrado
class tipo_ativo(Enum):
    Notebook = 10 
    Impressora = 20
    Roteador = 30
    Software = 40

#Enum para a categoria
class categoria(Enum):
    Autenticação = 1 
    Controle_de_acesso = 2
    Software_desatualizado = 3
    Rede= 4
    Banco_de_dados = 5
    Configuração_incorreta = 6

#Enum para a severidade
class severidade(Enum):
    Baixa = 1 
    Media = 2
    Alta = 3

#Enum para o status    
class status(Enum):
    Aberta = 1 
    Em_tratamento = 2
    Risco_aceito = 3
    Corrigida = 4