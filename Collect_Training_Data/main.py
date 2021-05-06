import cv2 as cv
import numpy as np
import os
import shutil
from time import time

from Utilities import WindowCapture
from Utilities import Paths
from Utilities import InputReader
from Utilities import Vision
from Utilities import x_button_clicked
from Utilities import hsvfilter
from Utilities import mario_training_filter

from Character import Character
from Character import FrameData

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize classes
try:
    gc_capture = WindowCapture('ViewWindow')
    smash_capture = WindowCapture('Game Capture HD')
except:
    print("can't find window")
    
paths = Paths()
gc_reader = InputReader()

frame_data = FrameData()
mario = Character(frame_data.mario)

vision_jab = Vision('Screenshots\\my_image.jpg') 

loop_time = time()
fps_loop_time = time()
count = 0
lag = 1

#use this to see if they just jumped
button_log = []
while(True):
    # get an updated image of the game and controler
    gc_screenshot = gc_capture.get_screenshot()
    smash_screenshot = smash_capture.get_screenshot()
    output_image = vision_jab.apply_hsv_filter(smash_screenshot, mario_training_filter)

    # display the processed image
    # cv.imshow('Matches', gc_screenshot)

    cv.imwrite(str(paths.catch) + '/{}.jpg'.format(count), output_image)
    
    gc_reader.set_clicks(gc_screenshot)
    buttons_clicked = gc_reader.buttons_clicked()
    if len(buttons_clicked) > 0:
        button_log += buttons_clicked

    # TRAIN MARIO TRACKER 
    # if (len(buttons_clicked) > 0):
    #     try:
    #         shutil.move(str(paths.catch) + '/{}.jpg'.format(count), str(paths.no_mario) + '/{}.jpg'.format(loop_time))
    #         cv.imwrite(str(paths.no_mario) + '/{}.jpg'.format(loop_time), smash_screenshot)
    #     except:
    #         print("Unable to move file")
    #     loop_time = time()

    x_button_clicked(buttons_clicked, count, loop_time, smash_screenshot)

    # ----------------------------------------------------------------
    # Attacks
    if ("B" in buttons_clicked):
        # print(button_log)

        # Jab
        if (gc_reader.only_one_button_clicked()):
            first = True
            for i in range( count - mario.jab().end, count - mario.jab().start):
                try:
                    # move from catch to jab folder
                    shutil.move(str(paths.catch) + '/{}.jpg'.format(i), str(paths.jab) + '/{}.jpg'.format(loop_time))
                    # print("moved " + str(count))
                    # I don't know if i need this 
                    cv.imwrite(str(paths.jab) + '/{}.jpg'.format(loop_time), output_image)

                except:
                    pass
                    # print("Unable to move file")
                loop_time = time()
    
    # Grab
    if ("A" in buttons_clicked):
        if (gc_reader.only_one_button_clicked()):
            for i in range(count - mario.grab().end + lag, count - mario.grab().start + lag):
                try:
                    # move from catch to jab folder
                    shutil.move(str(paths.catch) + '/{}.jpg'.format(i), str(paths.grab) + '/{}.jpg'.format(loop_time))
                    # I don't know if i need this 
                    cv.imwrite(str(paths.grab) + '/{}.jpg'.format(loop_time), output_image)
                except:
                    print("Unable to move file")
                loop_time = time()

    # ----------------------------------------------------------------
    # Specials
    if ("L" in buttons_clicked):
        
        # Neutral Special
        if (gc_reader.only_one_button_clicked()):
            for i in range(count - mario.neutral_special().end + 10, count - mario.neutral_special().start + 5):
                try:
                    shutil.move(str(paths.catch) + '/{}.jpg'.format(i), str(paths.neutral_special) + '/{}.jpg'.format(loop_time))
                    cv.imwrite(str(paths.neutral_special) + '/{}.jpg'.format(loop_time), output_image)
                except:
                    print("Unable to move file")
                loop_time = time()
    
    # ----------------------------------------------------------------
    # Jump
    if ("Z" in buttons_clicked):
        for i in range(count + mario.jump().start + lag, count + mario.jump().end + lag):
            try:
                shutil.move(str(paths.catch) + '/{}.jpg'.format(i), str(paths.jump) + '/{}.jpg'.format(loop_time))
                cv.imwrite(str(paths.jump) + '/{}.jpg'.format(loop_time), output_image)
            except:
                print("Unable to move file")
            loop_time = time()
    
    # ----------------------------------------------------------------
    # Sheild
    if ("R" in buttons_clicked and gc_reader.only_one_button_clicked()):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count - lag), str(paths.sheild) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.sheild) + '/{}.jpg'.format(loop_time), output_image)
        except:
            print("Unable to move file")
        loop_time = time()
    count += 1

    # ----------------------------------------------------------------
    # C STICK
    if ("C_Right" in buttons_clicked and gc_reader.only_one_button_clicked()):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count - lag), str(paths.right_smash) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.right_smash) + '/{}.jpg'.format(loop_time), output_image)
        except:
            print("Unable to move file")
        loop_time = time()
    count += 1

    if ("C_Left" in buttons_clicked and gc_reader.only_one_button_clicked()):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count - lag), str(paths.left_smash) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.left_smash) + '/{}.jpg'.format(loop_time), output_image)
        except:
            print("Unable to move file")
        loop_time = time()
    count += 1

    if ("C_Up" in buttons_clicked and gc_reader.only_one_button_clicked()):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count - lag), str(paths.up_smash) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.up_smash) + '/{}.jpg'.format(loop_time), output_image)
        except:
            print("Unable to move file")
        loop_time = time()
    count += 1

    if ("C_Down" in buttons_clicked and gc_reader.only_one_button_clicked()):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count - lag), str(paths.down_smash) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.down_smash) + '/{}.jpg'.format(loop_time), output_image)
        except:
            print("Unable to move file")
        loop_time = time()
    count += 1

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - fps_loop_time)))
    fps_loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positdddive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('d'):
        cv.imwrite('{}.jpg'.format(loop_time), output_image)

print('Done.')
