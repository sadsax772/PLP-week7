# Parent class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Child classes with unique move() implementations
class Dog(Animal):
    def move(self):
        return "Running on four legs 🐕💨"

class Bird(Animal):
    def move(self):
        return "Flying through the sky 🐦✨"

class Snake(Animal):
    def move(self):
        return "Slithering silently 🐍🌿"

class Kangaroo(Animal):
    def move(self):
        return "Hopping across the field 🦘🌾"

# Create a list of animals
animals = [Dog(), Bird(), Snake(), Kangaroo()]

# Loop through them and call move()
for animal in animals:
    print(animal.move())
