class Cat:
    def sound(self):
        print("Meo meo")

class Dog:
    def sound(self):
        print("Gâu gâu")

animals = [Cat(), Dog()]
for a in animals:
    a.sound()