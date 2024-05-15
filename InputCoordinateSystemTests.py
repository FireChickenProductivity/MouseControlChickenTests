from ..source import InputCoordinateSystem

def create_one_through_nine_coordinate_system():
    return InputCoordinateSystem.SimpleNumericCoordinateSystem(1, 9)

def return_unraveled_generator(generator):
    return [value for value in generator]

def create_valid_one_through_nine_primary_coordinates():
    return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

import unittest
class TestInputCoordinateSystem(unittest.TestCase):
    def test_simple_numeric_coordinate_system_primary_coordinates(self):
        coordinate_system = create_one_through_nine_coordinate_system()
        expected = create_valid_one_through_nine_primary_coordinates()
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        self.assertEqual(actual, expected)

    def test_simple_numeric_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = create_one_through_nine_coordinate_system()
        for coordinate in coordinate_system.get_primary_coordinates():
            self.assertTrue(coordinate_system.do_coordinates_belong_to_system(coordinate))
        for value in range(10, 90):
            self.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))
        for value in range(-90, 1):
            self.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))
        
    def test_test_simple_numeric_coordinates_system_do_coordinates_start_belong_to_system(self):
        primary_coordinates = create_valid_one_through_nine_primary_coordinates()
        coordinate_system = create_one_through_nine_coordinate_system()
        endings = ["0", "10", "-1", "-10", "a", "b", "c k", "d", "e", "f", "g", "h", "i", "j", "1"]
        for valid_coordinates in primary_coordinates:
            for ending in endings:
                self.assertTrue(coordinate_system.do_coordinates_start_belong_to_system(valid_coordinates + " " + ending))
            
        for value in range(10, 90):
            self.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value)))
            for ending in endings:
                self.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value) + " " + ending))
            
    def test_simple_coordinates_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        primary_coordinates = create_valid_one_through_nine_primary_coordinates()
        coordinate_system = create_one_through_nine_coordinate_system()
        for valid_coordinate in primary_coordinates:
            for value in range(0, 20):
                self.assertEqual(
                coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system(valid_coordinate + " " + str(value)),
                (valid_coordinate, str(value))
                )
        
        self.assertEqual(
            coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system("1 2 c"),
            ("1", "2 c")
        )

def create_simple_list_coordinate_system():
    coordinate_list = ["1", "2"]
    return InputCoordinateSystem.ListCoordinateSystem(coordinate_list)

class ListCoordinateSystem(unittest.TestCase):
    def test_list_coordinate_system_primary_coordinates(self):
        coordinate_system = create_simple_list_coordinate_system()
        first_expected = ["1", "2"]
        second_expected = ["2", "1"]
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        self.assertTrue(actual == first_expected or actual == second_expected)
    
    def test_list_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = create_simple_list_coordinate_system()
        for coordinate in coordinate_system.get_primary_coordinates():
            self.assertTrue(coordinate_system.do_coordinates_belong_to_system(coordinate))
        for value in range(10, 15):
            self.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))

    def test_list_coordinate_system_do_coordinates_start_belong_to_system(self):
        coordinate_system = create_simple_list_coordinate_system()
        endings = ["0", "10", "-1", "-10", "a", "b", "c k", "d", "e", "f", "g", "h", "i", "j", "1"]
        for coordinate in coordinate_system.get_primary_coordinates():
            for ending in endings:
                self.assertTrue(coordinate_system.do_coordinates_start_belong_to_system(coordinate + " " + ending))
        for value in range(10, 15):
            for ending in endings:
                self.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value) + " " + ending))
            
    def test_list_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = create_simple_list_coordinate_system()
        for coordinate in coordinate_system.get_primary_coordinates():
            for value in range(0, 20):
                self.assertEqual(
                    coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system(coordinate + " " + str(value)),
                    (coordinate, str(value))
                )
        self.assertEqual(
            coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system("1 2 c"),
            ("1", "2 c")
        )