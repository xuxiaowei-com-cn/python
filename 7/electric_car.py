import car


class ElectricCar(car.Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('telsa', 'model s', 2019)
print(my_tesla.get_descriptive_name())
