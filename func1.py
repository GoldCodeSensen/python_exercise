def myfunc1():
    print("I am GodCodeSensen")
myfunc1()
def myfunc2(name):#带参数的函数
    print("hello, I am "+name)
myfunc2("GodCodeSensen")
def myfunc3(name):#带参数和返回值的函数
    print("Who is "+name+"?")
    return "myfunc3 run SUCCESS"
print(myfunc3("GodCodeSensen"))

#关键字索引参数
def myfunc4(name,words):
    print(name+" says "+words)
myfunc4("sensen","I'm Code God")
myfunc4("I'm Code God","sensen")#当函数参数比较多时，容易弄错参数顺序
myfunc4(words="I'm Code God",name="sensen")#这时可以用实参给形参赋值的方式来输入参数

#函数的默认值参数
def myfunc5(name="myfunc5",words="you don't give me any argument"):
    print(name + " says " + words)
myfunc5()#调用时没有传入参数
myfunc5("life","you must be stiff")

#函数参数中包含收集参数，就像指针
def myfunc6(*param,x1="default value 1",x2="default value 2"):
    print("param is as flow:")
    print(param)
    print("x1 is "+x1)
    print("x2 is "+x2)
#test = [1,2,3,4,5,6]#打印出的test将是一个元组，而不是一个列表
test = "1,2,3,4,5,6"#打印出的test将是一个元组，而不是一个字符串
myfunc6(*test)#可见收集参数会将各种参数元素收集为元组

#python的所有函数都是有返回值的，如果没有人为确定返回值，则函数的返回值none
#python可以按照list或tuple来返回对象，实现返回多个变量

#全局变量
#函数不可以直接访问和修改全局变量，若要访问和修改，需要使用global关键字进行声明
orignal_price = float(input("请输入原价："))
def off(orignal):
#    global orignal_price
    print("the orignal price you give is " + str(orignal) + ", do u wanna change it?")
    change = input()
    if(change == 'Y' or change == 'y'):
        orignal_price = float(input("please re-input the orignal price:"))
    cut_off = float(input("请输入折扣："))
#    print("这里试图输出orignal_price",orignal_price)
    present_price = orignal_price*cut_off
    print("the present price is " + str(present_price))
off(orignal_price)
print("the orignal price is "+str(orignal_price))
#该程序运行会有如下结果：
#请输入原价：100
#the orignal price you give is 100.0, do u wanna change it?
#y
#please re-input the orignal price:200
#请输入折扣：0.8
#the present price is 160.0
#the orignal price is 100.0
##不加global关键字，创建的变量总是局部的

