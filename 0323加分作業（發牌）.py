#隨機發牌後四位同學分別得到的牌

print("今有4位同學在玩牌，以下分別為四位同學取得之牌組(編碼):\n")
#x是牌組亂數 

import random
x = list(range(1, 53))
random.shuffle(x)

#順序：黑桃、紅心、方塊、梅花

a = x[0: 13]
b = x[13: 26]
c = x[26: 39]
d = x[39: 52]

print("甲同學擁有的牌組編碼", a)
print("乙同學擁有的牌組編碼", b)
print("丙同學擁有的牌組編碼", c)
print("丁同學擁有的牌組編碼", d,"\n")

#以a為例
'''
ia = 0
x = 0

for x in range(1,13):
  ia = a[x:x+1]
  x = x+1
  iax = eval(str(ia)) 
  print(iax//5)

'''
#甲同學的牌組
print("甲同學擁有的牌: ")
for x in a :
  tya = x//13
  numa = x % 13
  if tya == 0:
    if numa == 1:
      print("黑桃 A")
    if numa == 11:
      print("黑桃 J")
    if numa == 12:
      print("黑桃 Q")
    if numa == 0:
      print("黑桃 K")
    if 2 <= numa <=10: 
      print("黑桃", numa)
  if tya == 1:
    if numa == 1:
      print("紅心 A")
    if numa == 11:
      print("紅心 J")
    if numa == 12:
      print("紅心 Q")
    if numa == 0:
      print("紅心 K")
    if 2 <= numa <=10: 
      print("紅心", numa)
  if tya == 2:
    if numa == 1:
      print("方塊 A")
    if numa == 11:
      print("方塊 J")
    if numa == 12:
      print("方塊 Q")
    if numa == 0:
      print("方塊 K")
    if 2 <= numa <=10: 
      print("方塊", numa)
  if tya == 3:
    if numa == 1:
      print("梅花 A")
    if numa == 11:
      print("梅花 J")
    if numa == 12:
      print("梅花 Q")
    if numa == 0:
      print("梅花 K")
    if 2 <= numa <=10: 
      print("梅花", numa)

#乙同學的牌組
print("\n")
print("乙同學擁有的牌: ")
for x in b :
  
  tya = x//13
  numa = x % 13
  if tya == 0:
    if numa == 1:
      print("黑桃 A")
    if numa == 11:
      print("黑桃 J")
    if numa == 12:
      print("黑桃 Q")
    if numa == 0:
      print("黑桃 K")
    if 2 <= numa <=10: 
      print("黑桃", numa)
  if tya == 1:
    if numa == 1:
      print("紅心 A")
    if numa == 11:
      print("紅心 J")
    if numa == 12:
      print("紅心 Q")
    if numa == 0:
      print("紅心 K")
    if 2 <= numa <=10: 
      print("紅心", numa)
  if tya == 2:
    if numa == 1:
      print("方塊 A")
    if numa == 11:
      print("方塊 J")
    if numa == 12:
      print("方塊 Q")
    if numa == 0:
      print("方塊 K")
    if 2 <= numa <=10: 
      print("方塊", numa)
  if tya == 3:
    if numa == 1:
      print("梅花 A")
    if numa == 11:
      print("梅花 J")
    if numa == 12:
      print("梅花 Q")
    if numa == 0:
      print("梅花 K")
    if 2 <= numa <=10: 
      print("梅花", numa)


#丙同學的牌組
print("\n")
print("丙同學擁有的牌: ")
for x in c :
  
  tya = x//13
  numa = x % 13
  if tya == 0:
    if numa == 1:
      print("黑桃 A")
    if numa == 11:
      print("黑桃 J")
    if numa == 12:
      print("黑桃 Q")
    if numa == 0:
      print("黑桃 K")
    if 2 <= numa <=10: 
      print("黑桃", numa)
  if tya == 1:
    if numa == 1:
      print("紅心 A")
    if numa == 11:
      print("紅心 J")
    if numa == 12:
      print("紅心 Q")
    if numa == 0:
      print("紅心 K")
    if 2 <= numa <=10: 
      print("紅心", numa)
  if tya == 2:
    if numa == 1:
      print("方塊 A")
    if numa == 11:
      print("方塊 J")
    if numa == 12:
      print("方塊 Q")
    if numa == 0:
      print("方塊 K")
    if 2 <= numa <=10: 
      print("方塊", numa)
  if tya == 3:
    if numa == 1:
      print("梅花 A")
    if numa == 11:
      print("梅花 J")
    if numa == 12:
      print("梅花 Q")
    if numa == 0:
      print("梅花 K")
    if 2 <= numa <=10: 
      print("梅花", numa)

#丁同學的牌組
print("\n")
print("丁同學擁有的牌: ")
for x in d :
  tya = x//13
  numa = x % 13
  if tya == 0:
    if numa == 1:
      print("黑桃 A")
    if numa == 11:
      print("黑桃 J")
    if numa == 12:
      print("黑桃 Q")
    if numa == 0:
      print("黑桃 K")
    if 2 <= numa <=10: 
      print("黑桃", numa)
  if tya == 1:
    if numa == 1:
      print("紅心 A")
    if numa == 11:
      print("紅心 J")
    if numa == 12:
      print("紅心 Q")
    if numa == 0:
      print("紅心 K")
    if 2 <= numa <=10: 
      print("紅心", numa)
  if tya == 2:
    if numa == 1:
      print("方塊 A")
    if numa == 11:
      print("方塊 J")
    if numa == 12:
      print("方塊 Q")
    if numa == 0:
      print("方塊 K")
    if 2 <= numa <=10: 
      print("方塊", numa)
  if tya == 3:
    if numa == 1:
      print("梅花 A")
    if numa == 11:
      print("梅花 J")
    if numa == 12:
      print("梅花 Q")
    if numa == 0:
      print("梅花 K")
    if 2 <= numa <=10: 
      print("梅花", numa)
