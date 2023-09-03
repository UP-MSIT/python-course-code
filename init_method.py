
class People:
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

    def set_age(self, age):
        self.age = age


p1 = People("name", "location", 43)
print(p1.name)
print(p1.location)
print(p1.age)
