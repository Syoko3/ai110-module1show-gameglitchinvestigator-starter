from logic_utils import check_guess, get_range_for_difficulty, get_attempts_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be "Win", "🎉 Correct!"
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High", "📉 Go LOWER!"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low", "📈 Go HIGHER!"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_get_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_get_range_default():
    low, high = get_range_for_difficulty("Invalid")
    assert low == 1
    assert high == 100

def test_get_attempts_easy():
    attempts = get_attempts_for_difficulty("Easy")
    assert attempts == 6

def test_get_attempts_normal():
    attempts = get_attempts_for_difficulty("Normal")
    assert attempts == 8

def test_get_attempts_hard():
    attempts = get_attempts_for_difficulty("Hard")
    assert attempts == 5

def test_get_attempts_default():
    attempts = get_attempts_for_difficulty("Invalid")
    assert attempts == 8

def test_update_score_win():
    new_score = update_score(0, "Win", 1)
    assert new_score == 80  # 100 - 10 * (1 + 1) = 80

def test_update_score_win_min():
    new_score = update_score(0, "Win", 9)
    assert new_score == 10  # min 10

def test_update_score_too_high_even():
    new_score = update_score(0, "Too High", 2)
    assert new_score == 5

def test_update_score_too_high_odd():
    new_score = update_score(0, "Too High", 1)
    assert new_score == -5

def test_update_score_too_low():
    new_score = update_score(0, "Too Low", 1)
    assert new_score == -5
