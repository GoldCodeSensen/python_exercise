import pickle #泡菜，一般情况下，会将字典存放在pickle文件中，需要使用时加载。这样做有助于缩小程序大小
my_list = [1,3.14,'hello',[1,2,3]]
#建立一个泡菜文件
pickle_file = open('my_list.pkl','wb')#‘wb’表示以二进制写的形式打开
pickle.dump(my_list,pickle_file)#将my_list写入二进制文件pickle_file
pickle_file.close()#关闭该文件
pickle_file = open('my_list.pkl','rb')#‘rb’表示以二进制读的形式打开
my_list2 = pickle.load(pickle_file)#将二进制信息读出，放入my_list2中
print('my_list is '+str(my_list))
print('my_list2 is '+str(my_list2))

