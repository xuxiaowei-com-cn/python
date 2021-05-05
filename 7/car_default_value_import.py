import car_default_value

my_car = car_default_value.Car('audi', 'a4', '2019')
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.odometer_reading = 23
my_car.read_odometer()

my_car.update_odometer(50)
my_car.read_odometer()

my_car.increment_odometer(5)
my_car.read_odometer()
