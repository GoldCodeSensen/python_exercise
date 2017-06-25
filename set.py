#集合，集合中不存在重复的元素
set1 = {1,2,3,4,5,3,2,2,1,6,4}
print(set1)#集合会自动剔除重复的元素，每个元素都是唯一的
set2 = set([1,2,3,4,5,2,3,4])#给set传入一个list
print(set2)
set3 = set((1,2,3,4,5,2,3,4))#给set传入一个tuple
print(set3)

#将一个list中的重复元素去除：现将list转化为集合，再将集合转化为list
list1 = [5,4,3,2,1,1,1,1,4,5]
list2 = list(set(list1))
print(list2)#打印的结果为[1, 2, 3, 4, 5]，可见虽然set很方便的提出了重复元素，但是它也破坏了list的顺序

set4 = set([1,2,3])
set4.add(0)#给集合中增加单个元素
set4.add((0,3,7,8,9))#给集合中增加一个元组
print('after add, set4 is '+ str(set4))
print('pop a element from set4, it is '+str(set4.pop()))#从集合中取出一个元素
set4.remove(3)#从集合中删除元素3
set5 = set4.copy()#复制一份set4的内容给set5
print('set5 is ' + str(set5))
set4.clear()

set6 = frozenset([1,3,4,5,6,7,0,23])#冰冻集合，集合中的元素不允许修改
