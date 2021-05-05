class Battery:
    """一个模拟电动汽车电瓶的简单尝试."""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性."""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条电瓶的描述."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印有关此电池可提供范围的声明."""

        if self.battery_size == 75:
            range_int = 260
        elif self.battery_size == 100:
            range_int = 315
        else:
            range_int = 0
        print(f"This car can go about {range_int} miles on a full charge.")
