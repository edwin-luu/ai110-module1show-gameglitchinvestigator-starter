from app import check_guess


def test_go_higher_when_guess_is_below_secret():
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_go_lower_when_guess_is_above_secret():
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_correct_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_go_higher_when_guess_is_one_below_secret():
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_go_lower_when_guess_is_one_above_secret():
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
