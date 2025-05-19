from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Dennis")
c2 = Customer("Alice")
cof1 = Coffee("Espresso")
cof2 = Coffee("Latte")

o1 = Order(c1, cof1, 3.5)
o2 = Order(c1, cof2, 4.0)
o3 = Order(c2, cof1, 2.5)

print(c1.orders())    
print(c1.coffees())   
print(cof1.orders())  
print(cof1.customers())