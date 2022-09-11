from ImageLoader import ImageLoader
from Pedestrian import Pedestrian
from GraphCreator import GraphCreator


if __name__ == "__main__":
    graph_creator = GraphCreator()
    loader = ImageLoader()
    previous_pedestrians = None
    for img_num in range(loader.get_img_list_len()):
        org_img, coords = loader.get_data(img_num)
        pedestrians = [Pedestrian(org_img, coord, i) for i, coord in enumerate(coords)]

        if len(pedestrians) == 0:
            previous_pedestrians = None
            continue

        if previous_pedestrians is None:
            previous_pedestrians = pedestrians
            print('-1 '*len(pedestrians))
            continue

        result = graph_creator.create(pedestrians, previous_pedestrians)
        print(result)
        previous_pedestrians = pedestrians
