"""
Problem 15: How many routes are there through a 20x20 grid if you can only move right or down each time.

Algorithm: Dynamic Programming
"""

# a 20x20 grid actually has 21 vertices on either side
grid = [[None for i in range(21)] for j in range(21)]

# default values - starting from any vertex on the bottom row, there is only 1 path (going right all the way)
for j in range(21):
    grid[20][j] = 1

# default values - starting from any vertex on the far left column, there is only 1 path (going down all the way)
for i in range(21):
    grid[i][20] = 1

# bottom up iterative code
for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

print(grid[0][0])
