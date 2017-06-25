#类的组合：把类的实例化放在新的类中
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:#类Pool将Turtle类和Fish类实例化，作为自己的元素
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print('There are %d turtles and %d fishes in the pool' %(self.turtle.num,self.fish.num))

A = Pool(10,200)
A.print_num()


#property（属性函数）:property(fget,fset,del,doc)，注意它的参数顺序
class C:
    def __init__(self,size = 10):#构造函数，定义了一个类“C”的变量size
        self.size = size

    def getsize(self):
        return self.size

    def setsize(self,x):
        self.size = x

    def delsize(self):
        del self.size
    # 用property作为方法装饰器，将类的方法变为和属性一样的操作。
    # 好处在于，这种方式保持了对象对外的形式统一；即便要修改类内部内容，也不会影响对外接口
    x = property(getsize,setsize,delsize) #经过属性函数的转化，x可以看作类的一个属性

DD= C()
print('size is %d' %(DD.x))
DD.x = 18
print('size is %d' %(DD.x))

