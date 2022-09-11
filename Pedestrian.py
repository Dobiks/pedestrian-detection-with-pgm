import cv2
import numpy as np
from matplotlib import pyplot as plt


class Pedestrian:
    def __init__(self, frame, coords, id: int) -> None:
        self.image = self.__create_image(frame, coords)
        self.histograms = self.__create_histograms()
        self.id = str(id)

    def __create_image(self, frame, coords) -> np.ndarray:
        # Create image from coordinates
        x = int(float(coords[0]))
        y = int(float(coords[1]))
        w = int(float(coords[2]))
        h = int(float(coords[3]))
        return frame[y:y+h, x:x+w]

    def __create_histograms(self) -> list:
        # Create histograms for each channel
        channels = cv2.split(self.image)
        channels += cv2.split(cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV))
        histograms = []
        for channel in channels:
            histograms.append(cv2.calcHist(
                [channel], [0], None, [256], [0, 256]))
        return histograms

    def get_image(self) -> np.ndarray:
        return self.image

    def get_histograms(self) -> list:
        return self.histograms

    def get_id(self) -> int:
        return self.id