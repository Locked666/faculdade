############################################
#   Projeto Calculadora de IMC:            #     
#   Aluno: Julio Sales                     #     
#                                          #     
#   Anhanguera: 05/09/2024                 #     
#   Campo Grande - MS                      #      
############################################

__version__ = 0.1

### Inserindo Variaveis imutaveis. 
INFO = f"""
#########################################
#     Deseja Continua ?                 #
#       1 - Sim                         #
#       2 - Não                         #
#########################################
"""


PRESENTATION = f"""
#########################################
# BEM VINDO AO CALCULADOR DE REAJUSTE   #
# FIQUE A VONTADE PARA COMENTAR         # 
# VERSÃO: {__version__}                 #
#########################################
"""

COMPLETION = f"""
#########################################
# Obrigado por utilizar nosso sistema   #
#            Até Breve                  #
#########################################

"""
DATABASE_NAME = {}

def return_table_calc_reajuste(value):
    value_reajuste = float(value)
    try:
        if value_reajuste <= 280 :
            return 0.20
        elif value_reajuste >= 280.01 or value_reajuste <= 700:
            return 0.15
        elif value_reajuste >=700.01 or value_reajuste <= 1500:
            return 0.10
        elif value_reajuste > 1500:
            return 0.5
        else:
            return 0.5 
    except ValueError as e:
        print(f"Houve um erro ao retornar valor da do reajuste, verifique!\n {e}")



def calc_reajuste(value):
    value_calc = float(value)
    value_porc = return_table_calc_reajuste(value_calc)
    value_reajuste_end =   value_calc + (value_calc * value_porc)
    print(value_reajuste_end)
    return value_porc,value_reajuste_end

def main():
    print(PRESENTATION)  
    while True:
        try:
            value_entry = input("Informe o valor do Salário:")
            value_entry = value_entry.replace(',','.').strip()
            value_entry = float(value_entry)
            
            value_end = calc_reajuste(value_entry)
            
            print("_"*28)
            print(f"Salário antes do reajuste: {value_entry}")
            print("-"*28)
            print(f"Percentual de aumento: {(value_end[0]*100)}")
            print("-"*28)
            print(f"Valor do aumento: {(value_entry*value_end[0])}")
            print("-"*28)
            print(f"Valor do Sário Após o aumento: {value_end[1]}")

        except ValueError as e:
            print(" Ocorreu um erro ao executar o programa!\n{e}")


if __name__=='__main__':
    app = main()
    
    
        