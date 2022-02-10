from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class ConcreteObserver1(Observer):

    data = {}

    def update(self, data):
        print(f'OBSERVER 1: my old data: {self.data}')
        self.data = data
        print(f'OBSERVER 1: my new data: {self.data}')

class ConcreteObserver2(Observer):

    data = {}

    def update(self, data):
        print(f'OBSERVER 2: my old data: {self.data}')
        self.data = data
        print(f'OBSERVER 2: my new data: {self.data}')

class ConcreteObserver3(Observer):

    data = {}

    def update(self, data):
        print(f'OBSERVER 3: my old data: {self.data}')
        self.data = data
        print(f'OBSERVER 3: my new data: {self.data}')

class Observable(ABC):
    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def unregister(self, observer: Observer):
        pass

class ConcreteObservable(Observable):
    
    observers = []
    data = {}

    def notify(self):
        for observer in self.observers:
            observer.update(self.get_state())

    def register(self, observer: Observer):
        self.observers.append(observer)

    def unregister(self, observer: Observer):
        self.observers = [obs for obs in self.observers if obs != observer]

    def get_state(self):
        return self.data

    def set_state(self, data):
        self.data = data

observable = ConcreteObservable()
observer1 = ConcreteObserver1()
observer2 = ConcreteObserver2()
observer3 = ConcreteObserver3()
observable.register(observer1)
observable.register(observer2)
observable.register(observer3)

observable.set_state({"name": "John", "age": 45, "profession": "mechanic", "country": "Belgium"})
observable.notify()

observable.unregister(observer2)
observable.set_state({"pet": "cat", "name": "lucy", "age": 4})
observable.notify()
