"""
Problem 67: Find sum of max path from the top of pyramid to bottom if with every move, you can only move to adjacent
numbers on the next row.

Algorithm: Dynamic Programming
"""

with open("./resources/67.txt") as f:
    string = f.read().strip()

grid = [[int(i) for i in j.split(" ")] for j in string.split("\n")]

# update the grid, grid[i][j] will represent max value path from i,j to bottom of pyramid, bottom up approach
for i in range(98, -1, -1):
    for j in range(i, -1, -1):
        grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])

print(grid[0][0])
