from tkinter import *
from tkinter import messagebox
import math
window = Tk()
window.title("H54086135 陳以新")

#存放輸入之數字
num1 = IntVar()
num2 = IntVar()
result = IntVar()

def minus():
    x = num1.get()-num2.get()  
    if x < 0:
        #y = round(math.fabs(x))
        y = -x
        warn = "金額不足，還差" + str(y) + "元"
        messagebox.showinfo("WARNING!", warn)
        
    else:
        return result.set(x)

receive = Label(window, text="收款NT$", width=30, bg="lightblue") 
n1      = Entry(window, width=50, textvariable=num1) 
price   = Label(window, text="應付NT$", width=30, bg="lightblue")
n2      = Entry(window, width=50, textvariable=num2)
change  = Label(window, text="找零NT$", width=30, bg="lightblue") 
n3      = Entry(window, width=50, textvariable=result) 
btn     = Button(window, text="計算找零", fg="#009FCC", command = minus)

#排版
receive.grid(row=0, column=0)
price.grid(row=1, column=0)
change.grid(row=2, column=0)
n1.grid(row=0, column=1)
n2.grid(row=1, column=1)
n3.grid(row=2, column=1)
btn.grid(row=3, column=0)

window.mainloop()
