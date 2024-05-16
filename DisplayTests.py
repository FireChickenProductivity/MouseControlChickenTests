from ..source.display.UniversalDisplays import UniversalPositionDisplay
from ..source.GridFactory import SquareRecursiveDivisionGridFactory
from ..source.display.Canvas import Canvas
from ..source.grid.Grid import Rectangle
import unittest

def compute_one_through_four_grid():
    return SquareRecursiveDivisionGridFactory().create_grid("2")

class UniversalPositionDisplayTest(unittest.TestCase):
    def test_display_with_one_through_four_grid(self):
        rectangle = Rectangle(1, 1, 5, 5)
        grid = compute_one_through_four_grid()
        grid.make_around(rectangle)
        display = UniversalPositionDisplay()
        display.set_rectangle(rectangle)
        canvas = Canvas()
        display.set_grid(grid)
        display.draw_on(canvas)

        