"""
- Graphs
- Backtracking

"""


# ========================================================
# Graphs : 5 questions
# ========================================================

# 200. Number of Islands (Medium)

class Solution(object):
    def numIslands(self, grid):
        
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != '1':
                return
            
            grid[row][col] = '0'
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    cnt += 1

        return cnt

# 994. Rotting Oranges (Medium)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = set()
        rotten = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        cnt = 0
        while fresh and rotten:
            for _ in range(len(rotten)):
                i, j = rotten.pop(0)
                for xy in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                    if xy in fresh:
                        fresh.remove(xy)
                        rotten.append(xy)
            cnt += 1

        return -1 if fresh else cnt