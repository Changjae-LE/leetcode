# ======================================================================
# 688. Knight Probability in Chessboard
# Topic : DP, Probability
# ======================================================================

class Solution:
    def knightProbability(self, n, k, row, column):
        directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]

        dp = [[0] * n for _ in range(n)]

        dp[row][column] = 1

        for _ in range(k):
            next_dp = [[0] * n for _ in range(n)]

            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in directions:
                            n_r, n_c = r+ dr, c+dc
                            if 0 <= n_r < n and 0 <= n_c < n:
                                next_dp[r+ dr][c+dc] += dp[r][c]/8
            dp = next_dp

        return sum(map(sum, dp))
    

# ======================================================================
# 200. Number of Islands
# Topic : DP, DFS
# ======================================================================

class Solution:
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):

        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == '0':
            return

        if grid[i][j] == '1':
            grid[i][j] = '0'

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)