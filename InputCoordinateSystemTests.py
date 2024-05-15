from ..source import InputCoordinateSystem
import unittest

def create_one_through_nine_coordinate_system():
    return InputCoordinateSystem.SimpleNumericCoordinateSystem(1, 9)

def return_unraveled_generator(generator):
    return [value for value in generator]

def create_valid_one_through_nine_primary_coordinates():
    return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def assert_primary_coordinates_belong_to_system(testing_class: unittest.TestCase, coordinate_system: InputCoordinateSystem.InputCoordinateSystem):
    for coordinate in coordinate_system.get_primary_coordinates():
        testing_class.assertTrue(coordinate_system.do_coordinates_belong_to_system(coordinate))

def assert_extreme_numeric_values_do_not_belong_to_system(testing_class: unittest.TestCase, coordinate_system: InputCoordinateSystem.InputCoordinateSystem):
    for value in range(10, 90):
        testing_class.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))
    for value in range(-90, 1):
        testing_class.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))

def assert_system_handles_primary_coordinates_and_extreme_numeric_values(testing_class: unittest.TestCase, coordinate_system: InputCoordinateSystem.InputCoordinateSystem):
    assert_primary_coordinates_belong_to_system(testing_class, coordinate_system)
    assert_extreme_numeric_values_do_not_belong_to_system(testing_class, coordinate_system)

class TestInputCoordinateSystemTests(unittest.TestCase):
    def test_simple_numeric_coordinate_system_primary_coordinates(self):
        coordinate_system = create_one_through_nine_coordinate_system()
        expected = create_valid_one_through_nine_primary_coordinates()
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        self.assertEqual(actual, expected)

    def test_simple_numeric_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = create_one_through_nine_coordinate_system()
        assert_system_handles_primary_coordinates_and_extreme_numeric_values(self, coordinate_system)
        
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

class ListCoordinateSystemTests(unittest.TestCase):
    def test_list_coordinate_system_primary_coordinates(self):
        coordinate_system = create_simple_list_coordinate_system()
        first_expected = ["1", "2"]
        second_expected = ["2", "1"]
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        self.assertTrue(actual == first_expected or actual == second_expected)
    
    def test_list_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = create_simple_list_coordinate_system()
        assert_system_handles_primary_coordinates_and_extreme_numeric_values(self, coordinate_system)

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

def create_simple_sequential_combination_coordinate_system():
    one_through_nine_system = create_one_through_nine_coordinate_system()
    list_system = create_simple_list_coordinate_system()
    return InputCoordinateSystem.SequentialCombinationCoordinateSystem([one_through_nine_system, list_system])

def assert_lists_have_same_elements_and_size(testing_class: unittest.TestCase, first_list, second_list):
    testing_class.assertEqual(len(first_list), len(second_list))
    for element in first_list:
        testing_class.assertTrue(element in second_list)

class SequentialCombinationCoordinateSystemTests(unittest.TestCase):
    def test_sequential_combination_coordinate_system_primary_coordinates(self):
        coordinate_system = create_simple_sequential_combination_coordinate_system()
        first_system_coordinates = create_valid_one_through_nine_primary_coordinates() 
        second_system_coordinates = ["1", "2"]
        expected = []
        for first_coordinate in first_system_coordinates:
            for second_coordinate in second_system_coordinates:
                expected.append(first_coordinate + " " + second_coordinate)
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        assert_lists_have_same_elements_and_size(self, expected, actual)

    def test_sequential_combination_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = create_simple_sequential_combination_coordinate_system()
        assert_primary_coordinates_belong_to_system(self, coordinate_system)
        for value in create_valid_one_through_nine_primary_coordinates():
            self.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))

    def test_sequential_combination_coordinate_system_do_coordinates_start_belong_to_system(self):
        coordinate_system = create_simple_sequential_combination_coordinate_system()
        endings = ["0", "10", "-1", "-10", "a", "b", "c k", "d", "e", "f", "g", "h", "i", "j", "1"]
        for coordinate in coordinate_system.get_primary_coordinates():
            for ending in endings:
                self.assertTrue(coordinate_system.do_coordinates_start_belong_to_system(coordinate + " " + ending))
        for value in range(10, 15):
            for ending in endings:
                self.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value) + " " + ending))
            
    def test_sequential_combination_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = create_simple_sequential_combination_coordinate_system()
        for coordinate in coordinate_system.get_primary_coordinates():
            for value in range(0, 20):
                self.assertEqual(
                    coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system(coordinate + " " + str(value)),
                    (coordinate, str(value))
                )
        self.assertEqual(
            coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system("1 1 2 c"),
            ("1 1", "2 c")
        )
    
def simple_alphabetical_list_input_coordinate_system():
    return InputCoordinateSystem.ListCoordinateSystem(["a", "b"])

class DisjointUnionCoordinateSystemTests(unittest.TestCase):
    def test_disjoint_union_coordinate_system_primary_coordinates(self):
        coordinate_system = InputCoordinateSystem.DisjointUnionCoordinateSystem([create_one_through_nine_coordinate_system(), simple_alphabetical_list_input_coordinate_system()])
        expected = create_valid_one_through_nine_primary_coordinates() + ["a", "b"]
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        assert_lists_have_same_elements_and_size(self, expected, actual)

    def test_disjoint_union_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = InputCoordinateSystem.DisjointUnionCoordinateSystem([create_one_through_nine_coordinate_system(), simple_alphabetical_list_input_coordinate_system()])
        assert_primary_coordinates_belong_to_system(self, coordinate_system)

    def test_disjoint_union_coordinate_system_do_coordinates_start_belong_to_system(self):
        coordinate_system = InputCoordinateSystem.DisjointUnionCoordinateSystem([create_one_through_nine_coordinate_system(), simple_alphabetical_list_input_coordinate_system()])
        endings = ["0", "10", "-1", "-10", "a", "b", "c k", "d", "e", "f", "g", "h", "i", "j", "1"]
        for coordinate in coordinate_system.get_primary_coordinates():
            for ending in endings:
                self.assertTrue(coordinate_system.do_coordinates_start_belong_to_system(coordinate + " " + ending))
        for value in range(10, 15):
            for ending in endings:
                self.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value) + " " + ending))
            
    def test_disjoint_union_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = InputCoordinateSystem.DisjointUnionCoordinateSystem([create_one_through_nine_coordinate_system(), simple_alphabetical_list_input_coordinate_system()])
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