from filtros.gender import Gender
from filtros.stdage import stdAge
from filtros.filtra_por_data import filtra_por_data
from filtros.filtra_por_fase import filtra_por_fase
from filtros.overal_status import overalStatus
from filtros.minimun_age import minimunAge
from filtros.maximun_age import maximumAge

def filtraDados(dadosTabela, dados, data = False, fase=False, idade_min=False, idade_max=False,  status=False,gender=False, stdage=False):
  
    for estudo in dados:
        if data:
            if not filtra_por_data(data[0], data[1], estudo):
                continue
            
        if fase:
            if not filtra_por_fase(fase, estudo):
                continue

        if idade_min:
            if not minimunAge(estudo, idade_min):
                continue

        if idade_max:
            if not maximumAge(estudo, idade_max):
                continue

        if status:
            # if status == 'Todos':
            if not overalStatus(estudo,status):
                    continue
          

        if gender:
            if gender == 'masculino':
                if not Gender(estudo, True, False, False, False):
                    continue
            elif gender == 'feminino':
                if not Gender(estudo, False, True, False,False ):
                    continue
            elif gender == 'todos':
                if not Gender(estudo, False, False,False,True):
                    continue
            elif gender == 'todos_generos':
                if  not Gender(estudo, False, False,True,False):
                    continue

        if stdage:
            if not stdAge(estudo, stdage)
        
            if stdage == 'adulto':
                if not stdAge(estudo, True, False, False, False):
                    continue
            elif stdage == 'idoso':
                if not stdAge(estudo, False, True, False, False):
                    continue
            elif stdage == 'crianca':
                if not stdAge(estudo, False, False, True, False):
                    continue
            elif stdage == 'todos':
                if not stdAge(estudo, False, False, False, True):
                    continue
            elif stdage == 'adulto_idoso' or stdage == 'idoso_adulto':
                if not stdAge(estudo, True, True, False, False):
                    continue
            elif stdage == 'adulto_crianca' or stdage == 'crianca_adulto':
                if not stdAge(estudo, True, False, True, False):
                    continue
            elif stdage == 'idoso_crianca' or stdage == 'crianca_idoso':
                if not stdAge(estudo, False, True, True, False):
                    continue

        dadosTabela['estudos'].append(estudo)
    return dadosTabela
