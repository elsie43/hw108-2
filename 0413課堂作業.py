#輸入x，以計算sin(x)/x
import math
x = eval(input("計算sin(x)/x，請輸入x="))
l = []
if isinstance(x, int) is True or isinstance(x, float) is True:
    l.append(x)
    if x == 0:
        print("分母為0無意義")
    
else:
    for i in x:
        l.append(i)
        if i == 0:
            print("分母為0無意義")

def cal(y):
    ans = [math.sin(i)/i for i in y] 
    print(ans)

cal(l)
