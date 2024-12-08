#!/usr/bin/python3
"""Finding the area of an island"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int):

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for the cell
                perimeter += 4

                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove shared sides with the cell above

                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
