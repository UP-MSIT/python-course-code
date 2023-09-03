class Parent:
    def __init__(self, x):
        self.x = x


class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


c = Child(1, 2)

print(c.x)
print(c.y)
