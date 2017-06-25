#定义方式1：使用花括号；键值和内容之间用冒号隔开
dict1 = {'李宁':'一切皆有可能', '耐克':'Just do it', '阿迪达斯':'impossible is noting'}
print('耐克的广告语是: '+dict1['耐克'])#注意：字典是用方括号查找的
#定义方式2：
dict2 = dict(((1,'一'),(2,'二'),(3,'三儿'),(4,'四儿'),(5,'五儿')))#注意这里括号的数量，必须括两层
print('number 3 is '+dict2[3])
#定义方式3：
dict3 = dict(x='一',y='二',z='三儿',o='四儿',p='五儿')#这里的键值不能是有具体值的表达式
dict3['z'] = 'nothing'
print('number 3 is '+dict3['z'])#访问时需要加引号
print(dict3)

dict4 = {}
print(dict4.fromkeys((1,2,3)))#fromkeys会重新创建一个新的字典，而不是修改已有字典dict4的内容
print(dict4)
print(dict4.fromkeys((1,2,3),'hello'))#将索引1,2,3的映射都设置为hello
print(dict4)


dict5 = dict(((1,'hello1'),(2,'hello2'),(3,'hello3'),(4,'hello4'),(5,'hello5'),(6,'hello6')))
print(dict5.copy())#打印出dict5的复制品
print(dict5.items())#按（键，值）的形式打印出字典的元素
print(dict5.values())#只打印出字典的值
print(dict5.keys())#只打印出字典的键
print(dict5.get(1))
print(dict5.get(7))#当尝试获取字典中没有的元素时，会返回None
dict5.clear()#清除字典
