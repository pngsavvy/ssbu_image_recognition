from .moveset import Moveset

class Character:
    name = ""
    moveset = Moveset()

    def __init__(self, moveset):
        self.moveset = moveset
        self.name = moveset.character_name

    def jab(self):
        return self.moveset.jab
    def grab(self):
        return self.moveset.grab
    def sheild(self):
        return self.moveset.sheild
    def jump(self):
        return self.moveset.jump

    def down_smash(self):
        return self.moveset.down_smash
    def up_smash(self):
        return self.moveset.up_smash
    def right_smash(self):
        return self.moveset.right_smash
    def left_smash(self):
        return self.moveset.left_smash

    def down_tilt(self):
        return self.moveset.down_tilt
    def up_tilt(self):
        return self.moveset.up_tilt
    def right_tilt(self):
        return self.moveset.right_tilt
    def left_tilt(self):
        return self.moveset.left_tilt
    
    def down_smash(self):
        return self.moveset.down_smash
    def up_smash(self):
        return self.moveset.up_smash
    def right_smash(self):
        return self.moveset.right_smash
    def left_smash(self):
        return self.moveset.left_smash

    def down_special(self):
        return self.moveset.down_special
    def up_special(self):
        return self.moveset.up_special
    def right_special(self):
        return self.moveset.right_special
    def left_special(self):
        return self.moveset.left_special
    def neutral_special(self):
        return self.moveset.neutral_special