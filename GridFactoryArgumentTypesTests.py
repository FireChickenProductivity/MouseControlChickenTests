from ..source.grid_creation.GridFactoryArgumentTypes import TwoToNineArgumentType, PositiveIntegerArgumentType, GridOptionArgumentType, CustomCoordinateSystemArgumentType
import unittest
from .TestUtilities import assert_true_for_all, assert_false_for_all

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
    