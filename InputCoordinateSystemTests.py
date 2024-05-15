from ..source import InputCoordinateSystem
from .TestingUtilities import assert_actual_equals_expected

def create_one_through_nine_coordinate_system():
    return InputCoordinateSystem.SimpleNumericCoordinateSystem(1, 9)

def return_unraveled_generator(generator):
    return [value for value in generator]

def test_simple_numeric_coordinate_system():
    coordinate_system = create_one_through_nine_coordinate_system()
    expected = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
    assert_actual_equals_expected(actual, expected)




test_simple_numeric_coordinate_system()