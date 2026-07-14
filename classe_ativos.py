from classe_vulnerabilidades import Vulnerabilidades
import classe_enum


class Ativos():

    contator = 0
    #Criando o objeto ativo
    def __init__(self, tipo, nome, responsavel, setor):

        Ativos.contator += 1
        self.__id = Ativos.contator 
        self.__tipo = tipo
        self.__nome = nome
        self.__responsavel = responsavel
        self.__setor = setor
        self.__vulnerabilidades = [] #Lista de vulnerabilidades vinculado ao número de ID do ativo

    def adicionar_vulnerabilidade(self, vulnerabilidade):
        self.__vulnerabilidades.append(vulnerabilidade)

    def buscar_vulnerabilidade(self, id):

        for vulnerabilidade in self.__vulnerabilidades: #Percorre a lista
             
             if vulnerabilidade.id == id: #Encontra o ID correspondente
                return vulnerabilidade #Dessa forma ele retorna o contato e da para usar a busca em outros metodos

        return None

    def atualizar_vulnerabilidade(self, indice,nova_descricao,nova_categoria,nova_severidade,novo_status):

        if not self.__vulnerabilidades:
            raise ValueError("Nenhuma vulnerabilidade cadastrada.")

        if indice < 0 or indice >= len(self.__vulnerabilidades):
            raise ValueError("Indice de vulnerabilidade invalido.")

        vulnerabilidade = self.__vulnerabilidades[indice]

        if nova_descricao:
            vulnerabilidade.descricao = nova_descricao

        if nova_categoria is not None:
            vulnerabilidade.categoria = nova_categoria

        if nova_severidade is not None:
            vulnerabilidade.severidade = nova_severidade

        if novo_status is not None:
            vulnerabilidade.status = novo_status

    def remover_vulnerabilidade(self, indice):

        if indice < 0 or indice >= len(self.__vulnerabilidades):
            raise ValueError("Vulnerabilidade não encontrada.")
  
        self.__vulnerabilidades.pop(indice)

        return True
        
    def possui_vulnerabilidades(self):
        return len(self.__vulnerabilidades) > 0

    def imprimir_ativo(self):

        print('___________________________________')
        print(f'         ID : {self.__id}')
        print(f'       Tipo : {self.__tipo.name}')
        print(f'Equipamento : {self.__nome}')
        print(f'Responsável : {self.__responsavel}')
        print(f'      Setor : {self.__setor}')

    def imprimir_vulnerabilidades(self):

        if not self.__vulnerabilidades:
            print("Nenhuma vulnerabilidade cadastrada.\n")
            return  

        for indice, vulnerabilidade in enumerate(self.__vulnerabilidades, start=1):

            print(f"\nVulnerabilidade {indice}")

            vulnerabilidade.imprimir()
    
    def to_dict(self):
    
        return {
            "id": self.id,
            "tipo": self.tipo.name,
            "nome": self.nome,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "vulnerabilidades": [
                vulnerabilidade.to_dict()
                for vulnerabilidade in self.vulnerabilidades
            ]
        }
    
    #Criando as propertys e setters para que a classe equipamentos manipule os atributos
    #da classe ativos

    @property
    def id(self):
        return self.__id
    
    #Como o ID é um informação do ativo que não pode ser alterada ela contém apenas
    #A classe equipamentos apenas vai ter acesso de fazer o uso do atributo sem alterar 
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, novo_tipo):
        if len(str(novo_tipo)) < 3: 
            raise ValueError
        
        self.__tipo = novo_tipo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if len(str(novo_nome)) < 3:
            raise ValueError("O nome deve possuir pelo menos 3 caracteres.")
        
        self.__nome = novo_nome
    
    @property
    def responsavel(self):
        return self.__responsavel
    
    @responsavel.setter
    def responsavel(self, novo_responsavel):
        if len(str(novo_responsavel)) < 3: 
            raise ValueError("O responsavel deve possuir pelo menos 3 caracteres.")
        
        self.__responsavel = novo_responsavel
    
    @property
    def setor(self):
        return self.__setor
    
    @setor.setter
    def setor(self, novo_setor):
        if len(str(novo_setor)) < 3: 
            raise ValueError("O setor deve possuir pelo menos 3 caracteres.")
        
        self.__setor = novo_setor

    @property
    def vulnerabilidades(self):
        return self.__vulnerabilidades
    
   