#2-2 從負無窮大積到k的結果
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math
a = sp.symbols('a')
f = ((2*sp.pi)**(-1/2))  * sp.exp(-a**2/2)
k = eval(input("輸入一個數k:"))
result1 = (sp.integrate(f,(a,-sp.oo,k))).evalf()
print("the result using sympy:", result1)
