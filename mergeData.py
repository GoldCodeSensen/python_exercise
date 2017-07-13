import turtle
list1_name = []
list1_tele = []
list2_name = []
list2_email = []
f1 = open('emailADDR.txt','rb')
f2 = open('TellNumber.txt','rb')
f1.readline()#跳过第一行
f2.readline()#跳过第一行
lines1 = f1.readlines()
lines2 = f2.readlines()
for line in lines1:
    elements = line.split()
    list1_name.append(str(elements[0].decode('gbk')))
    list1_tele.append(str(elements[1].decode('gbk')))
for line in lines2:
    elements = line.split()
    list2_name.append(str(elements[0].decode('gbk')))
    list2_email.append(str(elements[1].decode('gbk')))
lines = []
lines.append('姓名\t    电话\t    邮箱\n')
for i in range(len(list1_name)):
    s = ''
    if list1_name[i] in list2_name:
        j = list2_name.index(list1_name[i])
        s = '\t'.join([list1_name[i],list1_tele[i],list2_email[j]])
        s+='\n'
    else:
        s = '\t'.join([list1_name[i],list1_tele[i],str('---------')])
        s+='\n'
    lines.append(s)
for i in range(len(list2_name)):
    s = ''
    if list2_name[i] not in list1_name:
        s = '\t'.join([list2_name[i],str('--------'),list2_email[i]])
        s+='\n'
    lines.append(s)
f3 = open('AddrsBook.txt','w')
f3.writelines(lines)

f3.close()
f2.close()
f1.close()
