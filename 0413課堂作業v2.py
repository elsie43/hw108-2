#v2
import math
x = eval(input("計算sin(x)/x，請輸入x=")) #x為執行者輸入多數字 e.g. 1,3,5 或單一數字
l = [] #建立空集合用以存放執行者輸入之數字

if isinstance(x, int) is True or isinstance(x, float) is True: #當x是單一數字時
    l.append(x) #一樣將x先加入串列
    if x == 0: #sin0/0=1
        l.append(1)

else:
    for i in x: #當x為多數字(tuple)時
        l.append(i) #將每個數字加入串列
        if i == 0:#sin0/0=1
            l.append(1)
            
def cal(y):
    ans = [math.sin(i)/i for i in y] #將串列的每一元素做題目要求之計算
    print(ans) #列印出的ans為一串列，結果對應方才輸入之數字

cal(l)

