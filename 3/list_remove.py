bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'redline', 'redline']

print(bicycles)

bicycles.remove('trek')

print(bicycles)

try:
    bicycles.remove('trek')
except ValueError:
    print('trek 不存在，删除失败')

print(bicycles)

print()

# 仅能删除第一个值
bicycles.remove('redline')

print(bicycles)

# 删除所有相同的值
while 'redline' in bicycles:
    bicycles.remove('redline')

print(bicycles)
