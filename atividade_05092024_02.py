############################################
#   Projeto Calculadora de IMC:            #     
#   Aluno: Julio Sales                     #     
#                                          #     
#   Anhanguera: 05/09/2024  2.0            #     
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
# BEM VINDO AO CALCULADOR DE NOTAS      #
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


def calc_return_value_media(notas : list ):
    qt_nota = float(len(notas))
    soma_notas = 0.0
    status = ''
    conceito = ''
    for i in notas:
        soma_notas +=float(i)
    
    media = soma_notas / qt_nota
    media = float(media)
    
    if float(media) < 3.9:
        status = "Reprovado"
        conceito = "E"
        return media,status,conceito
        
    elif float(media) >= 4.0 and float(media) <= 5.9:
        status = "teste"
        conceito = "D"
        return media,status,conceito
         
    elif float(media) >= 6.0  and float(media) <= 7.4:
        status = "Aprovado"
        conceito = "C"
        return media,status,conceito     
    
    elif float(media) >= 7.5 and float(media) <= 8.9:
        status = "Aprovado"
        conceito = "B" 
        return media,status,conceito
    
    elif float(media) >= 8.9 and float(media) <= 10:
        status = "Aprovado"
        conceito = "A"  
        return media,status,conceito              
    
    
    


def main():
    notas= []
    print(PRESENTATION)
    print("")
    print("A seguir, informe as notas do aluno, ao minimo duas.")
    while True:
        try:
            
            entry_notas = input(f"Informe a {len(notas) + 1 }º nota do aluno: ")
            entry_notas = entry_notas.replace(',','.').strip()
            if float(entry_notas) == 0 or float(entry_notas) == 0.0:
                print("_"*30)
                print("Nota informada inválida")
                print("_"*30)
            else:    
                notas.append(float(entry_notas))
            
            if len(notas) >= 2:
                print(" Deseja Informar mais notas ?")
                print("_"*30)
                print("1 - Sim")
                print("2 - Não")
                a  = input("R: ")
                if int(a) != 1: 
                    conta  =  calc_return_value_media(notas=notas)
                    print('-'*30)
                    print(f"Notas:{[i for i in notas]}")
                    print('-'*30)
                    print(f"Média: {conta[0]}")
                    print('-'*30)
                    print(f"Conceito: {conta[2]}")
                    print('-'*30)
                    print(f"Status: {conta[1].upper()}")
                    
                    print('-'*30)
                    print('-'*30)
                    print('-'*30)
                    break

            
        except ValueError as e: 
            print("Ocorreu um erro na execução. \n {e}")
            
            
if __name__ == '__main__':
    app = main()            