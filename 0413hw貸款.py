#貸款試算，依提示輸入本金、利率與期限，計算每月應攤還之金額

def loan(p,iy,ny):
  im = iy / 12 / 100  #im月利率
  nm = ny * 12  #nm月數, ny 年數
  rate = (((1+im) ** nm) * im)/(((1+im) ** nm)-1) #本息平均月攤還率
  aveamount = p * rate #每月攤還金額
  print("每月應攤還金額：", aveamount)

print("貸款試算，請注意單位")
loan(eval(input("請輸入貸款本金(元)：")), eval(input("請輸入年利率(%)：")), eval(input("請輸入貸款年限（年）：")))

