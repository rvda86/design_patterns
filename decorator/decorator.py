from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def get_speed(self):
        pass

class CharacterA(Character):
    
    speed = 5

    def __init__(self):
        pass

    def walk(self):
        print(f"I am walking at speed {self.speed}")

    def fly(self):
        return print("sorry, I cannot fly")

    def get_speed(self):
        return self.speed

class Decorator(Character):

    character = Character

    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def get_speed(self):
        pass

class Walk2XSpeedDecorator(Decorator):

    def walk(self):
        print(f"I am walking at speed {self.get_speed()}")

    def fly(self):
        return self.character.fly()

    def get_speed(self):
        return self.character.get_speed() * 2

class CanFlyDecorator(Decorator):

    def walk(self):
        print(f"I am walking at speed {self.get_speed()}")

    def fly(self):
        return print("weee.. I am flying")

    def get_speed(self):
        return self.character.get_speed()

character1 = CharacterA()
character1.walk()
character1.fly()

character1_fast = Walk2XSpeedDecorator(character1)
character1_fast.walk()

character1_faster = Walk2XSpeedDecorator(character1_fast)
character1_faster.walk()

character1_flyer = CanFlyDecorator(character1)
character1_flyer.fly()

character1_flyer_fast_walker = Walk2XSpeedDecorator(character1_flyer)
character1_flyer_fast_walker.fly()
character1_flyer_fast_walker.walk()