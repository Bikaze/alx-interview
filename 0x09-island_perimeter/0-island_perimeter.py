#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in the grid.

    The grid is represented as a list of lists, where 0 represents water
    and 1 represents land. The cells are connected horizontally/vertically,
    and the grid is completely surrounded by water.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell initially
                perimeter += 4

                # Check the right neighbor
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

                # Check the bottom neighbor
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
