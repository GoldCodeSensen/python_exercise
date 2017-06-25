class XY:
    def __init__(self,x,y):#构造函数
        self.x = x
        self.y = y
    def printxy(self):
        print('X = %d, Y = %d' %(self.x,self.y))
A = XY(3,4)
A.printxy()

class C:
    def __init__(self):
        print('now init is been called')
    def __del__(self):
        print('now del is been called')
#创建C类的实例，并将c1、c2、c3都指向该实例；当实例第一次被创建时，调用构造函数__init__
c1 = C()
print('c1 is created')
c2 = c1
print('c2 = c1')
c3 = c2
print('c3 = c2')
#逐一删除c1、c2、c3，在删除最后一个引用时，析构函数__del__得到调用
del c1
print('c1 is deleted')
del c2
print('c2 is deleted')
del c3
print('c3 is deleted')

print('*******************************************************')

#重写加减运算
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a = New_int(1)
b = New_int(2)
print('a+b = %d' %(a+b))
print('a-b = %d' %(a-b))

print('*******************************************************')


