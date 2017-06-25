#递归算法关键点:1.调用函数自身的行为 2.有停止条件
#下面举一个计算阶乘的例子
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
print(factorial(10))

#递归举例，计算斐波那契数列
def fabo(x):
    if x > 2:
        return fabo(x-1)+fabo(x-2)
    elif x == 2:
        return 1
    elif x == 1:
        return 1
print(fabo(20))

#用递归解决汉诺塔
def hanoi(n,A,B,C):
    if n==1:
        print(A,"->",C)
    else:
        hanoi(n-1,A,C,B)#将n-1个盘由A移动到B
        print(A,"->",C)#将第n个盘由A移动到C
        hanoi(n-1,B,A,C)#将将n-1个盘由B移动到C
hanoi(4,"A","B","C")