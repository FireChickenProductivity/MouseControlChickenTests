from ..source.display.UniversalDisplays import UniversalPositionDisplay
from ..source.grid_creation.GridFactory import SquareRecursiveDivisionGridFactory, RectangularRecursiveDivisionGridFactory, AlphabetGridFactory
from ..source.display.Canvas import Canvas, Text
from ..source.grid.Grid import Rectangle
import unittest

def compute_one_through_four_grid():
    return SquareRecursiveDivisionGridFactory().create_grid("2")

def compute_one_by_two_grid():
    return RectangularRecursiveDivisionGridFactory().create_grid("1:2")

def assert_text_element_inside_list(assertion_class: unittest.TestCase, element, elements):
    for e in elements:
        #print(f"e.x: {e.x}, e.y: {e.y}, e.text: {e.text}")
        if e.x == element.x and e.y == element.y and e.text == element.text:
            return
    assertion_class.fail(f"Element not found in list {element.x}, {element.y}, {element.text}")

def assert_display_works_for_grid(assertion_class: unittest.TestCase, grid, display, rectangle, expected_text_elements):
    grid.make_around(rectangle)
    display.set_rectangle(rectangle)
    canvas = Canvas()
    display.set_grid(grid)
    display.draw_on(canvas)
    text_manager = canvas.text
    text_elements = text_manager.elements[:]
    for element in expected_text_elements:
        assert_text_element_inside_list(assertion_class, element, text_elements)
    assertion_class.assertEqual(len(expected_text_elements), len(text_elements))

def compute_letter_list():
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
    return letter_list

class UniversalPositionDisplayTest(unittest.TestCase):
    def test_display_with_one_through_four_grid(self):
        rectangle = Rectangle(1, 5, 1, 5)
        grid = compute_one_through_four_grid()
        display = UniversalPositionDisplay()
        text_elements = [
            Text(2, 2, "1"),
            Text(4, 2, "2"),
            Text(2, 4, "3"),
            Text(4, 4, "4"),
        ]
        assert_display_works_for_grid(self, grid, display, rectangle, text_elements)
        
    def test_display_with_one_by_two_grid(self):
        rectangle = Rectangle(1, 5, 1, 5)
        grid = compute_one_by_two_grid()
        display = UniversalPositionDisplay()
        text_elements = [
            Text(3, 2, "1"),
            Text(3, 4, "2")
        ]
        assert_display_works_for_grid(self, grid, display, rectangle, text_elements)
    
    def test_display_with_alphabet_grid(self):
        grid = AlphabetGridFactory().create_grid("")
        display = UniversalPositionDisplay()
        start = 0
        ending = 27
        rectangle = Rectangle(start, ending, start, ending)
        text_elements = []
        letters = compute_letter_list()
        for i in range(1, ending):
            for j in range(1, ending):
                text = letters[j - 1] + " " + letters[i - 1]
                text_elements.append(Text(i, j, text))
        assert_display_works_for_grid(self, grid, display, rectangle, text_elements)