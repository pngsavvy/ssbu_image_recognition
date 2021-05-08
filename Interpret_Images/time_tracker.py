from time import time

# These are used to keep track of FPS as well as how long it has been since a certain move has been recognized. 
# This way it does not count the same move too many times. 

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
