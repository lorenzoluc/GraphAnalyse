import pytest
from functions.searchPath import searchPath
#TODO: improve it and create new tests

class DummyObject:
    def __init__(self, params):
        self.params = params


@pytest.fixture
def setup_data():
    highway_coords = [(0, 0), (0, 1), (0, 2), (1, 2)]
    highway_widths = [1, 1, 1, 1]

    building1 = DummyObject(params=[[0, 0, 1]])
    building2 = DummyObject(params=[[1, 2, 1]])

    return highway_coords, highway_widths, building1, building2

def test_path_found(setup_data):
    highway_coords, highway_widths, building1, building2 = setup_data
    paths, costs = searchPath(building1, building2, highway_coords, highway_widths)

    assert len(paths) > 0, "No path found when there should be one."

    for path in paths:
        assert path[0] == (0, 0), "The path does not start at the correct coordinate."
        assert path[-1] == (1, 2), "The path does not end at the correct coordinate."

def test_no_path(setup_data):
    highway_coords, highway_widths, building1, _ = setup_data
    building3 = DummyObject(params=[[10, 10, 1]])

    paths, costs = searchPath(building1, building3, highway_coords, highway_widths)

    assert len(paths) == 0, "There is a path when there shouldn't have been one."
    assert len(costs) == 0, "It should return zero cost when there is no path."
