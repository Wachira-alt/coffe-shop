# test.py
from customer import Customer
from coffee import Coffee
from order import Order

cust = Customer("Dennis")
coffee = Coffee("Mocha")

cust.create_order(coffee, 4.0)
cust.create_order(coffee, 5.0)

print(coffee.num_orders())      # Output: 2
print(coffee.average_price())   # Output: 4.5
