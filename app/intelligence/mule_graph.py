import networkx as nx
from typing import Tuple

class MuleGraphAnalyzer:
    def __init__(self):
        self.graph = nx.Graph()
        self.graph.add_edges_from([
            ("U_NORMAL_1", "MERCHANT_CHAI"), ("U_NORMAL_1", "MERCHANT_GROCERY"),
            ("MULE_HUB_1", "RAHUL_SHARMA_UPI"), ("MULE_HUB_1", "SUSPECT_ACC_2"),
            ("SUSPECT_ACC_2", "LAYERING_ACC_3"),
        ])
        self.flagged_mules = {"MULE_HUB_1"}

    def check_payee(self, payee_id: str) -> Tuple[int, int]:
        if payee_id not in self.graph:
            return 0, 99
        min_hops = min(
            (nx.shortest_path_length(self.graph, payee_id, m) for m in self.flagged_mules if nx.has_path(self.graph, payee_id, m)),
            default=99,
        )
        if min_hops <= 1:
            return 35, min_hops
        if min_hops == 2:
            return 20, min_hops
        return 0, min_hops

