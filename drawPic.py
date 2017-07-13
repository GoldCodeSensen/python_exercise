import turtle
import random
def ground():
    turtle.hideturtle()
    turtle.speed(100)
    for i in range(400):
        turtle.pensize(random.randint(5,10))
        x = random.randint(-640,640)
        y = random.randint(-400,-1)
        r = abs(y)/450
        g = abs(y)/450
        b = abs(y)/450
        turtle.pencolor((r,g,b))#y值越小时，颜色越浅，便在屏幕中间实现渐变效果
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward(random.randint(40,100))

def snow():
    turtle.hideturtle()
    turtle.speed(100)
    turtle.pensize(2)
    for i in range(200):
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.pencolor((r,g,b))
        x = random.randint(-640,640)
        y = random.randint(-400,400)
        turtle.penup()
        turtle.goto(x,y)
        den = random.randint(5,11)
        snowsize = random.randint(7,12)
        turtle.pendown()
        for j in range(den):
            turtle.forward(snowsize)
            turtle.backward(snowsize)
            turtle.right(360/den)


def main():
    turtle.setup(1280,800,0,0)
    turtle.tracer(False)
    turtle.bgcolor("black")
    ground()
    snow()
    turtle.tracer(True)
    turtle.mainloop()
if __name__ == '__main__':
    main()