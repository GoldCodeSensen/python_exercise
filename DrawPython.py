import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad,angle/2) #draw circle
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3) #forward distance

def main():
    turtle.setup(1300,800,-1,-1)
    pythonsize = 10
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    turtle.seth(-45) #set heading direction
    drawSnake(10, 90, 3, pythonsize)

main()