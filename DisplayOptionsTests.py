from ..source.display.DisplayOptionsComputations import compute_display_options_given_grid, DisplayOption, DisplayOptions
from ..source.display.RectangularGridDisplays import *
from ..source.display.Display import EmptyDisplay
from ..source.display.UniversalDisplays import UniversalPositionDisplay
from ..source.display.NarrowDisplays import NarrowDisplay, DoubleNarrowDisplay
from ..source.GridFactory import SquareRecursiveDivisionGridFactory, RectangularRecursiveDivisionGridFactory, AlphabetGridFactory
import unittest

def compute_rectangular_display_options():
    rectangular_display_types = [RectangularGridFrameDisplay, RectangularCheckerDisplay, RectangularDiagonalDisplay, RectangularPositionDisplay, DoubleRectangularDiagonalDisplay, 
                               DoubleFrameDisplay, QuadrupleFrameDisplay, EmptyDisplay, UniversalPositionDisplay]
    rectangular_display_options = [DisplayOption(display_type) for display_type in rectangular_display_types]
    return rectangular_display_options

def assert_display_options_match(assertion_class: unittest.TestCase, display_options: DisplayOptions, expected_display_options: DisplayOptions):
    actual_names = display_options.get_names()
    expected_names = expected_display_options.get_names()
    assertion_class.assertEqual(len(expected_names), len(actual_names))
    for name in expected_names:
        assertion_class.assertTrue(name in actual_names)
        actual_type = display_options.get_option_with_name(name).get_type()
        expected_type = expected_display_options.get_option_with_name(name).get_type()
        assertion_class.assertEqual(expected_type, actual_type)

class DisplayOptionsComputationTest(unittest.TestCase):
    def test_handles_rectangular_grid(self):
        grid = AlphabetGridFactory().create_grid("")
        display_options: DisplayOptions = compute_display_options_given_grid(grid)
        rectangular_display_options = compute_rectangular_display_options() 
        assert_display_options_match(self, display_options, DisplayOptions(rectangular_display_options))

