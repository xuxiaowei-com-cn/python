from pizza import make_pizza, make_pizza_overview as overview

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

overview('pepperoni')
overview('mushrooms', 'green peppers', 'extra cheese')
