
def minimunAge(estudo, idade_min):
    if estudo['MinimumAge'] == []:
        return True
    
    if int(estudo['MinimumAge'][0].split(" ")[0]) >= int(idade_min):
        return True
    return False