import os
from file_paths import Paths

# reads all the files in the specified folders and generates a text file with all the negative images from them.

path = Paths()

def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('jab_neg.txt', 'w') as f:
        # loop over all the filenames
        # for filename in os.listdir(path.jab):
        #     f.write(str(path.jab) + '/' +  filename + '\n')

        for filename in os.listdir(path.sheild):
            f.write(str(path.grab) + '/' +  filename + '\n')

        for filename in os.listdir(path.neutral_special):
            f.write(str(path.neutral_special) + '/' +  filename + '\n')

        for filename in os.listdir(path.jump):
            f.write(str(path.jump) + '/' +  filename + '\n')

generate_negative_description_file()
