height = [1,8,6,2,5,4,8,3,7]
Area = [ ]
cnt_2 = 0
for i in range(len(height)):
    cnt_2 += 1 
    cnt_1  = 0
    for j in range(len(height)):
        width =cnt_1 - (cnt_2 - 1)
        if height[i]<=height[j]:
            lenght = height[i]*width
            cnt_1 += 1
            Area.append(lenght)
        else :    
            lenght = height[j]*width
            cnt_1 += 1
            Area.append(lenght)
    
Area_max = max(Area)        
print(Area_max)       