from source.main import insert_dashes


def test_no_even__nor_odd_digits_next_to_each_other():
    #act
    original_digits = 45478
    #arrange
    expected = 45478
    result = insert_dashes(original_digits)
    #assert
    assert expected == result
