from time import time

class TimeTracker:
    last_loop = None
    last_jab = None
    last_neutral_b = None
    last_sheild = None

    def __init__(self):
        self.last_loop = time()
        self.last_neutral_b = time()
        self.last_jab = time()
        self.last_sheild = time()

    # def last_loop(self):
    #     return self.last_loop
    
    # def last_jab(self):
    #     return self.last_jab

    # def last_neutral_b(self):
    #     return self.last_neutral_b
