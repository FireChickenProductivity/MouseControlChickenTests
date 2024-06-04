from ..source.display.UniversalDisplays import UniversalPositionDisplay
from ..source.GridFactory import SquareRecursiveDivisionGridFactory, RectangularRecursiveDivisionGridFactory
from ..source.display.Canvas import Canvas, Text
from ..source.grid.Grid import Rectangle
import unittest

def compute_one_through_four_grid():
    return SquareRecursiveDivisionGridFactory().create_grid("2")

def compute_one_by_two_grid():
    return RectangularRecursiveDivisionGridFactory().create_grid("1:2")

def assert_text_element_inside_list(assertion_class: unittest.TestCase, element, elements):
    for e in elements:
        if e.x == element.x and e.y == element.y and e.text == element.text:
            return
    assertion_class.fail(f"Element not found in list {element.x}, {element.y}, {element.text}")

class UniversalPositionDisplayTest(unittest.TestCase):
    def test_display_with_one_through_four_grid(self):
        rectangle = Rectangle(1, 5, 1, 5)
        grid = compute_one_through_four_grid()
        grid.make_around(rectangle)
        display = UniversalPositionDisplay()
        display.set_rectangle(rectangle)
        canvas = Canvas()
        display.set_grid(grid)
        display.draw_on(canvas)
        text_manager = canvas.text
        text_elements = text_manager.elements[:]
        self.assertEqual(4, len(text_elements))
        assert_text_element_inside_list(self, Text(2, 2, "1"), text_elements)
        assert_text_element_inside_list(self, Text(4, 2, "2"), text_elements)
        assert_text_element_inside_list(self, Text(2, 4, "3"), text_elements)
        assert_text_element_inside_list(self, Text(4, 4, "4"), text_elements)
        
    def test_display_with_one_by_two_grid(self):
        rectangle = Rectangle(1, 5, 1, 5)
        grid = compute_one_by_two_grid()
        grid.make_around(rectangle)
        display = UniversalPositionDisplay()
        display.set_rectangle(rectangle)
        canvas = Canvas()
        display.set_grid(grid)
        display.draw_on(canvas)
        text_manager = canvas.text
        text_elements = text_manager.elements[:]
        self.assertEqual(2, len(text_elements))
        assert_text_element_inside_list(self, Text(3, 2, "1"), text_elements)
        assert_text_element_inside_list(self, Text(3, 4, "2"), text_elements)