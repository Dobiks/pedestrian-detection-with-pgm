from itertools import combinations
import numpy as np
import cv2
from pgmpy.inference import BeliefPropagation
from pgmpy.models import FactorGraph
from pgmpy.factors.discrete import DiscreteFactor
from Pedestrian import Pedestrian


class GraphCreator:
    def __get_matrix(self, previous_pedestrians: list) -> np.ndarray:
        m_size = len(previous_pedestrians)+1
        matrix = np.full((m_size, m_size), 1.0)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if i == j and i != 0 and j != 0:
                    matrix[i][j] = 0.0
        return matrix

    def create(self, pedestrians: Pedestrian, previous_pedestrians: Pedestrian) -> str:
        g = FactorGraph()
        for i, current_ped in enumerate(pedestrians):
            hist_means = []
            g.add_nodes_from([str(i)])
            for j, previous_ped in enumerate(previous_pedestrians):
                hist_diff = []
                for hist_idx in range(len(current_ped.get_histograms())):
                    hist_diff.append(1.0 - cv2.compareHist(current_ped.get_histograms()[
                                     hist_idx], previous_ped.get_histograms()[hist_idx], cv2.HISTCMP_BHATTACHARYYA))
                hist_means.append(sum(hist_diff) / len(hist_diff))
            tmp_df = DiscreteFactor(
                [str(i)], [len(previous_pedestrians)+1], [[0.54] + hist_means])
            g.add_factors(tmp_df)
            g.add_edge(str(i), tmp_df)

        matrix = self.__get_matrix(previous_pedestrians)

        if len(pedestrians) > 1:
            for ped1, ped2 in combinations(pedestrians, 2):
                tmp_df = DiscreteFactor([str(pedestrians.index(ped1)), str(pedestrians.index(ped2))],
                                        [len(previous_pedestrians)+1, len(previous_pedestrians)+1], matrix)
                g.add_factors(tmp_df)
                g.add_edge(str(pedestrians.index(ped1)), tmp_df)
                g.add_edge(str(pedestrians.index(ped2)), tmp_df)

        bp = BeliefPropagation(g)
        bp.calibrate()
        bp_dict = bp.map_query(g.get_variable_nodes(), show_progress=False)

        result = [str(bp_dict[key]-1) for key in bp_dict]

        return ' '.join(result)
