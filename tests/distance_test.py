from mlproject.distance import haversine

def test_length_coordinates():
    assert haversine(10.0,10.0,10.0,11.0) != 0
