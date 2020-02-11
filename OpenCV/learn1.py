import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import random

IMAGE_FOLDER = os.path.join(os.getcwd(), 'stage1_test')
#IDS = next(os.walk('../stage1_test'))[1]
MAIN_DIR = os.path.abspath('../stage1_test')
IDS = os.listdir('../stage1_test')
IMAGES_ABSPATH = [os.path.join(MAIN_DIR, id, 'images', id+'.png') for id in IDS]

image = cv2.imread(random.choice(IMAGES_ABSPATH), 1)
cv2.imshow('Window', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
  