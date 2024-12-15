# -*- coding: utf-8 -*-
"""Day 12

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jzLyLVsMazC0VfjuVmwoRmqmsjw3XHGi
"""

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def get_neighbors(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def dfs(x, y, plant_type, grid, visited, rows, cols):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()
        area += 1
        local_perimeter = 0

        for nx, ny in get_neighbors(cx, cy):
            if is_valid(nx, ny, rows, cols):
                if grid[nx][ny] == plant_type and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    local_perimeter += 1
            else:
                local_perimeter += 1

        perimeter += local_perimeter

    return area, perimeter

def calculate_total_cost(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_cost = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = grid[i][j]
                area, perimeter = dfs(i, j, plant_type, grid, visited, rows, cols)
                total_cost += area * perimeter

    return total_cost

def main():
    file_path = '/content/input12par1.txt'
    grid = read_input(file_path)
    total_cost = calculate_total_cost(grid)
    print(total_cost)

if __name__ == '__main__':
    main()

import os
import sys
import collections

# Define the file path
if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    fname = '/content/input12part2.txt'
else:
    fname = '/content/input12part2.txt' if len(sys.argv) < 2 else sys.argv[1]

# Ensure file exists
if not os.path.exists(fname):
    raise FileNotFoundError(f"File {fname} does not exist.")

# Initialize variables
out = 0
grid = []
total = 0

# Read the file and populate the grid
with open(fname, 'r') as f:
    for line in f:
        line = line.strip()
        grid.append(line)
        total += len(line)

used = set()

# Define utility functions
def p(a, b):
    return (a[0] + b[0], a[1] + b[1])

def invert(a):
    return (a[1], a[0])

def neg(a):
    return (-a[0], -a[1])

# Main logic
while len(used) < total:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in used:
                current_region = set()
                borders = []
                num_borders = 0
                queue = [(i, j)]

                # BFS to find regions
                while queue:
                    n = queue.pop()
                    current_region.add(n)
                    ii, jj = n
                    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        iii, jjj = ii + d[0], jj + d[1]
                        if (iii < 0 or iii >= len(grid) or
                            jjj < 0 or jjj >= len(grid[iii]) or
                            grid[iii][jjj] != grid[i][j]):
                            borders.append(((iii, jjj), d))
                        elif (iii, jjj) not in queue and (iii, jjj) not in current_region:
                            queue.append((iii, jjj))

                # Process borders
                while borders:
                    pt, d = borders.pop()
                    flipped = invert(d)
                    pt2 = pt

                    while True:
                        pt2 = p(pt2, flipped)
                        if (pt2, d) in borders:
                            borders.remove((pt2, d))
                        else:
                            break

                    pt2 = pt
                    while True:
                        pt2 = p(pt2, neg(flipped))
                        if (pt2, d) in borders:
                            borders.remove((pt2, d))
                        else:
                            break

                    num_borders += 1

                out += len(current_region) * num_borders
                for n in current_region:
                    used.add(n)

# Output the result
print(out)
