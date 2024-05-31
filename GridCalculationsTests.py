from ..source.grid.GridCalculations import compute_grid_tree
from ..source.grid.Grid import Grid, RecursivelyDivisibleGridCombination
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

    def test_simple_combination_gives_both_grids(self):
        primary_simple_grid = SquareRecursiveDivisionGridFactory().create_grid("2")
        secondary_simple_grid = SquareRecursiveDivisionGridFactory().create_grid("3")
        combination = RecursivelyDivisibleGridCombination(primary_simple_grid, secondary_simple_grid)
        tree = compute_grid_tree(combination)
        self.assertTrue(tree.has_children() and len(tree.get_children()) == 1)
        self.assertEqual(tree.get_value(), primary_simple_grid)
        child = tree.get_children()[0]
        self.assertFalse(child.has_children())
        self.assertEqual(child.get_value(), secondary_simple_grid)