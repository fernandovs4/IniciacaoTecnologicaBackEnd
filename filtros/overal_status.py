
def overalStatus(estudo, status):
    status = [i.lower() for i in status.split(',')]

    for st in status:
        if len(estudo['OverallStatus']) == 1:
            if estudo['OverallStatus'][0].lower() == st:
                return True
    if status == ['todos'] or status == []:
        return True
    return False