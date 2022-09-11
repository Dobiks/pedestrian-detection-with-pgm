import cv2
import os


class ImageLoader:
    def __init__(self, ds_path) -> None:
        self.frames_names = sorted(os.listdir(f"{ds_path}/frames/"))
        self.lines = self.__get_lines(f"{ds_path}/bboxes.txt")
        self.img_list = self.__load_images(ds_path)
        self.img_list_len = len(self.img_list)

    def __load_images(self, ds_path) -> list:
        img_list = []
        for file in self.frames_names:
            if file.endswith(".jpg"):
                img_color = cv2.imread(f"{ds_path}/frames/{file}")
                img_list.append((file, img_color))
        return img_list

    def __get_lines(self, file) -> list:
        with open(file, "r") as f:
            lines = f.readlines()
        return lines

    def __get_BB(self, tup_img) -> list:
        coords_list = []
        img_name = tup_img[0]
        for line in self.lines:
            idx = self.lines.index(line)+1
            if img_name in line and int(self.lines[idx].replace("\n", "")) > 0:
                for i in range(int(self.lines[idx])):
                    coords = self.lines[idx+i+1].split()
                    coords_list.append(coords)
        return coords_list

    def get_img_list_len(self) -> int:
        return self.img_list_len

    def get_data(self, image_num) -> tuple:
        img_color = self.img_list[image_num]
        org_img = img_color[1]
        coords = self.__get_BB(img_color)
        return org_img, coords
