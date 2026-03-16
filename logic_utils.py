<<<<<<< HEAD
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
=======
import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
<<<<<<< HEAD
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
=======
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
<<<<<<< HEAD
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
=======
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
<<<<<<< HEAD
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
=======
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def reset_game_state(state: dict, low: int, high: int):
    """Reset a dictionary game state for a new game."""
    # FIX: Added helper to make new-game reset behavior reusable and testable.
    state["attempts"] = 1
    state["secret"] = random.randint(low, high)
    state["score"] = 0
    state["status"] = "playing"
    state["history"] = []
    return state
>>>>>>> 536293a (Fix Streamlit game state bugs and logic refactor)
