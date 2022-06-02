from ImageLoader import ImageLoader
from PedastrianTracker import PedastrianTracker
import time
import cv2 as cv,cv2

if __name__ == "__main__":
    loader = ImageLoader()
    cv.namedWindow('Image')
    img_num = 0
    while True:
        img = loader.get_image(img_num)
        cv.imshow('Image', img)
        key_code = cv.waitKey(10)
        time.sleep(.01)
        img_num += 1
        if key_code == 27:
            break

    cv.destroyAllWindows()

        # elif key_code == ord('s'):
        #     image_num += 1
        # elif key_code == ord('a'):
        #     image_num -= 1