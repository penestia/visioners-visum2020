
from distutils.dir_util import copy_tree

'''
Some simple file functions that allows us to manipulate the training data
'''
import os

def copydirectory(inputdirname:str, destinationdirname:str):
    '''
    Make a local copy of the training data so we can play
    with it, and not affect the other teams
    '''

    if not  os.path.exists(inputdirname):
        print (f"{inputdirname} Does not exist")
        return 

    if not os.path.exists(destinationdirname):
        os.makedirs(f"{destinationdirname}")


    copy_tree(inputdirname, destinationdirname)


def filecontents(inputdirname:str)->[]:
    '''
    return full pathname of files in the training directory
    '''

    if not os.path.exists(inputdirname):
        print (f"{inputdirname} Does not exist")
        return []


    returnresults = []
    for r,d,files in os.walk(inputdirname):
        if d:
            continue
        
        for f in files:
            filename = f"{r}/{f}"
            returnresults.append(filename)

    return returnresults



