import time
import cv2 as cv,cv2
import numpy as np
import os

SCALE = 100

class ImageLoader:
    def __init__(self):
        self.frames_names = sorted(os.listdir("c6s1/frames"))     
        self.img_list = self.load_images()

    def load_images(self):
        img_list = []       
        for file in self.frames_names:
            if file.endswith(".jpg"):
                img_color = cv.imread("c6s1/frames/" + file)
                img_list.append((file, img_color))
        return img_list
    
    def resize(self, image = None):
        width = int(image.shape[1] * SCALE / 100)
        height = int(image.shape[0] * SCALE / 100)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


    def drawBB(self, tup_img):
        img = tup_img[1]
        img_name = tup_img[0]
        with open(f"c6s1/bboxes.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                idx = lines.index(line)+1
                if img_name in line and lines[idx].replace("\n","").isdigit():
                    for i in range(int(lines[idx])):
                        coords = lines[idx+i+1].split()
                        cv.rectangle(img, (int(float(coords[0])), int(float(coords[1]))), (int(float(coords[0]))+int(float(coords[2])),int(float(coords[1]))+int(float(coords[3]))), (0, 255, 0), 2)
        return img


    def get_image(self, image_num):
        img_color = self.img_list[image_num]
        img_to_display = self.drawBB(img_color)
        print(img_color[0])
        resized = self.resize(image=img_to_display)
        return resized

    def get_bbox(self):
        pass