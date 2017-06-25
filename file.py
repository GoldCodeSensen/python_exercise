#'r'以只读方式打开文件（默认）
#'w'以写入方式打开文件，会覆盖之前写入的内容
#'x'如果文件已经存在，就会报错
#'a'以追加写入的方式打开
#'b'以二进制模式打开
#'t'以文本模式打开（默认）
#'+'可读写模式
#'U'通用换行符支持
f = open('/home/sen/Documents/notes_python.txt')
print('read 10 element, they are \n'+ f.read(10) + '\n')#打印文件内容的前10个字符
f.seek(0,0)#将操作位置移动到最开始
print('read all element, they are \n'+ f.read())#读取文件的全部内容
f.close()#关闭文件