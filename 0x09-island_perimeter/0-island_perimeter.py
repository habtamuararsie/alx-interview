#!/usr/bin/python3
""""
Solution module for island perimeter
"""


def island_perimeter(grid):
    
    """"
    A function which calculats and return the perimeter
    of island in given grid
    """
    width = len(grid[0])
    height = len(grid)
    perimeter = 0
    for a in range(height):
        for b in range(width):
            if grid[a][b] == 1:
                perimeter += 4
                if a > 0 and grid[a - 1][b] == 1:
                    perimeter -= 2
                if b > 0 and grid[a][b - 1] == 1:
                    perimeter -= 2
    return perimeter