import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math
#2-1標準常態分佈的圖

x = np.arange(-4,4,0.01)
y = (1/((2*np.pi)**(1/2)) ) * np.exp(-x**2/2)
plt.plot(x,y,"b-")
plt.xlim((-4,4))
plt.ylim((-0.1,0.5))
plt.show()






