class Pedestrian:
    def __init__(self, frame, coords) -> None:
        self.frame = frame
        self.coords = coords
        self.center = self.get_center()
        self.size = self.get_size()

    def cropp_frame(self):
        x = int(float(self.coords[0]))
        y = int(float(self.coords[1]))
        w = int(float(self.coords[2]))
        h = int(float(self.coords[3]))
        return self.frame[y:y+h, x:x+w]

    def get_size(self):
        w = int(float(self.coords[2]))
        h = int(float(self.coords[3]))
        size = (w, h)
        return size        

    def get_center(self):
        x = int(float(self.coords[0]))
        y = int(float(self.coords[1]))
        w = int(float(self.coords[2]))
        h = int(float(self.coords[3]))
        center = (x + w / 2, y + h / 2)
        print(center)
        return center