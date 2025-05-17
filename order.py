class Order:
    def __init__(self, customer, coffee, price):
        if not (isinstance(price, float) or isinstance(price, int)):
            raise TypeError("Price must be a float or int.")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    
    class Order:
        all_orders = []

        def __init__(self, customer, coffee):
            self.customer = customer
            self.coffee = coffee
            Order.all_orders.append(self)