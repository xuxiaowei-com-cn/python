def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"Making a {size}-inch pizza with the following toppings：")
    for topping in toppings:
        print(f"- {topping}")


def make_pizza_overview(*toppings):
    """概述要制作的披萨"""
    print(f"Making a pizza with the following toppings：")
    for topping in toppings:
        print(f"- {topping}")
