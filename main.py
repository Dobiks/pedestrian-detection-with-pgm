from ImageLoader import ImageLoader
from Pedestrian import Pedestrian
from GraphCreator import GraphCreator
import argparse

# TODO Jakość kodu i raport (4/5)
# TODO Raport zawiera większość potrzebnych informacji, jednak jest mało czytelny.
# TODO Kod przejrzysty i dobrze udokumentowany.

# TODO Skuteczność śledzenia  0.622 (3.5/5)
# TODO [0.00, 0.0] - 0.0
# TODO (0.0, 0.1) - 0.5
# TODO [0.1, 0.2) - 1.0
# TODO [0.2, 0.3) - 1.5
# TODO [0.3, 0.4) - 2.0
# TODO [0.4, 0.5) - 2.5
# TODO [0.5, 0.6) - 3.0
# TODO [0.6, 0.7) - 3.5
# TODO [0.7, 0.8) - 4.0
# TODO [0.8, 0.9) - 4.5
# TODO [0.9, 1.0) - 5.0

# niepoprawne wyjście: oczekiwana liczba linii = 400, otrzymana liczba linii = 399

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

        # TODO W przypadku braku bboxów program powinien wypisać pustą linię.
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
