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
        dp = [False] * (target + 1) # 해당하는 값을 만들 수 있는지
        dp[0] = True

        for num in nums: # 해당 num을 넣었을 때
            for s in reversed(range(num, target+1)):#만들수 이는 값은 num~target 사이의 값이다.
                dp[s] = dp[s] or dp[s-num]#만약 num을 더했을 때 s가 되는 값이 True라면 True
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
                for j in reversed(range(ones, n+1)):#0을 i개, 1을 j개까지 쓸 수 있을 때, 만들 수 있는 문자열 최대 개수
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)#해당 문자열을 쓰는 경우와 안쓰는 경우
            

        return dp[m][n]
    


# ======================================================================
# 526. Beautiful Arrangement
# Topic : DP
# ======================================================================

class Solution:
    def countArrangement(self, n):
        used = [False] * (n + 1)
        return self.backtrack(1, n, used)
        

    def backtrack(self, idx, n, used):
        if idx > n:
            return 1

        count = 0

        for num in range(1, n + 1):
            if not used[num] and (num % idx == 0 or idx % num == 0):
                used[num] = True
                count += self.backtrack(idx + 1, n, used)
                used[num] = False

        return count
# ======================================================================
# 49. Group Anagrams
# Topic: Hashmap
# ======================================================================
class Solution:
    def groupAnagrams(self, strs):
        str_dict = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in str_dict:
                str_dict[key].append(s)
            else:
                str_dict[key] = [s]
        return list(str_dict.values())
    
# ======================================================================
# 347. Top K Frequent Elements (Medium)
# Topic: Hashmap
# ======================================================================

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]

        return [n[0] for n in freq][:k]

