import os
print(os.getcwd())#输出当前目录
os.chdir('/home')#改变当前目录
print(os.getcwd())#输出当前目录
print(os.listdir('/home/sen'))#列举‘/home/sen’目录下的内容，包括文件和目录
os.chdir('/home/sen/Documents')
os.mkdir('./TEST')
os.rmdir('./TEST')
#......