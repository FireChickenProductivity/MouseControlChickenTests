from ..source.grid.GridCalculations import compute_grid_tree
from ..source.grid.Grid import Grid, RecursivelyDivisibleGridCombination
from ..source.grid.ReverseCoordinateDoublingGrid import ReverseCoordinateHorizontalDoublingGrid
from ..source.grid.RecursiveDivisionGrid import RectangularRecursiveDivisionGrid
from ..source.GridFactory import SquareRecursiveDivisionGridFactory

import unittest

def create_simple_combination_of_combinations_with_grids():
    simple_grids = [SquareRecursiveDivisionGridFactory().create_grid(str(i)) for i in range(2, 6)]
    primary_combination = RecursivelyDivisibleGridCombination(simple_grids[0], simple_grids[1])
    secondary_combination = RecursivelyDivisibleGridCombination(simple_grids[2], simple_grids[3])
    return RecursivelyDivisibleGridCombination(primary_combination, secondary_combination), simple_grids

def assert_combination_of_combinations_matches_expected(testing_class, tree, simple_grids):
    for i in range(3):
        testing_class.assertTrue(tree.has_children())
        testing_class.assertTrue(len(tree.get_children()) == 1)
        testing_class.assertEqual(tree.get_value(), simple_grids[i])
        tree = tree.get_children()[0]
    testing_class.assertFalse(tree.has_children())
    testing_class.assertEqual(tree.get_value(), simple_grids[-1])

def compute_simple_combination_types(combination):
    main_type = type(combination)
    primary_type = type(combination.get_primary_grid())
    secondary_type = type(combination.get_secondary_grid())
    return main_type, primary_type, secondary_type

def simple_combination_matches(actual, expected):
    expected_types = compute_simple_combination_types(expected)
    actual_types = compute_simple_combination_types(actual)
    return expected_types == actual_types

def compute_simple_doubling_types(doubling):
    main_type = type(doubling)
    primary_type = type(doubling.get_primary_grid())
    secondary_type = type(doubling.get_secondary_grid())
    return main_type, primary_type, secondary_type

def simple_doubling_matches(actual, expected):
    expected_types = compute_simple_doubling_types(expected)
    actual_types = compute_simple_doubling_types(actual)
    return expected_types == actual_types

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
    
    def test_simple_doubling_gives_both_grids(self):
        simple_grid = SquareRecursiveDivisionGridFactory().create_grid("2")
        doubling = ReverseCoordinateHorizontalDoublingGrid(simple_grid)
        tree = compute_grid_tree(doubling)
        self.assertTrue(tree.has_children())
        self.assertTrue(len(tree.get_children()) == 2)
        self.assertEqual(tree.get_value(), doubling)
        for child in tree.get_children():
            self.assertFalse(child.has_children())
            value_type = type(child.get_value())
            self.assertEqual(value_type, RectangularRecursiveDivisionGrid)

    def test_combination_of_combinations_gives_all_grids(self):
        combination, simple_grids = create_simple_combination_of_combinations_with_grids()
        tree = compute_grid_tree(combination)
        assert_combination_of_combinations_matches_expected(self, tree, simple_grids)
    
    def test_doubling_of_combinations_gives_all_grids(self):
        combination, simple_grids = create_simple_combination_of_combinations_with_grids()
        doubling = ReverseCoordinateHorizontalDoublingGrid(combination)
        tree = compute_grid_tree(doubling)
        self.assertTrue(len(tree.get_children()) == 2)
        primary_child = tree.get_children()[0]
        assert_combination_of_combinations_matches_expected(self, primary_child, simple_grids)
        secondary_simple_grids = []
        secondary_grid = doubling.get_secondary_grid()
        for combination_grid in [secondary_grid.get_primary_grid(), secondary_grid.get_secondary_grid()]:
            for simple_grid in [combination_grid.get_primary_grid(), combination_grid.get_secondary_grid()]:
                secondary_simple_grids.append(simple_grid)
        secondary_child = tree.get_children()[1]
        assert_combination_of_combinations_matches_expected(self, secondary_child, secondary_simple_grids)
        
    def test_combination_of_doublings_gives_all_grids(self):
        simple_grids = [SquareRecursiveDivisionGridFactory().create_grid(str(i)) for i in range(2, 4)]
        doublings = [ReverseCoordinateHorizontalDoublingGrid(grid) for grid in simple_grids]
        combination = RecursivelyDivisibleGridCombination(doublings[0], doublings[1])
        tree = compute_grid_tree(combination)
        self.assertEqual(len(tree.get_children()), 2)
        for child in tree.get_children():
            self.assertEqual(len(child.get_children()), 1)
            for grandchild in child.get_children():
                self.assertEqual(len(grandchild.get_children()), 2)
                for great_grandchild in grandchild.get_children():
                    self.assertEqual(len(great_grandchild.get_children()), 0)
        self.assertEqual(tree.get_value(), doublings[0])
        primary_child = tree.get_children()[0]
        self.assertEqual(primary_child.get_value(), simple_grids[0])
        secondary_child = tree.get_children()[1]
        self.assertEqual(secondary_child.get_value(), doublings[0].get_secondary_grid())
        primary_instance_of_secondary_doubling_node = primary_child.get_children()[0]
        primary_instance_of_secondary_doubling = primary_instance_of_secondary_doubling_node.get_value()
        self.assertEqual(primary_instance_of_secondary_doubling, doublings[1])
        secondary_instance_of_secondary_doubling_node = secondary_child.get_children()[0]
        secondary_instance_of_secondary_doubling = secondary_instance_of_secondary_doubling_node.get_value()
        self.assertTrue(simple_combination_matches(secondary_instance_of_secondary_doubling, doublings[1]))
        primary_secondary_doubling_primary_child = primary_instance_of_secondary_doubling_node.get_children()[0]
        self.assertEqual(primary_secondary_doubling_primary_child.get_value(), simple_grids[1])
        primary_secondary_doubling_secondary_child = primary_instance_of_secondary_doubling_node.get_children()[1]
        self.assertEqual(primary_secondary_doubling_secondary_child.get_value(), doublings[1].get_secondary_grid())
        secondary_secondary_doubling_grid = secondary_instance_of_secondary_doubling_node.get_children()[0].get_value()
        self.assertTrue(simple_doubling_matches(secondary_secondary_doubling_grid, doublings[1]))
    
        

