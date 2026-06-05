def frame(balls):   
    color = ""
    dec = {"R" : 1 , "Y" : 2 , "G" : 3 , "Bn" : 4 , "Be" : 5 , "P" : 6 , "Bk" : 7 , "W" : 0}
    score = 0
    i = 0  

    while(i < len(balls)):
        if balls[i : i + 2] in ('Bk' , 'Bn' , 'Be'):
            color = balls[i : i + 2]
            point = dec[color]
            i += 2
            num = ""

        else:
            if "W" in balls:
                return 'Foul'
            else:
                color = balls[i]

                i += 1
                point = dec[color]
                num = ""

        while (i < len(balls) and balls[i].isdigit()):
            num += balls[i]
            i += 1


        score += point*(int(num if num else "1"))
        
    if score > 147:
        return 'invalid data'   
    else:
        return score
        
    
   