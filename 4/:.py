magicians = ['Alice', 'David', 'Carolina', 'Lambert', 'Julie']

print(magicians)

# 复制全部
print(magicians[:])

# 复制前三个
print(magicians[:3])

# 复制后三个
print(magicians[-3:])

# 复制（索引）第 1 个到第 3 个
print(magicians[1:4])

# 遍历切片
for magician in magicians[1:4]:
    print(magician)
