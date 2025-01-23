from source.main import insert_asterisks, insert_dashes

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

def test_three_digits_odd_odd_odd():
    original_digits = 557

    expected = "5-5-7"
    result = insert_dashes(original_digits)

    assert expected == result

def test_four_digits():
    original_digits = 5574

    expected = "5-5-74"
    result = insert_dashes(original_digits)

    assert expected == result

def test_all_odd_four_digits():
    original_digits = 5571

    expected = "5-5-7-1"
    result = insert_dashes(original_digits)

    assert expected == result

def test_long_number():
    original_digits = 1012356895

    expected = "10123-5689-5"
    result = insert_dashes(original_digits)

    assert expected == result

def test_one_digit():
    original_digits = 1

    expected = "1"
    result = insert_dashes(original_digits)

    assert expected == result

#odd digits done

def test_two_even_digits_only():
    original_digits = 22

    expected = "2*2"
    result = insert_asterisks(original_digits)

    assert expected == result

def test_three_digits_odd_even_even():
    original_digits = 522

    expected = "52*2"
    result = insert_asterisks(original_digits)

    assert expected == result

def test_three_digits_even_even_even():
    original_digits = 246

    expected = "2*4*6"
    result = insert_asterisks(original_digits)

    assert expected == result

def test_all_odd_four_digits():
    original_digits = 8246

    expected = "8*2*4*6"
    result = insert_asterisks(original_digits)

    assert expected == result

def test_one_digit():
    original_digits = 1

    expected = "1"
    result = insert_dashes(original_digits)

    assert expected == result

# even numbers done


def test_four_digits():
    original_digits = 2233

    expected = "2*23-3"
    first_result = insert_dashes(original_digits)
    result = insert_asterisks(first_result)

    assert expected == result
