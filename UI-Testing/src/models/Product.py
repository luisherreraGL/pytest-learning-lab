class Product():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __eq__(self, other):
        if (isinstance(other, Product)):
            return self.name == other.name and self.price == other.price
        
        return False