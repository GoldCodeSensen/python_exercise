#内嵌函数：在函数定义中定义的函数
def func1(x):
    def inner_func(y):
        return x*y
    return inner_func
i = func1(5)
print("first call, result is ",i)
print("second call, result is ",i(5))
print("call as myfunc7(5)(5), result is ",func1(5)(5))#注意内嵌函数的参数传入形式

def func2():
    x = 5
    def inner_func():
#        nonlocal x
#        x *= x
        return x*x #return 是可以识别x的，但是inner_func函数内部对x进行操作就不行；除非用nonlocal关键字来声明
    return inner_func
print("result is ",func2()())#函数func2有内嵌函数，所以在调用时需要给它传递参数，即使参数为空

#匿名函数
y = lambda x:2*x+1#x为函数的参数，2*x+1为函数的返回值
print(y(2))

#过滤器filter
print(list(filter(None,[1,2,0,False,True])))
#输出结果为[1, 2, True]，filter的功能为过滤出列表[1,2,0,False,True]经过None处理的结果为True的部分
#再举一例
print(list(filter(lambda x:x%2,range(10))))
#输出结果为[1,3,,5,7,9]，range(10)为[0,1,2,3,4,5,6,7,8,9]，过滤出对2取余为真的部分

#map方法：返回将可迭代对象中的所有元素进行lambda函数处理后的结果
print(list(map(lambda x:x*2,range(10))))
#结果为[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]，可以看出对所有元素进行了乘2操作

