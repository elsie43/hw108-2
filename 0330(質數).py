#輸入一整數n，列出小於n的所有質數

n = eval(input("請輸入任意正整數 n = "))
print("以下為小於", n, "的所有質數：")

for i in range(2, n):
  for j in range (2, i):
    if i % j == 0:
      break
  else:
    print(i)
