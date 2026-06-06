def shorterest_time(n, m, speeds):
    a , b , c , d = speeds
    
    if n == 0:
        return 0
    elif n == m:
        ele = b + c + n + b
        stair = n * d
        return min(ele , stair)
             
    else :
        ele = abs(m - n) * a + b + c + n * a + b
        stair = abs(n - m) * d + b + c + m * a + b
        return min(ele , stair)
            
    