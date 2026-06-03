from sympy import symbols, sympify , Poly

x = symbols('x')#for creation of the veriable

# in python 3x = 3*x and x^2 = x**2 , x^3 = x**3 
exp = sympify("3*x**4 - 2*x**2 + x - 10")#for creatin of str equation and covert into math expression

p = Poly(exp , x)#this use for convert math expression into polynomial

#we can access each term induvidualy from exp as exp.arge
for power , coeff in p.terms(): #p.terms() = ((power,),coeff) of the polynomial equation
#   for i in range(der):
        if power[0] == 0:
            print(f"{coeff} -> 0")
        else:
            n_coeff = power[0] * coeff
            n_power = power[0] - 1 # power = tuplet = (x,) so we extract the x by power[0]
            print(f"{coeff}*x**{power[0]} -> {n_coeff}*x**{n_power}" )

