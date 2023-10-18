from datetime import datetime
from  funcoes_auxiliares.convert_month_year_to_dd__mm_yyyy import convert_month_year_to_dd_mm_yyyy
def filtra_por_data(datainicial, datafinal, estudo):
    try:
        dataEstudo = convert_month_year_to_dd_mm_yyyy(estudo['StartDate'][0])
    except:
        return False
    dataEstudo = datetime.strptime(dataEstudo, '%d-%m-%Y').date()
    datafinal = datetime.strptime(datafinal, '%d-%m-%Y').date()
    datainicial = datetime.strptime(datainicial, '%d-%m-%Y').date()
    if dataEstudo  >= datainicial and dataEstudo <= datafinal:
        return True
    return False