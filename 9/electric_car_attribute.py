import car


class ElectricCar(car.Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('telsa', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()