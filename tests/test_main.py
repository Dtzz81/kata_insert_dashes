from source.main import insert_dashes

def test_no_even__nor_odd_digits_next_to_each_other():
    #act
    original_digits = 45478
    #arrange
    expected = "45478"
    result = insert_dashes(original_digits)
    #assert
    assert expected == result

def test_insert_dash_between_two_odd_digits():
    original_digits = 79

    expected = "7-9"
    result = insert_dashes(original_digits)

    assert expected == result

def test_insert_dash_between_another_two_odds():
    original_digits = 51

    expected = "5-1"
    result = insert_dashes(original_digits)

    assert expected == result

def test_odd_even_only():
    original_digits = 52

    expected = "52"
    result = insert_dashes(original_digits)

    assert expected == result

def test_three_digits_odd_even_odd():
    original_digits = 525

    expected = "525"
    result = insert_dashes(original_digits)

    assert expected == result

def test_three_digits_odd_odd_even():
    original_digits = 552

    expected = "5-52"
    result = insert_dashes(original_digits)

    assert expected == result
