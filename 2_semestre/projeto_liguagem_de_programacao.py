############################################
#   Projeto Calculadora de IMC:            #     
#   Aluno: Julio Sales                     #     
#   Portifólio Linguagem de Programação.   #     
#   Anhanguera: 02/09/2024                 #     
#   Campo Grande - MS                      #      
############################################

__version__ = 0.1

### Inserindo Variaveis imutaveis. 
INFO = f"""
#########################################
#     Deseja Continua ?                 #
#       1 - Sim                         #
#       2 - Não                         #
#       3 - Mostrar Quadro novamente    #
#########################################
"""


PRESENTATION = f"""
#########################################
# BEM VINDO A CALCULADORA DE IMC {__version__}    #
# FIQUE A VONTADE PARA COMENTAR         #
#########################################
"""

COMPLETION = f"""
#########################################
# Obrigado por utilizar nosso sistema   #
#            Até Breve                  #
#########################################

"""

# Criando Função para retornar tabela com valor. 
def return_table_imc(value):
    
    #Criando Variaveis:
    v_alue = float(value)
    text_1='              '
    text_2='              '
    text_3='              '
    text_4='              '
    text_5='              '
    vlue_1='    '
    vlue_2='    '
    vlue_3='    '
    vlue_4='    '
    vlue_5='    '
    

    # Adicionando bloco de verificação de valor da variavel setada ao chamar a função. 
    if v_alue < 18.5:
        text_1 = 'Você está Aqui'
        vlue_1 = str(value).replace('.',',')

    elif v_alue >= 18.5 and v_alue <= 24.9: 
        text_2 = 'Você está Aqui'
        vlue_2 = str(value).replace('.',',')       

    elif v_alue >= 25 and v_alue <= 30: 
        text_3 = 'Você está Aqui'
        vlue_3 = str(value).replace('.',',')
    elif v_alue >= 30.1 and v_alue <= 39.9: 
        text_4 = 'Você está Aqui'
        vlue_4 = str(value).replace('.',',') 
    elif v_alue >=40: 
        text_5 = 'Você está Aqui'
        vlue_5 = str(value).replace('.',',')  

    else:
        print(f"Algo de errado\n {value}")                

 # Variavel contendo o  layout padrão da tabela.                
    tbl = f"""       
        ---------------------------------------------------------------------------------------------------
        |  Abaixo do peso   |  Peso Saudável    |    Sobrepeso      |      Obeso        |   Obeso Móbido    |
        |  Menor que 18,5   |   18,5-24,9       |    25,0-30,0      |    30,1 - 39,9    |   Maior que 40    |
        |                   |                   |                   |                   |                   |                 
        |   {text_1}  |   {text_2}  |   {text_3}  |   {text_4}  |   {text_5}  |
        |       {vlue_1}        |       {vlue_2}        |       {vlue_3}       |    {vlue_4}           |    {vlue_5}           |
        |_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|

    """
    return tbl



# Função que calcula o IMC, recebe dois parametros( peso, altura)
def calc_imc(weight:float,height:float):
    # condição de acerto caso correto.
    try:
        # Bloco de condição de execução do calculo
        # Caso o valor do peso ou altura for vazio, retornar o erro. 
        if weight =='' or height =='':
            return (f"Impossível realizar calculo, valores estão vazios.\n Peso = {weight}, Altura = {height}")
        # Caso o valor for zero ou menor que zero, retornar co erro
        elif weight <= 0 or height <=0 :
            return (f"Impossível realizar calculo, valores estão menor ou igua a zero.\n Peso = {weight}, Altura = {height}")
        # Caso não atenda nenhuma codição do erro acima, realizar o calculo e retornar o valor. 
        else:
            imc = (weight/(height*height))
            imc = f"{imc:.2f}"
            return imc
    # Caso houver erro na verificação, retornar valor do erro    
    except ValueError as e:
        return (f"Ocorreu um erro ao realizar calculo, por favor verifique.\n Erro ({e})")

def main():
    print(PRESENTATION)
    while True:
        try: 
            
            #Solicitando a entrada das informações:
            input_weight = (input("Qual seu peso?: "))
            input_height = input("Qual Sua Altura?: ")
            
            # Corrigindo caso houver entrada com virgulas.
            input_weight = input_weight.replace(',','.').strip()
            input_height = input_height.replace(',','.').strip()
            
            # Corrigindo caso o valor da altura for  em cm
            if float(input_height) > 10:
                input_height = float(input_height) / 100
            
            value_imc = calc_imc(float(input_weight), float(input_height))
            print(return_table_imc(value=value_imc))
            print("__"*20)
            continuea = int(input(f"{INFO}\nR: "))
            
            if continuea == 1:
                continue
            elif continuea == 2:
                print(COMPLETION)
                break
            elif continuea == 3:
                print(return_table_imc(value=value_imc))
                print("__"*20)
                break
            else:
                print("Opção Inválida")    
                
            
            
        except ValueError as e: 
            print(f" Impossivel realizar calculo, verifique ao valores e tente novamente \n Erro ({e})")

if __name__=='__main__':
    app = main()        
    