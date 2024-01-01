def filtra_por_fase(fase, estudo):
    if fase == 'nao_especificado':
        return True
    if fase == 'todas':
        return True
    fase = fase.split(',')
    fases_estudo = estudo['Phase']
    fase_estudo_alterado = []
    for f in fases_estudo:
        fase_estudo_alterado.append(f.replace('Phase ', ''))
    for f in fase:
        if f in fase_estudo_alterado:
            return True
    return False
  