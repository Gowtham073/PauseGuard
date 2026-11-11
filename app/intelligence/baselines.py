from typing import Dict, List, Tuple
import numpy as np
from .schemas import RiskSignalRequest

PROFILE_DEFAULT_AVG = {"personal": 3500.0, "professional": 18000.0, "business": 55000.0}

def evaluate_baseline(req: RiskSignalRequest) -> Tuple[int, List[str], List[str], Dict[str, float]]:
    reasons, codes, score = [], [], 0
    if req.history:
        mean_amt = float(np.mean([h.amount for h in req.history]))
        cold_start = False
    else:
        mean_amt = PROFILE_DEFAULT_AVG[req.profile_type]
        cold_start = True

    ratio = req.amount / max(mean_amt, 1.0)
    if req.is_new_beneficiary:
        score += 25
        codes.append("R01_NEW_BENEFICIARY")
        reasons.append(f"New beneficiary (account added {req.beneficiary_age_days} days ago)")
    if ratio >= 4.0:
        score += 30
        codes.append("R03_UNUSUAL_AMOUNT")
        reasons.append(f"Amount is {ratio:.1f}x higher than your usual ₹{mean_amt:,.0f} average")
    elif ratio >= 2.0:
        score += 15
        codes.append("R03_ELEVATED_AMOUNT")
        reasons.append(f"Amount is {ratio:.1f}x higher than your usual average")
    if req.tx_count_last_60m >= 3:
        score += 25
        codes.append("R05_HIGH_VELOCITY")
        reasons.append(f"{req.tx_count_last_60m} transfers attempted in the last 60 minutes")

    return min(score, 100), codes, reasons, {"mean_amt": mean_amt, "amount_ratio": ratio, "cold_start": float(cold_start)}

