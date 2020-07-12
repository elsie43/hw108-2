#印星星
n = eval(input("height="))

for i in range (1, n+1):
  print(" "*(n-i), "*"*(2 * i -1))
