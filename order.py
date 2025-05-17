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
            self.price = price

        @classmethod
        def count_for_coffee(cls, coffee):
            return sum(1 for order in cls.all_orders if order.coffee == coffee)
        
        @classmethod
        def average_price_for_coffee(cls, coffee):
            prices = [order.price for order in cls.all_orders if order.coffee == coffee]
            if not prices:
                return 0
            return sum(prices) / len(prices)