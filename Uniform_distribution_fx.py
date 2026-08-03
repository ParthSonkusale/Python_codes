import matplotlib.pyplot as plt
import numpy as np

a = 4 
b = 10

x = np.linspace(0,20,1000)
y = np.where((x>a)&(x<b),1/(b - a),0)

plt.plot(x,y,color = 'blue' , linewidth = '2')
plt.title("Uniform Distribution")
plt.xlabel("X")
plt.ylabel("prob dens")
plt.grid(True)
plt.show()

