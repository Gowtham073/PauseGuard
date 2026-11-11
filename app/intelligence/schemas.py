from typing import List, Literal, Optional
from pydantic import BaseModel, Field

class TransactionHistoryItem(BaseModel):
    amount: float
    payee_id: str
    timestamp_hour: int

class RiskSignalRequest(BaseModel):
    transaction_id: str
    user_id: str
    profile_type: Literal["personal", "professional", "business"] = "personal"
    amount: float
    payee_id: str
    is_new_beneficiary: bool
    beneficiary_age_days: int = 0
    tx_count_last_60m: int = 0
    rolling_amount_60m: float = 0.0
    hour_of_day: int = 12
    purpose_selected: Optional[str] = None
    consented_transcript: Optional[str] = None
    history: List[TransactionHistoryItem] = Field(default_factory=list)

class RiskSignalResponse(BaseModel):
    transaction_id: str
    advisory_score: int = Field(ge=0, le=100)
    reason_codes: List[str]
    plain_reasons: List[str]
    ai_status: Literal["OK", "FALLBACK"] = "OK"
    uncertainty: Literal["LOW", "MEDIUM", "HIGH"] = "LOW"
    model_notes: List[str] = Field(default_factory=list)

