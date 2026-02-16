import random
import os
import sys
from characters import list_jss

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIRECTORY)

def return_img_character(file_name):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    return os.path.join(base_path, 'assets', file_name)

def return_random_character():
    select = random.choice(list_jss)
    select["real_url"] = return_img_character(select['img'])
    return select