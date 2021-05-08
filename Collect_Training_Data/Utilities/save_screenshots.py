import cv2 as cv
from time import time
from .file_paths import Paths


def save_screenshots(img, save_to_path, frame_data, loop_time, only_one_button_clicked):
    path = Paths()
    if only_one_button_clicked:
        for i in range(frame_data.start, frame_data.end):
            try:
                cv.imwrite(str(save_to_path) + '/{}.jpg'.format(loop_time), img)
            except Exception as e: 
                print(str(e))
                
            # set loop time for naming files
            loop_time = time()

def x_button_clicked(buttons_clicked, count, loop_time, smash_screenshot):
    if ("X" in buttons_clicked):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count), str(paths.not_in_game) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.not_in_game) + '/{}.jpg'.format(loop_time), smash_screenshot)
        except:
            print("Unable to move file")
        loop_time = time()