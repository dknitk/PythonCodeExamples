class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.energy = 1

    def describe(self):
        return f"{self.name} is {self.color}"
    def exercise(self):
        if self.energy >=1:
            print(f"You take {self.name} for a walk")
            self.energy -= 1
        else:
            raise RuntimeError(f"{self.name} is tired. it doesn't want a walk")

    def feed(self):
        print(f"You take {self.name} to eat")
        self.energy += 1
our_dog = Dog("Bruno", "brown")
try:
    print(f"Dog name is {our_dog.name}")
    print(f"Dog color is {our_dog.color}")
    print(our_dog.describe())
    print(our_dog.energy)
    our_dog.exercise()
    print(our_dog.energy)
    our_dog.exercise()
    print(our_dog.energy)
    our_dog.feed()
    print(our_dog.energy)
except RuntimeError as e :
    print(f"Something went wrong trying to exercise the dog {e}")

