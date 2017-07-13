#from turtle import *
#from datetime import *
import turtle
import datetime

def Skip(step):
    turtle.penup()#抬起画笔
    turtle.forward(step)#向前移动step
    turtle.pendown()#落笔


def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    turtle.reset()
    Skip(-length * 0.1)#将笔挪到-0.1×length处
    turtle.begin_poly()#开始画线
    turtle.forward(length * 1.1)#向前画1.1×length的长度
    turtle.end_poly()#结束画线
    handForm = turtle.get_poly()#将所画形状get到
    turtle.register_shape(name, handForm)#将该形状注册为“name”


def Init():
    global secHand, minHand, hurHand, printer
    #重置Turtle指向北
    turtle.mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 125)
    mkHand("minHand", 130)
    mkHand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()


def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)#线条粗细为7
    for i in range(60):
        Skip(radius)#将画笔移动表盘半径的距离
        if i % 5 == 0:
            turtle.forward(20)#长度为20的线段
            Skip(-radius - 20)#回到原点
        else:
            turtle.dot(5)#画一个点,粗细为5
            Skip(-radius)#返回原点
        turtle.right(6)#将turtle的方向向右旋转6度


def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)


def Tick():
    # 绘制表针的动态显示
    t = datetime.datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0

    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)
    turtle.ontimer(Tick, 100)  # 100ms后继续调用tick


def main():
    turtle.tracer(False)
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()


if __name__ == "__main__":
    main()