import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter
from move_counter import MoveCounter
from time_tracker import TimeTracker
from get_window_names import get_window_names
from move_labels import MoveLabels
from tracker import Tracker

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# This can either be a the full title of the window you want to
# screen capture or just a few distinct words that are in the title.
key_word = "Game Capture HD"

# windows = get_window_names()
# window_name = [window for window in windows if key_word in window][0]

try:
    # initialize the WindowCapture class
    # wincap = WindowCapture(window_name)
    cap = cv.VideoCapture('mario.mp4')

    # load the trained models
    neutral_b = cv.CascadeClassifier('cascade_models/cascade_copy.xml')
    jab = cv.CascadeClassifier('cascade_models/jab.xml')
    sheild = cv.CascadeClassifier('cascade_models/sheild.xml')

    count = MoveCounter()
    t = TimeTracker()
    labels = MoveLabels()
    tracker = Tracker()

    # This stores the locations at which images are recognized.
    move_locs = {
        labels.neutral_b: [],
        labels.jab:[],
        labels.shield:[]
    }

    mario_training_filter = HsvFilter(0, 5, 0, 179, 255, 255, 0, 17, 0 , 0)

    # initialize vision class
    vision = Vision('') 

    while(True):

        # get an updated image of the game
        # USE THIS IF YOU ARE USING SCREENCAPTURE
        # smash_screenshot = wincap.get_screenshot()

        # USE THIS IF YOU ARE READING A VIDEO FILE
        ret, smash_screenshot = cap.read()

        # apply filter to img.
        output_image = vision.apply_hsv_filter(smash_screenshot, mario_training_filter)

        move_locs[labels.neutral_b] = neutral_b.detectMultiScale(output_image)
        move_locs[labels.jab]  = jab.detectMultiScale(output_image)
        move_locs[labels.shield]  = sheild.detectMultiScale(output_image)
        
        # select object to track.
        tracker.track(output_image)

        weights = 1
        detection_image = vision.draw_rectangles(output_image, move_locs)

        # JAB       recenter tracker every time a jab is detected
        if(len(move_locs[labels.jab]) > 0 and time() - t.last_jab > 1):
            tracker.reset_tracker(output_image, move_locs[labels.jab])
            count.jab += 1
            t.last_jab = time()
        
        # # NEUTRAL_B     every 3 seconds
        if(len(move_locs[labels.neutral_b]) > 0 and time() - t.last_neutral_b > 3):
            count.neutral_b += 1
            t.last_neutral_b = time()

        # # SHEILD     every 3 seconds
        if(len(move_locs[labels.shield]) > 0 and time() - t.last_sheild > 1):
            count.sheild += 1
            t.last_sheild = time()

        # Press Q to quit
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break

        # fps = 1 / time() - t.last_loop
        # cv.putText(detection_image, str(int(fps)), (75,50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        # t.last_loop = time()

        cv.imshow('Deteciton', detection_image)
except Exception as e: 
    print(str(e))

print("Jab count: ", count.jab)
print("Sheild count: ", count.sheild)
print("Fireball count: ", count.neutral_b)
print('Done.')

