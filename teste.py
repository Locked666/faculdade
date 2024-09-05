def return_table_imc(value):
    v_alue = float(value)
    categories = [
        ("Abaixo do peso", "Menor que 18,5", v_alue < 18.5),
        ("Peso Saudável", "18,5-24,9", 18.5 <= v_alue <= 24.9),
        ("Sobrepeso", "25,0-30,0", 25 <= v_alue <= 30),
        ("Obeso", "30,1 - 39,9", 30.1 <= v_alue <= 39.9),
        ("Obeso Móbido", "Maior que 40", v_alue >= 40)
    ]

    texts = ['Você está Aqui' if cat[2] else '              ' for cat in categories]
    vlues = [str(value).replace('.', ',') if cat[2] else '    ' for cat in categories]

    tbl = f"""       
    ---------------------------------------------------------------------------------------------------
    |  {categories[0][0]:<17} |  {categories[1][0]:<17} |  {categories[2][0]:<17} |  {categories[3][0]:<17} |  {categories[4][0]:<17} |
    |  {categories[0][1]:<17} |  {categories[1][1]:<17} |  {categories[2][1]:<17} |  {categories[3][1]:<17} |  {categories[4][1]:<17} |
    |                   |                   |                   |                   |                   |                 
    |  {texts[0]:<17} |  {texts[1]:<17} |  {texts[2]:<17} |  {texts[3]:<17} |  {texts[4]:<17} |
    |       {vlues[0]:<5}       |       {vlues[1]:<5}       |       {vlues[2]:<5}       |       {vlues[3]:<5}       |       {vlues[4]:<5}       |
    |_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|

    """
    return tbl

# Exemplo de uso
print(return_table_imc(36))
