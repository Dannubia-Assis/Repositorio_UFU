"""
Cripytografando senha de usuario
"""
#Importando biblioteca para criptografar a senha
# as cryp renomeia pbkdf2_sha256 para ficar mais simples no codigo

from passlib.hash import pbkdf2_sha256 as cryp 

#Criando a classe usuario

class Usuario:

    contador = 0 #Atributo de classe

    @classmethod #Metodo de classe - decorador
    def contas_usuario(cls): #cls - parametro recebido é a própria classe
        print(f'Temos {cls.contador} usuários no sistema')

    #Cria o objeto usuario
    def __init__ (self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16) 
        Usuario.contador = self.__id
        #parametro - rounds = numero de vezes que sera embaralhado
        #parametro salt_size = tamanho da parte que sera acrescentada a senha 
        print(f'Usuario criado: {self.__gera_usuario()}')

    #Metodo de instancia que exibe o nome completo do usuario
    def nome_completo(self): #Recebe apenas o objeto e acessa seus atributos
        return f'{self.__nome} {self.__sobrenome}'
    
    #Metodo de instancia que checa se a senha do usuario esta correta
    def checa_senha(self, senha): #Recebe o objeto e a senha
        if cryp.verify(senha, self.__senha ): #Verifica se a 1 senha eh igual a 2 senha
            return True
        return False
    #Metodo de instancia privado
    def __gera_usuario(self):
        return self.__email.split('@')[0]
    

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)

else:
    print('A senha não confere...')
    exit(1)

print('Usuário cadastrado com sucesso!')

senha = input('Informe sua senha para acessar: ')  

if user.checa_senha(senha):
    print('Acesso permitido!')

else: 
    print('Acesso negado...')

print(f'Senha User Criptografada: {user._Usuario__senha}') #Acesso errado