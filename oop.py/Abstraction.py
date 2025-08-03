# Abstraction - Hiding the implementation details of a class and only showing the essantial fearture to user.
class car:
    def _init__(self):
        self.acceletor = False
        self.brk = False
        self.cluch = False
    def start(self):
        self.cluch = True
        self.acceletor = True
        print("car started..")
car1 = car()
car1.start()