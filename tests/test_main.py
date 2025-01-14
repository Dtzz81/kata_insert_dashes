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
    #act
    original_digits = 79
    #arrange
    expected = "7-9"
    result = insert_dashes(original_digits)
    #assert
    assert expected == result

def test_insert_dash_between_another_two_odds():
    #act
    original_digits = 51
    #arrange
    expected = "5-1"
    result = insert_dashes(original_digits)
    #assert
    assert expected == result

def test_odd_even_only():
    #act
    original_digits = 52
    #arrange
    expected = "52"
    result = insert_dashes(original_digits)
    #assert
    assert expected == result
