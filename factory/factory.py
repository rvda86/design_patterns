from abc import ABC, abstractmethod
import random

class Animal(ABC):
    def __init__(self):
        pass

class Lion(Animal):
    def __init__(self):
        pass

class Monkey(Animal):
    def __init__(self):
        pass

class Elephant(Animal):
    def __init__(self):
        pass

class Penguin(Animal):
    def __init__(self):
        pass

class AnimalFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_animal(self, animal_count):
        pass

class RandomAnimalFactory(AnimalFactory):
    def create_animal(self, animal_count):
        animals = [Lion(), Monkey(), Elephant(), Penguin()]
        animal = random.choice(animals)
        return animal

class BalancedAnimalFactory(AnimalFactory):
    def create_animal(self, animal_count):
        animals = {'Elephant': Elephant(), 'Lion': Lion(), 'Monkey': Monkey(), 'Penguin': Penguin()}
        animal = animals[min(animal_count, key=animal_count.get)]
        return animal

class Zoo:
    def __init__(self):
        self.animals = []
        self.animal_count = {'Elephant': 0, 'Lion': 0, 'Monkey': 0, 'Penguin': 0}

    def addAnimals(self, factory, amount):
        for _ in range(amount):
            animal = factory.create_animal(self.animal_count)
            self.animals.append(animal)
            self.animal_count[type(animal).__name__] += 1

zoo = Zoo()
random_factory = RandomAnimalFactory()
zoo.addAnimals(random_factory, 100)
print(zoo.animal_count)

balanced_factory = BalancedAnimalFactory()
zoo.addAnimals(balanced_factory, 100)
print(zoo.animal_count)

zoo2 = Zoo()
balanced_factory = BalancedAnimalFactory()
zoo2.addAnimals(balanced_factory, 100)
print(zoo2.animal_count)