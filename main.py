import numpy as np
from ImageLoader import ImageLoader
import time
import cv2
from Pedestrian import Pedestrian

DEBUG = False


def define_pedestrians(frame, coords):
    pedestrians = []
    for coord in coords:
        pedestrians.append(Pedestrian(frame, coord))
    return pedestrians


if __name__ == "__main__":
    loader = ImageLoader()
    img_num = 0
    previous_pedestrians = None
    ctr = 0
    while True: #do zmiany
        ctr += 1
        org_img, bbox_img, coords = loader.get_data(img_num)
        pedestrians = define_pedestrians(org_img, coords)
        time.sleep(.01)
        img_num += 1
        previous_pedestrians = pedestrians