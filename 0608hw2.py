import matplotlib.pyplot as plt
import numpy as np
a = np.loadtxt("ch15_homework.txt",delimiter='\t', usecols = 0) 
b = np.loadtxt("ch15_homework.txt",delimiter='\t', usecols = 1) 
plt.plot(a, b, "b*")
plt.yticks(np.arange(0,0.31,0.05))
plt.show()
