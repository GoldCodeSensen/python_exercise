try:
    #检测范围
    f = open("this_file_is_not_exist.txt")
    print(f.read)
    f.close()
except OSError as err:
    #出现异常后处理
    print("文件出错了")#结果会报出这句话
    print("错误原因是："+str(err))
finally:
    #无论如何都要执行的操作
    f.close()