class Person:
    __name = 'helloA'  #双下滑线表示这个属性是私有的，不能被直接访问
    def getname(self):
        return self.__name
class Person1:
    name = 'helloB'
    def getname(self):
        return self.name
a = Person()
b = Person1()
#print(a.__name)  #直接访问私有属性会导致错误
print(a.getname()) #可以通过该对象的方法来访问私有属性
print(b.name)  #公有的属性可以直接被访问
print(b.getname())

#继承
class XX:
    def hello(self):
        print("hello parent")
class YY(XX): #表示类YY是继承类XX的
    pass
class ZZ(XX):
    def hello(self):  #子类中定义了与父类中同名的函数，会覆盖父类中的函数定义
        print('hello child')
y = YY()
y.hello()
z = ZZ()
z.hello()

#多重继承
class base1:
    def fool1(self):
        print('Im fool1')
class base2:
    def fool2(self):
        print('Im fool2')
class base(base1,base2): #子类继承了两个父类的属性，将同时拥有fool1和fool2方法
    pass

A = base()
A.fool1()
A.fool2()
