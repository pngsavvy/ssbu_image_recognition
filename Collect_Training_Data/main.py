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
from Utilities import save_screenshots
from Character import Character
from Character import FrameData

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize classes
try:
    gc_capture = WindowCapture('ViewWindow')
    smash_capture = WindowCapture('Game Capture HD')
except Exception as e: 
    print(str(e))
    
paths = Paths()
gc_reader = InputReader()
frame_data = FrameData()
mario = Character(frame_data.mario)
vision = Vision('Screenshots\\my_image.jpg') 

loop_time = time()
fps_loop_time = time()

while(True):
    # get an updated image of the game and controler
    gc_screenshot = gc_capture.get_screenshot()
    smash_screenshot = smash_capture.get_screenshot()
    output_image = vision.apply_hsv_filter(smash_screenshot, mario_training_filter)

    # use image recognition to detect what buttons are being pressed
    gc_reader.set_clicks(gc_screenshot)
    buttons_clicked = gc_reader.buttons_clicked()

    # if there are any buttons clicked then add them to the button log
    if len(buttons_clicked) > 0:
        print("Pressed: ", buttons_clicked)

    only_one_button_clicked = gc_reader.only_one_button_clicked()

    # JAB
    if ("B" in buttons_clicked):
        save_screenshots(output_image, paths.jab, mario.jab(), loop_time, only_one_button_clicked)

    # GRAB
    if ("A" in buttons_clicked):
        save_screenshots(output_image, paths.grab, mario.grab(), loop_time, only_one_button_clicked)

    # NEUTRAL_B 
    if ("L" in buttons_clicked):
        save_screenshots(output_image, paths.neutral_special, mario.neutral_special(), loop_time, only_one_button_clicked)
       
    # JUMP
    if ("Z" in buttons_clicked):
        save_screenshots(output_image, paths.jump, mario.jump(), loop_time, only_one_button_clicked)
    
    # SHIELD
    if ("R" in buttons_clicked and gc_reader.only_one_button_clicked()):
        save_screenshots(output_image, paths.sheild, mario.sheild(), loop_time, only_one_button_clicked)

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - fps_loop_time)))
    # fps_loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
