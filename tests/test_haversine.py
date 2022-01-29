from mlproject.distance import haversine

def test_haversine():
    assert haversine(48, 2, 47, 3) != 0