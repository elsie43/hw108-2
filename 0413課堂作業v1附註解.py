#v1
import math
def cal(x): 
    ans = [math.sin(i)/i for i in x] #將串列的每一元素做題目要求之計算
    print(ans)

x = eval(input("計算sin(x)/x，請輸入x=")) #x為執行者輸入多數字 e.g. 1,3,5 型別為tuple
l = [] #建立空集合用以存放執行者輸入之數字
for i in x: #將執行者輸入之數字一一加入串列
  l.append(i) 
  if i == 0:
    print("分母為0無意義") #分母不得為0

cal(l)

