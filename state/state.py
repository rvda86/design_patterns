from abc import ABC, abstractmethod
import time

class State(ABC):
    @abstractmethod
    def call():
        pass

    @abstractmethod
    def hang_up():
        pass

    @abstractmethod
    def call_answered():
        pass

class Connected(State):
    
    def call(self, telephone):
        print("already in a call..")

    def hang_up(self, telephone):
        print("ok.. hanging up..")
        telephone.set_state(Listening())

    def call_answered(self, telephone):
        print("?? already in a call..")

class Listening(State):

    def call(self, telephone):
        for _ in range(10):
            time.sleep(1)
            print("calling..")
        telephone.set_state(Connecting())

    def hang_up(self, telephone):
        print("?? you never picked me up")

    def call_answered(self, telephone):
        print("?? but you didn't call anybody..")

class Connecting(State):

    def call(self, telephone):
        print("already trying to call..")

    def hang_up(self, telephone):
        print("ok.. hanging up..")
        telephone.set_state(Listening())

    def call_answered(self, telephone):
        print("hooray, someone answered.. call established!")
        telephone.set_state(Connected())

class Telephone:

    def __init__(self):
        self.set_state(Listening())

    def set_state(self, state: State):
        self.state = state

    def call(self):
        self.state.call(self)

    def hang_up(self):
        self.state.hang_up(self)

    def call_answered(self):
        self.state.call_answered(self)


my_phone = Telephone()
my_phone.hang_up()
my_phone.call()
my_phone.call_answered()
my_phone.call()
my_phone.call_answered()
my_phone.hang_up()