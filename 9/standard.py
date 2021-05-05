from random import randint, choice

# 模块 random 中的 函数 randint() 将两个整数作为参数，并随机返回一个位于者两个整数之间（含）的整数
print(randint(1, 6))

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 模块 random 中的 函数 choice() 将一个列表或元组作为参数，并随机返回其中的一个元素
print(choice(players))
