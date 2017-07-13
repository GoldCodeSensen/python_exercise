import turtle
turtle.title('数据驱动的动态路径绘制')
turtle.setup(800,600)
pen = turtle.Turtle()
pen.color("red")
pen.width(5)
pen.shape("turtle")
pen.speed(2)
result = []
#file = open("drawpath_data.txt","r")
file = open("drawpath_data2.txt","r")
for line in file:
    result.append(list(map(float, line.split(',')))) #map 表示要对括号中的每一个元素做强转float的操作
print(result)
for i in range(len(result)):#以“前进-旋转”的循环画完图形
    pen.color((result[i][3],result[i][4],result[i][5]))#获取线条的颜色
    pen.fd(result[i][0])#前进的长度
    if result[i][1]:
        pen.right(result[i][2])#向左转多少度
    else:
        pen.left(result[i][2])#向右转多少度
turtle.done()