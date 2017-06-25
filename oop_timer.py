import time as t
#注意类的方法名和属性名不能相同，否则，属性会覆盖方法
class Mytimer():
    def __init__(self):
        #类的属性都需要初始化
        self.__unit = ['年','月','日','时','分','秒']
        self.__carry = [0,12,30,24,60,60]
        self.__lasted = []#按年、月、日、时、分、秒的结构记录结果
        self.__lastedseconds = 0 #按秒记录结果
        self.__result = "init" #结果字符串

    #定义start方法
    def start(self):
        self.startime = t.localtime()
        print("计时开始。。。")

    #定义stop方法
    def stop(self):
        self.stoptime = t.localtime()
        self.__calc()
        print("计时结束。。。")

    #定义计算时间间隔的方法
    def __calc(self):
        self.__result = "精确计时："
        for index in range(6):
            self.__lasted.append(self.stoptime[index]-self.startime[index])
            if(index == 0):
                self.__lastedseconds += 31536000*self.__lasted[index]#year
            elif(index == 1):
                self.__lastedseconds += 2592000*self.__lasted[index]#month
            elif(index ==2):
                self.__lastedseconds += 86400*self.__lasted[index]#day
            elif(index == 3):
                self.__lastedseconds += 3600 * self.__lasted[index]  #hour
            elif(index == 4):
                self.__lastedseconds += 60*self.__lasted[index]#minute
            else:
                self.__lastedseconds += self.__lasted[index]#second

        #将各单位上的数值都换算成大于零的数
        for index in range(6):
            if self.__lasted[5-index] < 0:#当该单位上的时间小于零
                self.__lasted[5-index] += self.__carry[5-index]
                self.__lasted[5-index-1] -= 1

        #将换算后，非零值纳入结果字符串
        for index in range(6):
            if self.__lasted[index] > 0:
                self.__result += (str(self.__lasted[index])+self.__unit[index])

    #重新定义魔法方法__str__
    def __str__(self):#重写__str__函数，该函数需要返回一个字符串，不返回或返回其他类型，函数会出错
        print("计时时间约为%d秒" %(self.__lastedseconds))
        return self.__result

#按Mytimer类创建一个对象
t1 = Mytimer()
order = input("please enter 'start' to start the timer:")
while 1:
    if(order == "start"):
        t1.start()#调用该对象的类方法
        break
    else:
        order = input("please enter 'start' :")

#停止条件
order = input("please enter 'stop' to stop the timer:")
while 1:
    if(order == "stop"):
        t1.stop()
        print(t1)#这样调用会使print打印出__str__函数的返回值
        break
    else:
        order = input("please enter 'stop' :")