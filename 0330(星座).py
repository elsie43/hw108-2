#依提示分別輸入出生月份與日期以判別星座

print("請輸入生日\n")
m = eval(input("月份："))
d = eval(input("日期："))
print("\n您的星座是：")

if m == 1:
  if d <= 19:
    print("摩羯座")
  elif d >= 20 and d <= 31:
    print("水瓶座")
  else:
    print("error")


elif m == 2:
  if d <= 18:
    print("水瓶座")
  elif d >= 19 and d <= 29:
    print("雙魚座")
  else:
    print("error")

elif m == 3:
  if d <= 20:
    print("雙魚座")
  elif d >= 21 and d <= 31:
    print("牡羊座")
  else:
    print("error")

elif m == 4:
  if d <= 19:
    print("牡羊座")
  elif d >= 20 and d <= 30:
    print("金牛座")
  else:
    print("error")

elif m == 5:
  if d <= 20:
    print("金牛座")
  elif d >= 21 and d <= 31:
    print("雙子座")
  else:
    print("error")

elif m == 6:
  if d <= 21:
    print("雙子座")
  elif d >= 22 and d <= 30:
    print("巨蟹座")
  else:
    print("error")


elif m == 7:
  if d <= 22:
    print("巨蟹座")
  elif d >= 23 and d <= 31:
    print("獅子座")
  else:
    print("error")

elif m == 8:
  if d <= 22:
    print("獅子座")
  elif d >= 23 and d <= 31:
    print("處女座")
  else:
    print("error")

elif m == 9:
  if d <= 22:
    print("處女座")
  elif d >= 23 and d <= 30:
    print("天秤座")
  else:
    print("error")

elif m == 10:
  if d <= 23:
    print("天秤座")
  elif d >= 24 and d <= 31:
    print("天蠍座")
  else:
    print("error")

elif m == 11:
  if d <= 22:
    print("天蠍座")
  elif d >= 23 and d <= 30:
    print("射手座")
  else:
    print("error")

elif m == 12:
  if d <= 21:
    print("射手座")
  elif d >= 22 and d <= 31:
    print("摩羯座")
  else:
    print("error")

else:
  print("error")
