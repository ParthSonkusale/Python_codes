def gcd(m,n):
    com_fac = []
    for i in range (1,min(m+1 , n+1)):
        if m%i == 0 and n%i == 0:
            com_fac.append(i)
            
    return(com_fac[-1])    
            
        