import pytest
from src.triage import TriageModel
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_triage_prediction():
    triage = TriageModel("Assignment Data Base.xlsx")
    result = triage.predict_condition("sweating and shaky")[0]
    
    assert result["matched_sentence"] is not None
    assert result["score"] > 0.3
