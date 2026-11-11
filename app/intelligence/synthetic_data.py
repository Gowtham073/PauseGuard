import numpy as np
import pandas as pd

def generate_synthetic_dataset(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for i in range(150):
        rows.append({
            "tx_id": f"NORM_P_{i}", "profile_type": "personal",
            "amount": float(np.round(rng.uniform(100, 6000), 2)),
            "user_avg_amount": 3500.0, "is_new_beneficiary": int(rng.random() < 0.15),
            "tx_count_60m": int(rng.choice([0, 1], p=[0.85, 0.15])),
            "mule_hops": 99, "coercion_hits": 0, "is_scam": 0, "scenario": "normal_personal",
        })
    for i in range(50):
        rows.append({
            "tx_id": f"NORM_B_{i}", "profile_type": "business",
            "amount": float(np.round(rng.uniform(15000, 95000), 2)),
            "user_avg_amount": 55000.0, "is_new_beneficiary": int(rng.random() < 0.25),
            "tx_count_60m": int(rng.choice([0, 1, 2], p=[0.6, 0.3, 0.1])),
            "mule_hops": 99, "coercion_hits": 0, "is_scam": 0, "scenario": "normal_business",
        })
    for i in range(10):
        rows.append({
            "tx_id": f"MED_LEGIT_{i}", "profile_type": "personal",
            "amount": 80000.0, "user_avg_amount": 8200.0, "is_new_beneficiary": 1,
            "tx_count_60m": 0, "mule_hops": 99, "coercion_hits": 0, "is_scam": 0, "scenario": "genuine_medical",
        })
    for i in range(40):
        is_smurf = (i % 2 == 1)
        rows.append({
            "tx_id": f"SCAM_{i}", "profile_type": "personal",
            "amount": 12000.0 if is_smurf else 55000.0, "user_avg_amount": 8200.0,
            "is_new_beneficiary": 1, "tx_count_60m": 4 if is_smurf else 1,
            "mule_hops": int(rng.choice([1, 2])),
            "coercion_hits": 0 if is_smurf else int(rng.choice([2, 3])),
            "is_scam": 1, "scenario": "smurfing_scam" if is_smurf else "digital_arrest_55k",
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_synthetic_dataset()
    print("Total synthetic transactions generated:", len(df))
    print(df["scenario"].value_counts())

