import numpy as np
import cv2
import os

MAIN_DIR = os.path.abspath('../stage1_test')
IDS = os.listdir(MAIN_DIR)
print(IDS[0])
print(MAIN_DIR)

IMAGES_ABSPATH = [os.path.join(MAIN_DIR, id, 'images', id+'.png') for id in IDS]
print(IMAGES_ABSPATH[0])

IMAGES_WRITTEN = 'IMAGE_WRITTEN'


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Color', frame)
    cv2.imshow('GRAY', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


