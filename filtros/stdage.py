
def stdAge(estudo, stdage):
    if stdage == 'todas':
        return True
    stdage = stdage.split(',')
  
    tem = True
   
    if len(stdage) != len(estudo['StdAge']):
        return False
    for idade in stdage:
        if idade not in estudo['StdAge']:
            tem = False
            break  

    return tem