#印出指定矩陣並計算元素總和

#6-51 第四題 （原題目：由開發者決定矩陣形式，並計算總和）
print("有一矩陣如下：\n")
l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
ll = []
for i in range(len(l)):
  for j in range(len(l[i])):
    print(l[i][j],end = '\t')
    ll.append(l[i][j])
  print('\n')

#print("\n此矩陣中的所有元素和為",sum(ll))
print("此矩陣之元素總和為：",sum(ll))

#6-51 第四題 延伸為使用者可自行輸入矩陣
r = eval(input("請輸入列數："))
c = eval(input("請輸入行數："))
l = []
ll = []
sum = 0
for i in range(r):
  l.append([])
  for j in range(c):
    element = eval(input("請分次輸入矩陣元素（左至右，上至下）："))
    l[i].append(element)
    sum += element

def pr(x):
  for i in range(len(x)):
    for j in range(len(x[i])):
      print(x[i][j], end = '\t')
    print('\n')

print("\n以下為您設定的矩陣：\n")
pr(l)
print("此矩陣中之所有元素總和為：", sum)
