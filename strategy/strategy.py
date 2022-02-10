from abc import ABC, abstractmethod
import random

class IFoodAcquiringBehavior(ABC):
    @abstractmethod
    def acquiring_food(self):
        pass

class FisherStategy(IFoodAcquiringBehavior):    
    def acquiring_food(self):
        print("I am now fishing")

class HunterStrategy(IFoodAcquiringBehavior):
    def acquiring_food(self):
        print("I am now hunting")

class ForagerStrategy(IFoodAcquiringBehavior):
    def acquiring_food(self):
        print("I am now foraging")

class FarmerStrategy(IFoodAcquiringBehavior):
    def acquiring_food(self):
        print("I am now farmer")


class IMiningBehavior(ABC):
    @abstractmethod
    def mining(self):
        pass

class GoldMinerStrategy(IMiningBehavior):
    def mining(self):
        print("I am now working in the gold mine")

class IronMinerStrategy(IMiningBehavior):
    def mining(self):
        print("I am now working in the iron mine")

class CopperMinerStrategy(IMiningBehavior):
    def mining(self):
        print("I am now working in the copper mine")


class IEntertainerBehavior(ABC):
    @abstractmethod
    def entertaining(self):
        pass

class SingerStrategy(IEntertainerBehavior):
    def entertaining(self):
        print("I am now singing for you")

class JugglerStrategy(IEntertainerBehavior):
    def entertaining(self):
        print("I am now juggling for you")


class Character: 

    food_strategy: IFoodAcquiringBehavior
    mining_strategy: IMiningBehavior
    entertaining_strategy: IEntertainerBehavior

    def __init__(self, food_strategy: IFoodAcquiringBehavior, mining_strategy: IMiningBehavior, entertaining_strategy: IEntertainerBehavior):
        self.food_strategy = food_strategy()
        self.mining_strategy = mining_strategy()
        self.entertaining_strategy = entertaining_strategy()

    @staticmethod
    def IJuggleWithGoldplatedFish():
        return Character(FisherStategy, GoldMinerStrategy, JugglerStrategy)

    @staticmethod
    def IAmSoRandom():
        food_strategies = [FisherStategy, HunterStrategy, ForagerStrategy, FarmerStrategy]
        mining_strategies = [GoldMinerStrategy, IronMinerStrategy, CopperMinerStrategy]
        entertaining_strategies = [SingerStrategy, JugglerStrategy]
        return Character(random.choice(food_strategies), random.choice(mining_strategies), random.choice(entertaining_strategies))

    def acquiring_food(self):
        return self.food_strategy.acquiring_food()
    
    def mining(self):
        return self.mining_strategy.mining()

    def entertaining(self):
        return self.entertaining_strategy.entertaining()

iron_fisherman_juggler = Character(FisherStategy, IronMinerStrategy, JugglerStrategy)
iron_fisherman_juggler.acquiring_food()

random_character = Character.IAmSoRandom()
random_character.acquiring_food()
random_character.mining()
random_character.entertaining()

weird_dude = Character.IJuggleWithGoldplatedFish()
weird_dude.acquiring_food()
weird_dude.mining()
weird_dude.entertaining()

