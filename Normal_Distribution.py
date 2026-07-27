import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4 , 8 , 1000)

y = (1/np.sqrt(2*np.pi))*np.exp(-((x - 2)**2)/2) #here sigma is 1 and mean which is mu is 2

plt.plot(x , y , color = 'blue' , linewidth = '2')
plt.title("standard normal distribution")
plt.xlabel("x")
plt.ylabel("pribability density")
plt.grid(True)
plt.show()