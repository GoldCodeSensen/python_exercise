#__getattr__(self, name)
#定义当用户试图获取一个不存在的属性时的行为

#__getattribute__(self, name)
#定义该类的属性被访问时的行为

#__setattr__(self, name, value)
#定义当一个属性被设置时的行为

#__delattr__(self, name)
#定义当一个属性被删除时的行为

class C:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)#超类

    def __getattr__(self, name):
        print("getattr")

    def __setattr__(self, name, value):
        print("setattr")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)

c = C()
print(str(c.x))
c.x = 1
print(str(c.x))


class Rectangle:
    def __init__(self,x=0,y=0):
        self.width = x
        self.height = y

    # 定义当一个属性被设置时的行为.属性square虽然不存在，但是我们通过更改__setattr__方法使其完成预期功能
    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(key,value)#这里若不使用super，则会与self.width = x造成循环的递归调用

    def getArea(self):
        return self.width * self.height

r1 = Rectangle(4,5)
print("width is " + str(r1.width))
print("height is " + str(r1.height))
print("Area is " + str(r1.getArea()))

r1.square = 10
print("width is " + str(r1.width))
print("height is " + str(r1.height))
print("Area is " + str(r1.getArea()))

