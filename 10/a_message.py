import time

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
filename = 'programming-a.txt'
str_1 = str(1)

# 第二个参数 w 告诉 Python，要以写入模式打开这个文件
# r 只读模式
# w 写入模式
# a 附加模式
# w+ 读写模式
# Python 只能将字符串写入文本文件。
# 要将数值是储存文本文件中，必须先使用函数 str() 将其转换为字符串格式
with open(filename, 'a') as file_object:
    file_object.write(f"{now} I also love finding meaning in large datasets.\n")
    file_object.write(f"{now} I love creating apps that can run in a browser.\n")
    file_object.write(f"{now} {str_1}\n")
