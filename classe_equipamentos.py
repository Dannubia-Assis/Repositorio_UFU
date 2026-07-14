
from classe_ativos import Ativos
from classe_vulnerabilidades import Vulnerabilidades
from classe_enum import tipo_ativo, categoria, severidade, status
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent #Identificando o local do arquivo json
ARQUIVO_JSON = BASE_DIR / "dados" / "ativos.json"

class Equipamentos():

    def __init__(self):
         
        self.lista_de_ativos = [] #Armazena os dados do ativo em uma lista

    #Criando os módulos para manipular as propriedades da classe ativo
    def cadastrar_ativo(self, ativo):
        self.lista_de_ativos.append(ativo) #Adiciona o ativo na lista de ativos da classe equipamentos
                                    #como um dicionário
        return ativo

    def buscar_cadastro_ativo(self, id):

        for ativo in self.lista_de_ativos: #Percorre a lista
             
             if ativo.id == id: #Encontra o ID correspondente
                return ativo #Dessa forma ele retorna o contato e da para usar a busca em outros metodos

        return None
    
    def atualizar_ativo(self, id, novo_tipo=None, novo_nome=None, novo_responsavel=None, novo_setor=None):

        ativo = self.buscar_cadastro_ativo(id)

        if ativo is None:
            print("ID não encontrado.")
            return None

        if novo_tipo is not None:
            ativo.tipo = novo_tipo

        if novo_nome != "":
            ativo.nome = novo_nome

        if novo_responsavel != "":
            ativo.responsavel = novo_responsavel

        if novo_setor != "":
            ativo.setor = novo_setor
        
        return ativo
    
    def excluir_cadastro(self,id):

        ativo = self.buscar_cadastro_ativo(id)

        if ativo is None:
            print("ID nao encontrado.")
            return
        
        self.lista_de_ativos.remove(ativo)

        return True
    
    def salvar_dados(self):

        dados = [ativo.to_dict() for ativo in self.lista_de_ativos]

        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
    def carregar_dados(self):
        
            try:
                with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
        
            except FileNotFoundError:
                return
        
            self.lista_de_ativos.clear()
        
            for ativo_json in dados:
        
                ativo = Ativos(
                    tipo_ativo[ativo_json["tipo"]],
                    ativo_json["nome"],
                    ativo_json["responsavel"],
                    ativo_json["setor"]
                )
        
                # Recupera o ID original
                ativo._Ativos__id = ativo_json["id"]
        
                for vulnerabilidade_json in ativo_json["vulnerabilidades"]:
        
                    vulnerabilidade = Vulnerabilidades(
                        vulnerabilidade_json["descricao"],
                        categoria[vulnerabilidade_json["categoria"]],
                        severidade[vulnerabilidade_json["severidade"]],
                        status[vulnerabilidade_json["status"]]
                    )
        
                    ativo.adicionar_vulnerabilidade(vulnerabilidade)
        
                self.lista_de_ativos.append(ativo)
        
            # Atualiza o contador para continuar os IDs
            if self.lista_de_ativos:
                Ativos.contator = max(ativo.id for ativo in self.lista_de_ativos)