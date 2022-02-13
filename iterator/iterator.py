from abc import ABC, abstractmethod

class IteratorOutOfBounds(Exception):
    pass

class Aggregate(ABC):
    @abstractmethod
    def get_iterator():
        pass

class StringList(Aggregate):

    def __init__(self, string):
        self.list = list(string)

    def get_iterator(self):
        return ListIterator(self)

class Iterator(ABC):

    @abstractmethod
    def is_done():
        pass
    
    @abstractmethod
    def first():
        pass

    @abstractmethod
    def next():
        pass
    
    @abstractmethod
    def current():
        pass

class ListIterator(Iterator):

    def __init__(self, string_list: StringList):
        self.list = string_list.list
        self.index = 0

    def is_done(self):
        return self.index == len(self.list)

    def first(self):
        self.index = 0

    def next(self):
        self.index += 1

    def current(self):
        if self.is_done():
            raise IteratorOutOfBounds
        return self.list[self.index]

list = StringList('abcde')
iterator = list.get_iterator()
print(iterator.current())
iterator.next()
print(iterator.current())
iterator.next()
print(iterator.current())
iterator.next()
print(iterator.current())
iterator.next()
print(iterator.current())
iterator.first()
print(iterator.current())
iterator.next()
iterator.next()
iterator.next()
iterator.next()
iterator.next()
print(iterator.current())