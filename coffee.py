

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise TypeError("name must be a string of three or more characters")

    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
    # coffee.py

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if orders:
            return sum(order.price for order in orders) / len(orders)
        return 0.0
    

    
