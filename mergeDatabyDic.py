import turtle
dic1 = {}
dic2 = {}
f1 = open('emailADDR.txt','rb')
f2 = open('TellNumber.txt','rb')
f1.readline()#跳过第一行
f2.readline()#跳过第一行
lines1 = f1.readlines()
lines2 = f2.readlines()
for line in lines1:
    elements = line.split()
    dic1[elements[0]] = str(elements[1].decode('gbk'))
for line in lines2:
    elements = line.split()
    dic2[elements[0]] = str(elements[1].decode('gbk'))

lines = []
for key in dic1.keys():
    s = ''
    if key in dic2.keys():
        s = '\t'.join([str(key.decode('gbk')),dic1[key],dic2[key]])
        s+='\n'
    else:
        s = '\t'.join([str(key.decode('gbk')),dic1[key],str('---------')])
        s+='\n'
    lines.append(s)

for key in dic2.keys():
    s = ''
    if key not in dic1.keys():
        s = '\t'.join([str(key.decode('gbk')),str('--------'),dic2[key]])
        s+='\n'
    lines.append(s)
f3 = open('AddrsBook1.txt','w')
f3.writelines(lines)

f3.close()
f2.close()
f1.close()
