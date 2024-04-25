from city_functions import get_formatted_location

def test_city_country():
    """Do locations like 'Santiago, Chile' work?"""
    formatted_location = get_formatted_location('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile'

def test_city_country_population():
    """Do locations like 'santiago, chile, 5000000' work?"""
    formatted_location = get_formatted_location('santiago', 'chile', 5000000)
    assert formatted_location == 'Santiago, Chile - Population 5000000'