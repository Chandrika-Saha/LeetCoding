from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_cost(self):
        return self.price * self.quantity

p1 = Product("Laptop", 123.23, 4)
p2 = Product("Mango", 2.2, 7)
p3 = Product("Lalal", 4.2, 9)

print(p1)
print(p1.total_cost())
print(p1 == p2)
print(p1 == p1)
print(p2)
print(p3)