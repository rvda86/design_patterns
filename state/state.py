from abc import ABC, abstractmethod
import time

class State(ABC):

    def __init__(self, telephone):
        self.telephone = telephone

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

    def call(self):
        print("already in a call..")

    def hang_up(self):
        print("ok.. hanging up..")
        self.telephone.set_state(Listening(self.telephone))

    def call_answered(self):
        print("?? already in a call..")

class Listening(State):

    def call(self):
        for _ in range(10):
            time.sleep(1)
            print("calling..")
        self.telephone.set_state(Connecting(self.telephone))

    def hang_up(self):
        print("?? you never picked me up")

    def call_answered(self):
        print("?? but you didn't call anybody..")

class Connecting(State):

    def call(self):
        print("already trying to call..")

    def hang_up(self):
        print("ok.. hanging up..")
        self.telephone.set_state(Listening(self.telephone))

    def call_answered(self):
        print("hooray, someone answered.. call established!")
        self.telephone.set_state(Connected(self.telephone))

class Telephone:

    def __init__(self):
        self.set_state(Listening(self))

    def set_state(self, state: State):
        self.state = state

    def call(self):
        self.state.call()

    def hang_up(self):
        self.state.hang_up()

    def call_answered(self):
        self.state.call_answered()


my_phone = Telephone()
my_phone.hang_up()
my_phone.call()
my_phone.call_answered()
my_phone.call()
my_phone.call_answered()
my_phone.hang_up()