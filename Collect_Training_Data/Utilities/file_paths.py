from pathlib import Path

class Paths:

    screenshots = Path('Screenshots')
    catch = screenshots / 'Catch'

    no_mario = screenshots / 'Negative_Mario'
    not_in_game = screenshots / 'Not_In_Game'
    in_game = screenshots / 'In_Game'
    
    attacks = screenshots / 'Attacks'
    specials = screenshots / 'Specials'
    sheild = screenshots / 'Shield'
    jump = screenshots / 'Jump'
    grab = screenshots / 'Grab'

    smashes = attacks / 'Smashes'
    tilts = attacks / 'Tilts'

    jab = attacks / 'Jab'

    right_smash = smashes / 'Right_Smash'
    left_smash = smashes / 'Left_Smash'
    down_smash = smashes / 'Down_Smash'
    up_smash = smashes / 'Up_Smash'

    right_tilt = tilts / 'Right_Tilt'
    left_tilt = tilts / 'Left_Tilt'
    up_tilt = tilts / 'Up_Tilt'
    down_tilt = tilts / 'Down_Tilt'

    down_special = specials / 'Down_Special'
    left_special = specials / 'Left_Special'
    right_special = specials / 'Right_Special'
    up_special = specials / 'Up_Special'
    neutral_special = specials / 'Neutral_Special'
