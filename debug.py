from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Joy")
coffee1 = Coffee("Latte")

order1 = Order(c1, coffee1, 4.5)
print(order1.customer.name)     
print(order1.coffee.name)       
print(order1.price)             
