#用sympy做指定運算
import sympy as sp
x = sp.symbols('x') #define x

#1
f = (sp.exp(sp.sin(x))-1)/sp.sin(x) 
r1 = sp.limit(f,x,0) #f取極限(當x趨近於0)

#2
g = sp.exp(sp.cos(1/x)) 
r2 = sp.limit(g, x, sp.oo) #g取極限(當x趨近於無窮大)

#3
h = (sp.sin(x**2+1))**3 
r3 = sp.diff(h,x) #h對x微分

#4
z = x/((1+x**2)**2) 
r4 = sp.integrate(z, (x, 0, sp.oo)) #對x定積分(0積到無窮大)

#印答案
print("第1題答案為:",r1)
print("第2題答案為:",r2)
print("第3題答案為:",r3)
print("第4題答案為:",r4)


