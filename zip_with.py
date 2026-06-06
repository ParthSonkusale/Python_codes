def add(a1, a2):
    return a1 + a2

def sub(a1, a2):
    return a1 - a2

def mul(a1, a2):
    return a1 * a2

def div(a1, a2):
    return a1 // a2

def maximum(a1, a2):
    if a1 > a2:
        return a1
    return a2

def power(a1, a2):
    return a1 ** a2     

def zip_with(fn,a1,a2):
    result = []
    for i in range(min(len(a1) , len(a2))):   
         result.append(fn(a1[i] , a2[i]))
            
    return result        
    
    
    
    