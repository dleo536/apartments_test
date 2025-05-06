from apartment_finder import find_closest_apartment

def test_find_closest_apartment():
    expected = "808 Berry St, Saint Paul, MN 55114"
    result = find_closest_apartment()
    assert result and result.strip().lower() == expected.strip().lower(), f"Expected '{expected}', but got '{result}'"
