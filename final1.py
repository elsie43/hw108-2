#期末考第一題：開發一GUI程式的收銀機，且要顯示找零方式
from tkinter import *
from tkinter import messagebox
import math
window = Tk()
window.title("H54086135 陳以新")

#存放輸入之數字
num1   = IntVar() #存放整數
num2   = IntVar()
result = IntVar()
xx     = StringVar()

def minus():
    x = num1.get()-num2.get()  
    if x < 0:
        #y = round(math.fabs(x))
        y = -x
        warn = "金額不足，還差" + str(y) + "元"
        messagebox.showinfo("WARNING!", warn)#跳視窗
        
    else:
        
        result.set(x)
        
        a = x//500
        b = (x%500)//100
        c = (x%100)//50
        d = (x%50)//10
        e = (x%10)//5
        f = x%5
        final = "五百"+str(a)+"張, "+"一百"+str(b)+"張, "+"五十元"+str(c)+"個, "+\
        "十元"+str(d)+"個, "+"五元"+str(e)+"個, "+"一元"+str(f)+"個"
        xx.set(final)
        
        
receive = Label(window, text="收款NT$", width=30, bg="lightblue") 
n1      = Entry(window, width=50, textvariable=num1) 
price   = Label(window, text="應付NT$", width=30, bg="lightblue")
n2      = Entry(window, width=50, textvariable=num2)
change  = Label(window, text="找零NT$", width=30, bg="lightblue") 
n3      = Entry(window, width=50, textvariable=result) 
btn     = Button(window, text="計算找零", fg="#009FCC", command = minus)
final   = Entry(window, textvariable=xx, width=60) 
#排版
receive.grid(row=0, column=0)
price.grid(row=1, column=0)
change.grid(row=2, column=0)
n1.grid(row=0, column=1)
n2.grid(row=1, column=1)
n3.grid(row=2, column=1)
btn.grid(row=3, column=0)
final.grid(row=3, column=1)
window.mainloop()
