"""
Problem 5: How many routes are there through a 20x20 grid if you can only move right or down each time.

Algorithm: Dynamic Programming
"""

# a 20x20 grid actually has 21 vertices on either side
grid = [[None for i in range(21)] for j in range(21)]

# default values - starting from any vertex on the bottom row, there is only 1 path
for j in range(21):
    grid[20][j] = 1

for i in range(19, -1, -1):
    for j in range(20, -1, -1):

        # paths if went down
        num_of_paths = grid[i + 1][j]

        # make sure there is space to go to the right
        if j < 20:
            num_of_paths += grid[i][j + 1]

        grid[i][j] = num_of_paths

print(grid[0][0])
