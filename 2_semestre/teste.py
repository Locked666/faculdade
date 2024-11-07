from datetime import datetime

global info_database

info_database = []


class Database:
    def __init__(self):
        self.database = []
        


    def __return_id(self):
        qt_data =  len(self.database)
        m_id = []
        if qt_data == 0: 
            return 1
        else :
            for i in self.database:
                id_m = i.get("id",0)
                m_id.append(id_m)
            return max(m_id)     

    def cadastrar_produto(self,id:int = 0, nome:str = '', categoria:str=0,localizacao:str = 0, quantidade:float=0):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.localizacao = localizacao
        self.quantidade = quantidade

        m_id = self.__return_id()
        
        try:
            if self.id == 0:
                value = {
                    "id": (m_id+1),
                    "nome": self.nome,
                    "categoria": self.categoria,
                    "localizacao":self.localizacao,
                    "quantidade":self.quantidade 
                }    

                info_database.append(value)
                return (True,f"id:{(m_id+1)}", info_database)

            else: 
                return (False, "Produto Já Cadastrado")

        except ValueError as e: 
            return  (False, e)   

    def consulta_produto(self, filter:bool =  False, tipo: str = "" ,valor:str ="", **kwargs):
        resultado = []
        if filter:
            match tipo:
                case "id":
                    for i in info_database:
                        if valor in str(i.get("id","0")):
                            resultado.append(i)

                case "nome":
                    for i in info_database:
                        if valor in str(i.get("nome","")):
                            resultado.append(i)
            return resultado
        else: 
            for i in info_database:
                resultado.append(i)
            return resultado                        

                
                

if __name__=='__main__':
    
    while True:
        datbase = Database()
        option = input("1,2: ")

        if option == "1":
            nome_produto = str(input("Nome Produto:  "))
            categoria_produto = str(input("Categoria Produto:   "))
            localizao_produto = str(input("localizao Produto:   "))
            quantidade_produto = float(input("quantidade Produto:   "))

            acao =  datbase.cadastrar_produto(nome=nome_produto, categoria=categoria_produto,localizacao=localizao_produto,quantidade=quantidade_produto)
            if acao:        
                print(acao)
        elif option ==  "2":
            acao =  datbase.consulta_produto()
            print(acao)




