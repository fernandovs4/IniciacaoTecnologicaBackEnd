def reajustaDatas(dados):
    """Essa função recebe um dicionário como o abaixo:
    {
        "Rio Preto": {
            "2023": 9,
            "2015": 13,
            "2022": 13,
            "2019": 12,
            "2006": 1
        },
        "Sírio Libanês": {
            "2020": 13,
            "2019": 9,
            "2018": 9,
            "2015": 5,
            "2007": 3
        },
        "A.C. Camargo": {
            "2019": 20,
            "2015": 7,
            "2018": 8,
            "2022": 12,
            "2008": 3,
          
        }
    }, e preenche os anos faltantes com 0, retornando um dicionário como o abaixo:
    ele todos os anos que estão presentes em todos os hospitais, e recria o dicionário com os anos faltantes preenchidos com 0.

    
    """

    hospitais = dados.keys()
    anos = set()
    for hospital in hospitais:
        anos.update(dados[hospital].keys())
    anos = sorted(anos)
    for hospital in hospitais:
        for ano in anos:
            if ano not in dados[hospital].keys():
                dados[hospital][ano] = 0
    return dados

