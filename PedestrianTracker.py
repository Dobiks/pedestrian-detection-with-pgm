from Pedestrian import Pedestrian


class PedestrianTracker:
    def __init__(self) -> None:
        self.frame_n = 0
        self.pedestrians = {}

    def new_frame(self, frame, coords):
        self.frame_n += 1
        self.pedestrians[self.frame_n] = self.track_pedestrians(frame, coords)

    def track_pedestrians(self, frame, coords):
        pedestrians = []
        for coord in coords:
            pedestrians.append(Pedestrian(frame, coord))
        return pedestrians
