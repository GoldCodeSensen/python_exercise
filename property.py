#描述符：将某种特殊类型的类的实例 指派给 另一个类的属性
#特殊类型至少要实现以下三个方法的一个：
#__get__(self, instance, owner)
#__set__(self, instance, value)
#__delete__(self, instance)
class Celsius:
    def __init__(self,value = 26):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel*1.8+32      #从这里可以看出，instance是指该对象的实例（fah）所在的对象的实例
    def __set__(self, instance, value):
        instance.cel = (float(value)-32)/1.8

class Temperature:
    cel = Celsius()#特殊类型的类的实例
    fah = Fahrenheit()#特殊类型的类的实例

T = Temperature()
T.cel = 100
print("Celsius "+str(T.cel)+" is equal to Fahrenheit "+str(T.fah))
T.fah = 100
print("Fahrenheit "+str(T.fah)+" is equal to Celsius "+str(T.cel))

#魔术方法（__xxx__）都有固定的调用规则，描述符类就是通过重写魔术方法来实现的。