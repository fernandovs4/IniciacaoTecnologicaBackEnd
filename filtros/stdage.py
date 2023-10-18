
def stdAge(estudo, adulto, idoso, crianca, todos):
    if estudo['StdAge']
    if estudo['StdAge'] == []:
        if todos:
            return True
    if adulto and crianca and (('Adult' in estudo['StdAge']  or 'Child' in estudo['StdAge']) and len(estudo['StdAge']) == 1 or( ('Adult' in estudo['StdAge']  and  'Child' in estudo['StdAge']) and len(estudo['StdAge']) == 2 )):
        return True
    
    if adulto and idoso and (('Older Adult' in estudo['StdAge']  or 'Adult' in estudo['StdAge']) and len(estudo['StdAge']) == 1 or( ('Older Adult' in estudo['StdAge']  and  'Adult' in estudo['StdAge']) and len(estudo['StdAge']) == 2 )):
        return True
    
    if crianca and idoso and (('Older Adult' in estudo['StdAge']  or 'Child' in estudo['StdAge']) and len(estudo['StdAge']) == 1 or( ('Older Adult' in estudo['StdAge']  and  'Child' in estudo['StdAge']) and len(estudo['StdAge']) == 2 )):
        return True

    if adulto and 'Adult' in estudo['StdAge'] and len(estudo['StdAge']) == 1:
        return True
    
    if idoso and 'Older Adult' in estudo['StdAge'] and len(estudo['StdAge']) == 1:
        return True
    
    if crianca and 'Child' in estudo['StdAge'] and len(estudo['StdAge']) == 1:
        return True
    
    if todos:
        return True
    return False