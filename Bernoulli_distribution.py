p = float(input("Enter probablity of success (0 to 1)"))
x = int(input("Enter outcome (0 or 1)"))
c = 1

if x == 1:
    probablity = p
else:
    probablity = 1 - p
        
print("P(X=",x,")= ",probablity)

mean = p
var = p*(1-p)

print("Mean = ",mean)
print("variance = " ,var)