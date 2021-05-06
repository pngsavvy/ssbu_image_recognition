from .frames import Frames
from .moveset import Moveset

class FrameData:
    mario = Moveset()

    mario.character_name = "Mario"
    mario.jab = Frames(1,3)
    mario.grab = Frames(6,11)
    mario.jump = Frames(1,5)

    mario.right_tilt = Frames(5,7)
    mario.left_tilt = Frames(5,7)
    mario.up_tilt = Frames(5, 11)
    mario.down_tilt = Frames(5,7)

    mario.dash_attack = Frames(6, 15)
    mario.right_smash = Frames(15,17)
    mario.left_smash = Frames(15,17)
    mario.up_smash = Frames(9,12)
    mario.down_smash = Frames(5,10)

    mario.neutral_special = Frames(10, 21)
    mario.right_special = Frames(12, 14)
    mario.left_special = Frames(12, 14)
    mario.up_special = Frames(3,18)
    mario.down_special = Frames(21, 30)



