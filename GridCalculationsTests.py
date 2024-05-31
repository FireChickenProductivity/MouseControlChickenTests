from ..source.grid.GridCalculations import compute_grid_tree
from ..source.grid.Grid import Grid
from ..source.grid.ReverseCoordinateDoublingGrid import ReverseCoordinateDoublingGrid
from ..source.GridFactory import SquareRecursiveDivisionGridFactory

import unittest

class ComputeGridTreeTests(unittest.TestCase):
    def test_simple_grid_gives_grid(self):
        factory = SquareRecursiveDivisionGridFactory()
        simple_grid = factory.create_grid("2")
        tree = compute_grid_tree(simple_grid)
        self.assertFalse(tree.has_children())
        self.assertEqual(tree.get_value(), simple_grid)

