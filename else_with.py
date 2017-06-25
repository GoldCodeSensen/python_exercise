#在python中，else不一定非要和if搭配
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num%count == 0:
            print('%d的最大约数是%d' %(num, count))#用print打印%d数据的调用格式
            break
        count -= 1
    else:#这个else和while在一个缩进级别上，表示count<=1时的情况
        print('%d是素数' %num)

num = int(input("请输入一个数："))
showMaxFactor(num)


try:
    #检测范围
    with open("this_file_is_not_exist.txt") as f: #使用with语句，无论操作是否成功，都会将资源释放（比如关闭文件）
        print(f.read)#with_body
        #f.close()
except OSError as err:
    #出现异常后处理
    print("文件出错了")#结果会报出这句话
    print("错误原因是："+str(err))
#finally:
    #无论如何都要执行的操作
    #f.close()