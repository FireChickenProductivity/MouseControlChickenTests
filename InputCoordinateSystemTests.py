from ..source import InputCoordinateSystem
from .TestingUtilities import assert_actual_equals_expected, assert_true, assert_false

def create_one_through_nine_coordinate_system():
    return InputCoordinateSystem.SimpleNumericCoordinateSystem(1, 9)

def return_unraveled_generator(generator):
    return [value for value in generator]

def test_simple_numeric_coordinate_system():
    coordinate_system = create_one_through_nine_coordinate_system()
    expected = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
    assert_actual_equals_expected(actual, expected)

    for coordinate in coordinate_system.get_primary_coordinates():
        assert_true(coordinate_system.do_coordinates_belong_to_system(coordinate))
    for value in range(10, 90):
        assert_false(coordinate_system.do_coordinates_belong_to_system(str(value)))
    for value in range(-90, 1):
        assert_false(coordinate_system.do_coordinates_belong_to_system(str(value)))

test_simple_numeric_coordinate_system()