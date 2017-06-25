#这个python脚本实现了将test.txt中不同人所说的话分文件储存的操作
def save_file(A,B,count):
    file_name_A = 'A_' + str(count) + '.txt'
    file_name_B = 'B_' + str(count) + '.txt'
    A_file = open(file_name_A, 'w')
    B_file = open(file_name_B, 'w')
    A_file.writelines(A)
    B_file.writelines(B)
    A_file.close()
    B_file.close()

def split_file(file_name):
    f = open(file_name)
    A = []#定义两个空列表，分别用来储存两个人所说的话。
    B = []
    count = 1
    for each_line in f:
        #这里的each_line可以是其他任何字符串，这里之所以可以调用split方法，是因为这条for xx in file语句潜在规定了这是文件的某一行。
        if each_line[:6] != '******':
            (role, speak) = each_line.split(':',1)#用元组来分开储存说话的人和所说的话
            #根据不同的人，将说话的内容分别添加到不同的列表中
            if role == 'A':
                A.append(speak)
            elif role == 'B':
                B.append(speak)
        else:
            save_file(A, B, count)#调用save_file函数将两个人对话的内容分别存放在对应的文件中

            count += 1#计数累加
            #一轮过后，将A、B列表都清空
            A = []
            B = []

    save_file(A,B,count)#储存最后一块数据

split_file('test.txt')