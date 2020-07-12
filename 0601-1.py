#讀取指定文字檔之數字並將其設定成矩陣，並做指定之運算
import numpy as np
a = np.loadtxt("chap14.txt",delimiter=',', usecols = (0,1,2,3)) #a只讀取1~4行
b = np.loadtxt("chap14.txt",delimiter=',', usecols = 4) #b只讀取第5行
ainv = np.linalg.inv(a) #a的反矩陣
bre = b.reshape(4,1) #b轉置()
x = ainv @ bre
print("x矩陣結果為：\n",x,"\n")
