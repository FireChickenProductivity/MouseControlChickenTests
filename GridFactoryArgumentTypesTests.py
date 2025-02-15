from ..source.grid_creation.GridFactoryArgumentTypes import TwoToNineArgumentType, PositiveIntegerArgumentType, GridOptionArgumentType, CustomCoordinateSystemArgumentType, GRID_CREATION_ARGUMENT_TWO_TO_NINE_TAG, GRID_CREATION_ARGUMENT_POSITIVE_INTEGER_TAG, ARGUMENT_INPUT_THROUGH_DICTATION_INPUT_TAG
import unittest
from .TestUtilities import assert_true_for_all, assert_false_for_all

DEFAULT_GRID_OPTION_NAMES = ["one to nine", "alphabet", "double alphabet", "alphabet numbers", "double alphabet numbers"]
EXPECTED_CUSTOM_COORDINATE_SYSTEM_FILE_NAME = "newer"

class GridFactoryArgumentTypesTests(unittest.TestCase):
    def test_two_to_nine_argument_type_with_valid_values(self):
        argument_type = TwoToNineArgumentType()
        valid_values = ["2", "3", "4", "5", "6", "7", "8", "9"]
        assert_true_for_all(self, argument_type.does_argument_match_type, valid_values)

    def test_to_two_nine_argument_type_with_invalid_values(self):
        argument_type = TwoToNineArgumentType()
        invalid_values = ["1", "10", "0", "-1", "text"]
        assert_false_for_all(self, argument_type.does_argument_match_type, invalid_values)

    def test_to_two_nine_argument_type_does_not_support_options_dialogue(self):
        argument_type = TwoToNineArgumentType()
        self.assertFalse(argument_type.supports_options_dialogue())

    def test_to_two_nine_argument_type_supports_correct_tags(self):
        argument_type = TwoToNineArgumentType()
        self.assertEqual([ARGUMENT_INPUT_THROUGH_DICTATION_INPUT_TAG, GRID_CREATION_ARGUMENT_TWO_TO_NINE_TAG], argument_type.get_tags())

    
    def test_positive_integer_argument_type_with_valid_values(self):
        argument_type = PositiveIntegerArgumentType()
        valid_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        assert_true_for_all(self, argument_type.does_argument_match_type, valid_values)
    
    def test_grid_option_argument_type_with_invalid_values(self):
        argument_type = PositiveIntegerArgumentType()
        invalid_values = ["0", "-1", "text", "-2"]
        assert_false_for_all(self, argument_type.does_argument_match_type, invalid_values)

    def test_positive_integer_argument_type_does_not_support_options_dialogue(self):
        argument_type = PositiveIntegerArgumentType()
        self.assertFalse(argument_type.supports_options_dialogue())
    
    def test_positive_integer_argument_type_supports_correct_tags(self):
        argument_type = PositiveIntegerArgumentType()
        self.assertEqual([ARGUMENT_INPUT_THROUGH_DICTATION_INPUT_TAG, GRID_CREATION_ARGUMENT_POSITIVE_INTEGER_TAG], argument_type.get_tags())

    
    def test_grid_option_argument_type_with_valid_values(self):
        argument_type = GridOptionArgumentType()
        valid_values = DEFAULT_GRID_OPTION_NAMES
        assert_true_for_all(self, argument_type.does_argument_match_type, valid_values)

    def test_grid_option_argument_type_with_invalid_values(self):
        argument_type = GridOptionArgumentType()
        invalid_value= "no99"
        self.assertFalse(argument_type.does_argument_match_type(invalid_value))

    def test_grid_option_argument_type_supports_options_dialogue(self):
        argument_type = GridOptionArgumentType()
        self.assertTrue(argument_type.supports_options_dialogue())

    def test_grid_option_argument_type_supports_correct_tags(self):
        argument_type = GridOptionArgumentType()
        self.assertEqual([], argument_type.get_tags())

    def test_grid_option_argument_type_has_expected_options(self):
        argument_type = GridOptionArgumentType()
        actual_options = argument_type.get_options()
        for option in DEFAULT_GRID_OPTION_NAMES:
            self.assertTrue(option in actual_options)

    
    def test_custom_coordinate_system_argument_type_with_valid_value(self):
        argument_type = CustomCoordinateSystemArgumentType()
        valid_value = EXPECTED_CUSTOM_COORDINATE_SYSTEM_FILE_NAME
        self.assertTrue(argument_type.does_argument_match_type(valid_value))

    def test_custom_coordinate_system_argument_type_with_invalid_value(self):
        argument_type = CustomCoordinateSystemArgumentType()
        invalid_value = "undefined.csv"
        self.assertFalse(argument_type.does_argument_match_type(invalid_value))

    def test_custom_coordinate_system_argument_type_supports_options_dialogue(self):
        argument_type = CustomCoordinateSystemArgumentType()
        self.assertTrue(argument_type.supports_options_dialogue())

    def test_custom_coordinate_system_argument_type_supports_correct_tags(self):
        argument_type = CustomCoordinateSystemArgumentType()
        self.assertEqual([], argument_type.get_tags())

    def test_custom_coordinate_system_argument_type_has_expected_options(self):
        argument_type = CustomCoordinateSystemArgumentType()
        actual_options = argument_type.get_options()
        self.assertTrue(EXPECTED_CUSTOM_COORDINATE_SYSTEM_FILE_NAME in actual_options)