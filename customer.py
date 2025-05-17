class Customer:
    def __init__(self, name):
        self.name = name
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

    def __str__(self):
        return f"Customer: {self.name}"   

customer = Customer("John Doe")   
print(customer)     
@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    if not isinstance(value, str):
        raise TypeError("Name must be a string")
    if not (1 <= len(value) <= 15):
        raise ValueError("Name must be 1-15 characters long")
    self._name = value

class Order:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        self._customer = customer

    @property
    def customer(self):
        return self._customer

    @classmethod
    def most_aficionado(cls, coffee):
        orders = [order for order in getattr(Order, "all", []) if getattr(order, "coffee", None) == coffee]
        if not orders:
            return None
        spending = {}
        for order in orders:
            customer = order.customer
            price = getattr(order, "price", 0)
            spending[customer] = spending.get(customer, 0) + price
        if not spending:
            return None
        return max(spending, key=spending.get)