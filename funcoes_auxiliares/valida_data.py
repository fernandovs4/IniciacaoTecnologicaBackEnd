
def validaDatas(datainicial):
    try:
        data = datainicial.split('-')
        if len(data) != 3:
            return {"status":"Data inválida"}
        if len(data[0]) != 2 or len(data[1]) != 2 or len(data[2]) != 4:
            return {"status":"Data inválida"}
        if int(data[0]) > 31 or int(data[0]) < 1:
            return {"status":"Data inválida"}
        if int(data[1]) > 12 or int(data[1]) < 1:
            return {"status":"Data inválida"}
    except:
        return {"status":"Data inválida"}
    
    return True
