import battery
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
        self.battery = battery.Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print(f"{self.make} {self.model} 没有油箱".title())


my_tesla = ElectricCar('telsa', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.get_range()
