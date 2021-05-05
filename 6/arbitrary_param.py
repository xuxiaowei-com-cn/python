# 形参 *toppings 让 Python 创建一个名为 toppings 的元组，并将收到的所有参数值都封装到这个元组中

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza_overview(*toppings):
    """概述要制作的披萨"""
    print(f"Making a pizza with the following toppings：")
    for topping in toppings:
        print(f"- {topping}")


make_pizza_overview('pepperoni')
make_pizza_overview('mushrooms', 'green peppers', 'extra cheese')
