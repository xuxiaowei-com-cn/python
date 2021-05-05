import time

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write(f"{now} I also love finding meaning in large datasets.\n")
    file_object.write(f"{now} I love creating apps that can run in a browser.\n")
