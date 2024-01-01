    
def Gender(estudo, masculino, feminino, todos, estudos_todos_generos):
    if estudo['Gender'] == []:
        if todos:
            return True
        else:
            return False
    if todos:
        return True

    if estudo['Gender'][0] == 'All' and estudos_todos_generos:
        return True
    
    if estudo['Gender'][0] == 'Female' and feminino:
        return True
   
    if estudo['Gender'][0] == 'Male' and masculino:
        

        return True
    
    return False