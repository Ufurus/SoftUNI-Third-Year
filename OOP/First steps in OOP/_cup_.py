class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
    def fill(self, needed_quantity):
        if needed_quantity <= self.size - self.quantity:
            self.quantity += needed_quantity
    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())