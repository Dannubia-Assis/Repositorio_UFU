from classe_enum import severidade, status, categoria

class Vulnerabilidades():

    def __init__(self, descricao, categoria, severidade, status):

        self.__descricao = descricao
        self.__categoria = categoria
        self.__severidade = severidade
        self.__status = status

    def imprimir(self):

        print(f' Descrição: {self.__descricao}')
        print(f' Categoria: {self.__categoria.name}')
        print(f'Severidade: {self.__severidade.name}')
        print(f'    Status: {self.__status.name}')
    
    def to_dict(self):

        return {
        "descricao": self.descricao,
        "categoria": self.categoria.name,
        "severidade": self.severidade.name,
        "status": self.status.name}
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_descricao): 
        if len(str(nova_descricao)) < 3: 
            raise ValueError
        
        self.__descricao = nova_descricao
        
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nova_categoria):
        
        if not isinstance(nova_categoria, categoria): 
            raise TypeError("Valor inválido.") #Mais uma camada de proteção que garante que 
                                                #a opção escolhida esteja no enum
        self.__categoria = nova_categoria
        
    @property
    def severidade(self):
        return self.__severidade
    
    @severidade.setter
    def severidade(self, nova_severidade):

        if not isinstance(nova_severidade, severidade):
            raise TypeError("Valor inválido.")

        self.__severidade = nova_severidade

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):

        if not isinstance(novo_status, status):
            raise TypeError("Valor inválido.")

        self.__status = novo_status
        
  