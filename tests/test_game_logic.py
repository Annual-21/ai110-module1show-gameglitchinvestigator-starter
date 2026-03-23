import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_score_symmetry_too_high_vs_too_low_odd_attempt():
    """
    Test that "Too High" and "Too Low" outcomes have symmetric scoring
    on odd attempts. Both should penalize by -5 points.
    
    This tests the fix for the bug where "Too Low" was always penalized
    while "Too High" had conditional logic based on attempt number.
    """
    current_score = 100
    odd_attempt = 1
    
    score_too_high = update_score(current_score, "Too High", odd_attempt)
    score_too_low = update_score(current_score, "Too Low", odd_attempt)
    
    # Both should penalize by 5 points on odd attempts
    assert score_too_high == 95, "Too High on odd attempt should penalize -5"
    assert score_too_low == 95, "Too Low on odd attempt should penalize -5"
    assert score_too_high == score_too_low, "Too High and Too Low should have same score on odd attempts"


def test_score_symmetry_too_high_vs_too_low_even_attempt():
    """
    Test that "Too High" and "Too Low" outcomes have symmetric scoring
    on even attempts. Both should reward by +5 points.
    
    This confirms the fix ensures both outcomes are equally treated.
    """
    current_score = 100
    even_attempt = 2
    
    score_too_high = update_score(current_score, "Too High", even_attempt)
    score_too_low = update_score(current_score, "Too Low", even_attempt)
    
    # Both should reward by 5 points on even attempts
    assert score_too_high == 105, "Too High on even attempt should reward +5"
    assert score_too_low == 105, "Too Low on even attempt should reward +5"
    assert score_too_high == score_too_low, "Too High and Too Low should have same score on even attempts"
