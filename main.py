from ImageLoader import ImageLoader
from Pedestrian import Pedestrian
from GraphCreator import GraphCreator
import argparse


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument('ds', type=str)
    args = arg.parse_args()
    
    loader = ImageLoader(args.ds)
    graph_creator = GraphCreator()
    
    previous_pedestrians = None
    
    for img_num in range(loader.get_img_list_len()):
        org_img, coords = loader.get_data(img_num)
        pedestrians = [Pedestrian(org_img, coord, i)
                       for i, coord in enumerate(coords)]

        if len(pedestrians) == 0:
            # No pedestrians in the frame
            previous_pedestrians = None
            continue

        if previous_pedestrians is None:
            # First frame
            previous_pedestrians = pedestrians
            print('-1 '*len(pedestrians))
            continue

        result = graph_creator.create(pedestrians, previous_pedestrians)
        print(result)
        previous_pedestrians = pedestrians
