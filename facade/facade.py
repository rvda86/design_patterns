class Facade: 

    def do_something(self):
        d = D()
        b = B()
        c = C(d)
        a = A(b, c)
        a.prepare()
        a.perform_action()

class D:
    def perform_action(self):
        print("something has been done")

class C: 
    def __init__(self, d: D):
        self.d = d
        self.ready = False

    def prepare(self):
        self.ready = True

    def is_ready(self):
        return self.ready

    def perform_action(self):
        self.d.perform_action()

class B: 
    def __init__(self):
        self.ready = False

    def prepare(self):
        self.ready = True

    def is_ready(self):
        return self.ready

class A:
    def __init__(self, b: B, c: C):
        self.b = b
        self.c = c

    def prepare(self):
        self.b.prepare()
        self.c.prepare()

    def perform_action(self):
        if self.b.is_ready() and self.c.is_ready():
            self.c.perform_action()


facade = Facade()
facade.do_something()