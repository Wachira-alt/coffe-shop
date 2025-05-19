from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Dennis")
c2 = Customer("Joy")
coffee = Coffee("Latte")

c1.create_order(coffee, 3.0)
c1.create_order(coffee, 2.0)
c2.create_order(coffee, 6.0)

top = Customer.most_aficionado(coffee)
print(top.name)  # Output: "Dennis" (5.0) vs Joy (6.0)
