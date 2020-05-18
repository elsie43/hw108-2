tcoding = [] #全班計程成績存入空串列
tacc = [] #全班會計成績存入空串列
tcal=[] #全班微積分成績存入空串列
print("執行時，請依序輸入會計、計算機程式、微積分之分數\n")
class Student: 
    num = 0 #存放全班人數
    def __init__(self,name="no name"):
        """可在建立物件時新增學生名字
        e.g. s1 = Student("Amy")，未新增則預設 no name"""
        self.name = name
        self.__class__.num += 1 #每新增一物件就+1
        
    def getGrade(self, acc = 0,coding = 0,cal = 0,Performance = 0): #getGrade方法求單一學生平均成績
        tacc.append(acc)
        tcoding.append(coding)
        tcal.append(cal)
        self.__per = Performance #操行成績的私有方法
        ave = (coding + acc + cal)/3
        print(self.name,"除操行外三科之平均成績為：" ,ave, "分")

    def getPerformance(self):#讀取操行成績
        p = self.__per 
        print(self.name,"的操行成績為", p, "分")
        
def bonus(): #額外：求全班人數與全體平均
    x = Student.num #全班人數
    print("全班共",x,"人")
    print("全班之會計平均分數為：", sum(tacc)/x, "分")
    print("全班之計程平均分數為：", sum(tcoding)/x, "分")
    print("全班之微積分平均分數為：", sum(tcal)/x,"分")
    print("全班之會計分數最高分為：", max(tacc), "分")
    print("全班之計程分數最高分為：", max(tcoding), "分")
    print("全班之微積分分數最高分為：", max(tcal), "分")



#main
s1 = Student("Mary")
s2 = Student("David")
s3 = Student("Bob")
s4 = Student("Candice")
s5 = Student("Sandra")
s1.getGrade(90,78,85,80)
s2.getGrade(87,92,90,70)
s3.getGrade(78,85,80,85)
s4.getGrade(80,95,90,90)
s5.getGrade(69,80,85,50)
s1.getPerformance()
s2.getPerformance()
s3.getPerformance()
s4.getPerformance()
s5.getPerformance()
print('\n')
bonus()

