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
    for value in range(80, 90):
        testing_class.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))
    for value in range(-10, 1):
        testing_class.assertFalse(coordinate_system.do_coordinates_belong_to_system(str(value)))

def assert_system_handles_primary_coordinates_and_extreme_numeric_values(testing_class: unittest.TestCase, coordinate_system: InputCoordinateSystem.InputCoordinateSystem):
    assert_primary_coordinates_belong_to_system(testing_class, coordinate_system)
    assert_extreme_numeric_values_do_not_belong_to_system(testing_class, coordinate_system)

def assert_coordinates_not_including_extreme_values_handle_do_coordinates_start_belong_to_system(testing_class: unittest.TestCase, coordinate_system: InputCoordinateSystem.InputCoordinateSystem):
    endings = ["0", "10", "-1", "-10", "a", "b", "c k", "d", "e", "f", "g", "h", "i", "j", "1"]
    for valid_coordinates in coordinate_system.get_primary_coordinates():
        for ending in endings:
            testing_class.assertTrue(coordinate_system.do_coordinates_start_belong_to_system(valid_coordinates + " " + ending))
            
    for value in range(80, 90):
        testing_class.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value)))
        for ending in endings:
            testing_class.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value) + " " + ending))
        for valid_coordinates in coordinate_system.get_primary_coordinates():
            testing_class.assertFalse(coordinate_system.do_coordinates_start_belong_to_system(str(value) + " " + valid_coordinates))

def assert_coordinate_system_split_works(testing_class: unittest.TestCase, coordinate_system: InputCoordinateSystem.InputCoordinateSystem):
    for coordinate in coordinate_system.get_primary_coordinates():
        for value in ["30", "a9 20"]:
            testing_class.assertEqual(
                coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system(coordinate + " " + value),
                (coordinate, value)
            )
    value_belonging_to_another_system = "valuenotinanysystem"
    testing_class.assertEqual(
        coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system(value_belonging_to_another_system),
        ("", value_belonging_to_another_system)
    )

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
        coordinate_system = create_one_through_nine_coordinate_system()
        assert_coordinates_not_including_extreme_values_handle_do_coordinates_start_belong_to_system(self, coordinate_system)
            
    def test_simple_coordinates_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        assert_coordinate_system_split_works(self, create_one_through_nine_coordinate_system())

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
        assert_coordinates_not_including_extreme_values_handle_do_coordinates_start_belong_to_system(self, coordinate_system)
            
    def test_list_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = create_simple_list_coordinate_system()
        assert_coordinate_system_split_works(self, coordinate_system)

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
        assert_coordinates_not_including_extreme_values_handle_do_coordinates_start_belong_to_system(self, coordinate_system)
            
    def test_sequential_combination_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = create_simple_sequential_combination_coordinate_system()
        assert_coordinate_system_split_works(self, coordinate_system)
    
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
        assert_system_handles_primary_coordinates_and_extreme_numeric_values(self, coordinate_system)

    def test_disjoint_union_coordinate_system_do_coordinates_start_belong_to_system(self):
        coordinate_system = InputCoordinateSystem.DisjointUnionCoordinateSystem([create_one_through_nine_coordinate_system(), simple_alphabetical_list_input_coordinate_system()])
        assert_coordinates_not_including_extreme_values_handle_do_coordinates_start_belong_to_system(self, coordinate_system)
            
    def test_disjoint_union_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = InputCoordinateSystem.DisjointUnionCoordinateSystem([create_one_through_nine_coordinate_system(), simple_alphabetical_list_input_coordinate_system()])
        assert_coordinate_system_split_works(self, coordinate_system)
    
def create_simple_infinite_sequence_alphabetic_coordinate_system():
    return InputCoordinateSystem.InfiniteSequenceCoordinateSystem(simple_alphabetical_list_input_coordinate_system())

class InfiniteSequenceCoordinateSystemTests(unittest.TestCase):
    def test_infinite_sequence_coordinate_system_primary_coordinates(self):
        coordinate_system = create_simple_infinite_sequence_alphabetic_coordinate_system()
        expected = ["a", "b"]
        actual = return_unraveled_generator(coordinate_system.get_primary_coordinates())
        assert_lists_have_same_elements_and_size(self, expected, actual)

    def test_infinite_sequence_coordinate_system_do_coordinates_belong_to_system(self):
        coordinate_system = create_simple_infinite_sequence_alphabetic_coordinate_system()
        assert_system_handles_primary_coordinates_and_extreme_numeric_values(self, coordinate_system)
        for first_coordinate in coordinate_system.get_primary_coordinates():
            for second_coordinate in coordinate_system.get_primary_coordinates():
                self.assertTrue(coordinate_system.do_coordinates_belong_to_system(first_coordinate + " " + second_coordinate))
            self.assertFalse(coordinate_system.do_coordinates_belong_to_system(first_coordinate + " " + "90"))

    def test_infinite_sequence_coordinate_system_do_coordinates_start_belong_to_system(self):
        coordinate_system = create_simple_infinite_sequence_alphabetic_coordinate_system()
        assert_coordinates_not_including_extreme_values_handle_do_coordinates_start_belong_to_system(self, coordinate_system)
        for first_coordinate in coordinate_system.get_primary_coordinates():
            for second_coordinate in coordinate_system.get_primary_coordinates():
                for value in ["90", "a9 20"]:
                    self.assertTrue(coordinate_system.do_coordinates_start_belong_to_system(first_coordinate + " " + second_coordinate + " " + value))
            
    def test_infinite_sequence_coordinate_system_split_coordinates_with_head_belonging_to_one_system_and_tail_belonging_to_another(self):
        coordinate_system = create_simple_infinite_sequence_alphabetic_coordinate_system()
        assert_coordinate_system_split_works(self, coordinate_system)
        for coordinate in coordinate_system.get_primary_coordinates():
            for another_coordinate in coordinate_system.get_primary_coordinates():
                for value in ["30", "a9 20"]:
                    self.assertEqual(
                        coordinate_system.split_coordinates_with_head_belonging_to_system_and_tail_belonging_to_another_system(coordinate + " " + another_coordinate + " " + value),
                        (coordinate + " " + another_coordinate, value)
                    )
        