import numpy as np
import math as m
import matplotlib.pyplot as plt

#0608hw1
x   = np.linspace(-np.pi,np.pi,10000)#定義x從-pi~pi(radians)

sin = np.sin(x)
cos = np.cos(x)
tan = np.tan(x)
cot = 1/tan
sec = 1/cos
csc = 1/sin
plt.figure(figsize=(8,6))

#1.sin
plt.subplot(331)
plt.plot(np.degrees(x),sin,"b-",label="sin(x)") #radians轉degrees,設定圖例
plt.title("y=sin(x)")
plt.legend() #show label
plt.ylim((-2,2))
plt.xlabel("degrees")
plt.xticks(np.arange(np.degrees(-np.pi),np.degrees(np.pi+1),90),\
          ("-180°",'-90°','0°','90°',"180°"))

#2.cos
plt.subplot(332)
plt.plot(np.degrees(x),cos,"g-",label="cos(x)")#radians轉degrees,設定圖例
plt.ylim((-2,2))
plt.legend()
plt.title("y=cos(x)")
plt.xlabel("degrees")
plt.xticks(np.arange(np.degrees(-np.pi),np.degrees(np.pi+1),90),\
          ("-180°",'-90°','0°','90°',"180°"))

#3.tan
plt.subplot(333)
plt.plot(np.degrees(x),tan,"r-",label="tan(x)")#radians轉degrees,設定圖例
plt.legend()#show label
plt.ylim((-2,2))
plt.title("y=tan(x)")
plt.xlabel("degrees")
plt.xticks(np.arange(np.degrees(-np.pi),np.degrees(np.pi+1),90),\
           ("-180°",'-90°','0°','90°',"180°"))

#4.csc
plt.subplot(337)
plt.plot(np.degrees(x),csc,"b-",label="csc(x)")#radians轉degrees,設定圖例
plt.legend()#show label
plt.ylim((-2,2))
plt.title("y=csc(x)")
plt.xlabel("degrees")
plt.xticks(np.arange(np.degrees(-np.pi),np.degrees(np.pi+1),90),\
          ("-180°",'-90°','0°','90°',"180°"))

#5.sec
plt.subplot(338)
plt.plot(np.degrees(x),sec,"g-",label="sec(x)")#radians轉degrees,設定圖例
plt.legend()#show label
plt.ylim((-2,2))
plt.title("y=sec(x)")
plt.xlabel("degrees")
plt.xticks(np.arange(np.degrees(-np.pi),np.degrees(np.pi+1),90),\
          ("-180°",'-90°','0°','90°',"180°"))

#6.cot
plt.subplot(339)
plt.plot(np.degrees(x),cot,"r-",label="cot(x)")#radians轉degrees,設定圖例
plt.legend()#show label
plt.ylim((-2,2))
plt.title("y=cot(x)")
plt.xlabel("degrees")
plt.xticks(np.arange(np.degrees(-np.pi),np.degrees(np.pi+1),90),\
          ("-180°",'-90°','0°','90°',"180°"))

plt.show()


