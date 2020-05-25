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
        y = round(math.fabs(x))
        messagebox.showinfo("WARNING!", "金額不足")
        
    else:
        return result.set(x)

receive = Label(window, text="收款NT$",width=30, bg="lightblue") #收款
n1 = Entry(window, width=50, textvariable=num1) #輸入收款
price = Label(window, text="應付NT$", width=30, bg="lightblue") #應付
n2 = Entry(window, width=50, textvariable=num2) #輸入應付
change = Label(window, text="找零NT$",width=30, bg="lightblue") #找零 
n3 = Entry(window, width=50, textvariable=result) #跳出找零
btn = Button(window, text="確定", fg="blue", command = minus)

#排版
receive.grid(row=0, column=0)
n1.grid(row=0, column=1)
price.grid(row=1, column=0)
n2.grid(row=1, column=1)
change.grid(row=2, column=0)
n3.grid(row=2, column=1)
btn.grid(row=3, column=0)

window.mainloop()
