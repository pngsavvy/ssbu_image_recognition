
def save_screenshots(save_to_path, move_from, frame_data):
    for i in range(count + frame_data.start + lag, count + frame_data.end + lag):
        try:
            # move from catch to jab folder
            shutil.move(str(move_from) + '/{}.jpg'.format(i), str(paths.jab) + '/{}.jpg'.format(loop_time))
            # I don't know if i need this 
            cv.imwrite(str(save_to_path) + '/{}.jpg'.format(loop_time), smash_screenshot)
        except:
            print("Unable to move file")
        loop_time = time()

def x_button_clicked(buttons_clicked, count, loop_time, smash_screenshot):
    if ("X" in buttons_clicked):
        try:
            shutil.move(str(paths.catch) + '/{}.jpg'.format(count), str(paths.not_in_game) + '/{}.jpg'.format(loop_time))
            cv.imwrite(str(paths.not_in_game) + '/{}.jpg'.format(loop_time), smash_screenshot)
        except:
            print("Unable to move file")
        loop_time = time()