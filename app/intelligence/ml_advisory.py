import numpy as np
from sklearn.ensemble import IsolationForest
from .synthetic_data import generate_synthetic_dataset

FEATURES = ["amount_ratio", "is_new_beneficiary", "tx_count_60m"]

class AnomalyAdvisor:
    def __init__(self):
        df = generate_synthetic_dataset()
        normal_df = df[df["is_scam"] == 0].copy()
        normal_df["amount_ratio"] = normal_df["amount"] / normal_df["user_avg_amount"].clip(lower=1.0)
        self.model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        self.model.fit(normal_df[FEATURES].values)

    def score(self, amount_ratio: float, is_new_beneficiary: bool, tx_count_60m: int) -> int:
        X = np.array([[amount_ratio, int(is_new_beneficiary), tx_count_60m]])
        raw = float(self.model.decision_function(X)[0])
        return int(np.clip((0.20 - raw) / 0.45 * 100, 0, 100))

