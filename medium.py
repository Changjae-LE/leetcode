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



# ======================================================================
# 46. Permutations
# Topic : DFS
# ======================================================================

class Solution:
    def permute(self, nums):
        rst = []
        seen = [0] * len(nums)
        self.dfs(nums, rst, [], seen)
        return rst


    def dfs(self, nums, rst, path, seen):
        if len(nums) == len(path):
            rst.append(path[:])
            return

        for i in range(len(nums)):
            if seen[i] == 0:
                path.append(nums[i])
                seen[i] = 1
                self.dfs(nums, rst, path, seen)
                path.pop()
                seen[i] = 0

# ======================================================================
# 416. Partition Equal Subset Sum
# Topic : DP
# ======================================================================

class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in reversed(range(num, target+1)):
                dp[s] = dp[s] or dp[s-num]
                if dp[target]:
                    return True

        return False


# ======================================================================
# 474. Ones and Zeroes
# Topic : DP
# ======================================================================

class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            for i in reversed(range(zeros, m+1)):
                for j in reversed(range(ones, n+1)):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
            

        return dp[m][n]