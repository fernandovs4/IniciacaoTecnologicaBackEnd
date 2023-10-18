def convert_month_year_to_dd_mm_yyyy(date_str):
    # Mapeamento de nomes de meses para números
    month_mapping = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    data_formatada = ''
    lista_de_strings = date_str.split(' ')
    if len(lista_de_strings) == 3:
        month = month_mapping[lista_de_strings[0]]
        day = lista_de_strings[1].replace(',', '')
        year = lista_de_strings[2]
        data_formatada = f'{"0" + day if len(day) == 1 else day }-{month}-{year}'
    else:
        if len(lista_de_strings) == 2:
            month = month_mapping[lista_de_strings[0]]
            year = lista_de_strings[1]
            data_formatada = f'01-{month}-{year}'
        else:
            return None
    return data_formatada