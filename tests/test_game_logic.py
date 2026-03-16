from logic_utils import check_guess, reset_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win and message should be correct.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and message should ask lower.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and message should ask higher.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_reset_game_state_resets_status_and_history():
    state = {
        "attempts": 5,
        "secret": 42,
        "score": 25,
        "status": "lost",
        "history": [10, 20, 30],
    }
    reset_game_state(state, low=1, high=100)

    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert 1 <= state["secret"] <= 100
