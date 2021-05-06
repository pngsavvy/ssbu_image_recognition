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
from Character_Tracker import Character_Tracker
from Character_Tracker import Tracker

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

key_word = "Game Capture HD"

windows = get_window_names()
name = [window for window in windows if key_word in window][0]

# initialize the WindowCapture class
wincap = WindowCapture(name)

# load the trained model
neutral_b = cv.CascadeClassifier('cascade_models/neutral_b.xml')
jab = cv.CascadeClassifier('cascade_models/jab.xml')
sheild = cv.CascadeClassifier('cascade_models/sheild2.xml')

count = MoveCounter()
t = TimeTracker()
labels = MoveLabels()
tracker = Character_Tracker()
trac = Tracker()

rectangles = {
    labels.neutral_b: [],
    labels.jab:[],
    labels.shield:[]
}

mario_training_filter = HsvFilter(0, 5, 0, 179, 255, 255, 0, 17, 0 , 0)
vision_jab = Vision('') 

# load an empty Vision class 
vision_limestone = Vision(None)

while(True):

    # get an updated image of the gameq
    smash_screenshot = wincap.get_screenshot()
    output_image = vision_jab.apply_hsv_filter(smash_screenshot, mario_training_filter)

    # do object detection
    rectangles[labels.neutral_b] = neutral_b.detectMultiScale(output_image)
    rectangles[labels.jab]  = jab.detectMultiScale(output_image)
    rectangles[labels.shield]  = sheild.detectMultiScale(output_image)
    
    # tracker.track(output_image)
    trac.track(output_image)

    # draw the detection results onto the original image
    detection_image = vision_limestone.draw_rectangles(output_image, rectangles)
    # detection_image = vision_limestone.draw_rectangles(output_image, jab_loc, neutral_b_loc, sheild_loc)

    # JAB       check if there is a new jab every second
    # if(len(jab_locations) > 0 and time() - t.last_jab > 1):
    #     print("Jab " + str(count.jab))
    #     count.jab += 1
    #     t.last_jab = time()
    
    # # NEUTRAL_B     every 3 seconds
    # if(len(neutral_b_locations) > 0 and time() - t.last_neutral_b > 3):
    #     print("Neutral B " + str(count.neutral_b))
    #     count.neutral_b += 1
    #     t.last_neutral_b = time()

    # # SHEILD     every 3 seconds
    if(len(rectangles['Sheild']) > 0 and time() - t.last_sheild > 1):
        print("Sheild: " + str(count.sheild))
        count.sheild += 1
        t.last_sheild = time()

    # print('FPS {}'.format(1 / (time() - loop_time)))
    t.last_loop = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)
    
    cv.imshow('Matches', detection_image)


print('Done.')
