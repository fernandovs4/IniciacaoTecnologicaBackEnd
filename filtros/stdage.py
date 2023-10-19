
def stdAge(estudo, stdage):
    stdage = stdage.split(',')
    print(stdage)
    tem = True
    if stdage[0] == 'all':
        return True
    if len(stdage) != len(estudo['StdAge']):
        return False
    for idade in stdage:
        if idade not in estudo['StdAge']:
            tem = False
            break  

    return tem