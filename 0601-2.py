#建立一個二項分布試驗並將數據用matplotlib繪製成圖
import numpy as np
import matplotlib.pyplot as plt
sample = np.random.binomial(10, 0.5, 500)#建立一個二項分布試驗（以擲銅板為例）
print("試驗結果為：",sample)
print("此試驗之平均數：",np.mean(sample)) #求算術平均：驗證期望值接近n*p=10*0.5=5
print("此試驗之標準差：",np.std(sample)) #求標準差
print("此試驗之變異數：",np.var(sample)) #求變異數(標準差之平方)：驗證結果接近n*p(1-p)=10*0.5*(1-0.5)=2.5
plt.hist(sample, bins=100) #用matplotlib將數據畫成圖
plt.show()
