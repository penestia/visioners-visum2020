'''
This is a set of functions that manipulate the training data. The functions will
include injecting noise, balancing and so on
'''

import sys
import os
sys.path.append("lib")
from fileutils import copydirectory
from fileutils import filecontents
from imgaug import augmenters as iaa
import random
import imageio
import imgaug as ia


'''
Step One - Make a local copy of the data. Master is back-up
If we mess up. Recover just delete data directory and run this script
'''

INPUTDIR:str = "/home/master/dataset/train"
OUTPUTDIR:str = "data"

if not os.path.exists(OUTPUTDIR):
    copydirectory(INPUTDIR, OUTPUTDIR)


def rotate():
    '''
    This function reads through the data directory and rotates the
    files by a given degree and resaves the image with a .r.jpg
    extension so we know which ones have been altered.
    The image will be rotated in a random way from 1 to 180 and
    -1 to -180. This it to try to get a variety of images - not
    just rotated all the same
    '''

    def returnnewname(location:str, middlename:str):
        '''
        Helper function which splits a filename to put
        a identifier in the middle. Perhaps move to fileutils
        if this proves popular
        '''

        #Assume has a dot in the filename
        SPLITTER:str = "."
        if SPLITTER not in location:
            return location
        parts:[] = location.split(SPLITTER)
        location = "f{parts[0]}{SPLITTER}R{SPLITTER}parts[-1]"
        return location

    filenames:[] = filecontents(INPUTDIR)
    if not filenames:
        return

    FILEREADER:str = "imageio:"

    imagecontents =[imageio.imread(img) for img in filenames]
    ia.seed(4)

    MAXROTATE:int = 180
    MINROTATE:int = 1

    returnresults ={}
    for counter,image in enumerate(imagecontents):
        degree = random.randint(MINROTATE, MAXROTATE)
        rotate = iaa.Affine(rotate=(-degree, degree))
        image_aug = rotate(image=image)
        outputname = returnnewname(filenames[counter],"R")
        returnresults[outputname] = image_aug
    return returnresults

newimages = rotate()


