# -*- coding: utf-8 -*-
"""0413課堂作業.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NVjcBp-aRT7m7hFkt_lVJY4zR216yVPH
"""

import math
def cal(x):
    ans = [math.sin(i)/i for i in x] 
    print(ans)

x = eval(input("計算sin(x)/x，請輸入x="))
l = []
for i in x:
  l.append(i)
  if i == 0:
    print("分母為0無意義")


cal(l)