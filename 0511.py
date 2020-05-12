tcoding = [] #全班計程成績存入空串列
tacc = [] #全班會計成績存入空串列
tcal=[] #全班微積分成績存入空串列
print("執行時，請依序輸入計算機程式、會計、微積分之分數")
member = [] #建立空串列以存放學生名字

class s:
    num = len(member)
    
    def __init__(self,name="no name"):
        """可在建立物件時新增學生名字
        e.g. S1 = Student("Amy")，未新增則預設 no name"""
        member.append(name) #每執行一次，就在串列新增學生名以計算學生數
        self.name = name
        #self.num = len(self.member)
        """for self.num in range(len(member)):
            self.num += 1"""
    def g(self, coding = 0,acc = 0,cal = 0): #單一學生平均成績
        tcoding.append(coding)
        tacc.append(acc)
        tcal.append(cal)
        ave = (coding + acc + cal)/3
        print(self.name,"三科之平均成績為：" ,ave, "分")
        
"""def count():
    print(len(s.member))"""
    
def Coding():
    print("全班之計程平均分數為：", sum(tcoding)/len(member), "分")
    print("全班之計程分數最高分為：", max(tcoding), "分")
    
def Accounting():
    print("全班之會計平均分數為：", sum(tacc)/len(member), "分")
    print("全班之會計分數最高分為：", max(tacc), "分")
    
def Calculus():
    print("全班之微積分平均分數為：", sum(tcal)/len(member),"分")
    print("全班之微積分分數最高分為：", max(tcal), "分")
