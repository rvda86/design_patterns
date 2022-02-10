import time
from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def get_answer(self):
        pass

class LazyUltimateTruthCalculatorProxy(Calculator):
    def __init__(self):
        self.calculator = None
    
    def get_answer(self):
        if self.calculator is None:
            self.calculator = UltimateTruthCalculator()
        return self.calculator.get_answer() 

class UltimateTruthCalculator(Calculator):
    def __init__(self):
        for _ in range(10):
            time.sleep(1)   
            print("calculating..")
        self.answer = 42

    def get_answer(self):
        return self.answer

calc1 = LazyUltimateTruthCalculatorProxy()

# do some other stuff
time.sleep(5)

print(calc1.get_answer())
print(calc1.get_answer())