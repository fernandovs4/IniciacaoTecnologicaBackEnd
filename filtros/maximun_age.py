
def maximumAge(estudo, idade_max):
    if estudo['MaximumAge'] == []:
        return True
    if int(estudo['MaximumAge'][0].split(" ")[0]) <= int(idade_max):
        return True
    return False

