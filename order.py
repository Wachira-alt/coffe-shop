from customer import Customer
from coffee import Coffee

class Order:
    
    orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
         self._customer = value
        else:
            raise TypeError ("customer must be a customer instance")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if isinstance (value, Coffee):
            self._coffee = value
        else:
            raise TypeError("coffee must be a Coffee instance")
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise TypeError("price must be a float between 1.0 and 10.0")
    

    
