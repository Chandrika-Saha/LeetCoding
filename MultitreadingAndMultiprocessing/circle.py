class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
       return self._radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError("No negatives")

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(20)
print(f"The circle radius: {c.radius}")
print(f"The circle diameter: {c.diameter}")
c.radius = 33
print(f"Circle radius now: {c.radius}")
c.radius = -34

