member = ["sensen","qiqi","jingjing"]
#for i in member:
#    print(i,len(i))
member.append("baba")
member.extend(["mama","baby"])
member.insert(0,"home")
for i in member:
    print(i,len(i))
temp = member[1]
member[1] = member[3]
member[3] = temp
for i in member:
    print(i,len(i))
list1 = [123,345,567,789]
list1 *= 3
for i in list1:
    print(i)
print(list1.count(123))
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
