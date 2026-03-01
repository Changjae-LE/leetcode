"""
- Dynamic Programming

"""

# ========================================================
# Dynamic Programming : 5 questions
# ========================================================

# 70. Climbing Stairs (Easy)
# Time Complexity = O(n)
# Space Complexity = O(n)
# Recurrence relation: dp[i] = dp[i-1] + dp[i-2]

# CREATE array dp
# dp[0] <- 0, dp[1] <- 1, dp[2] <- 2
# IF n < 3 THEN
#   RETURN dp[n]
# For i <- 3 TO DO
#   dp[i] <- dp[i-1] + dp[i-2]
#   RETURN dp[n]

class Solution:
    def climbStairs(self, n):
        
        array = [0, 1, 2]
        if n < 3:
            return array[n]
        
        for i in range(3, n+1):
            array.append(array[i-1] + array[i-2])

        return array[n]

# 53. Maximum Subarray (Medium)
# Time Complextity: O(n)
# Space Complexity: O(1)
# Recurrence relation: dp[i]=max(nums[i], dp[i−1]+nums[i])

# FUNCTION maxSubArray(nums)
#   max_sub ← nums[0]
#   best ← nums[0]
#   FOR i<-1 to length(nums) DO
#       max_sub <- MAX(max_sub + nums[i], nums[i])
#       best <- MAX(best, max_sub)
#       RETURN best

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = -9999999
        best = -9999999
        for n in nums:
            max_sub = max(max_sub + n, n)
            best=max(max_sub, best)
        return best

# 121. Best Time to Buy and Sell Stock (Medium)
# Time Complextity: O(n)
# Space Complexity: O(1)
# Recurrence relation: min_price[i] = min(min_price[i-1], price[i])
# Recurrence relation: dp[i] = Max(dp[i-1], price[i]-min_price[i-1])


# FUNCTION maxProfit(prices)
#   min_price <- prices[0]
#   max_profit <- 0
#   FOR i <- 1 TO length(prices) -1 DO
#       min_price <- MIN(min_price, prices[i])
#       max_profit <- MAX(max_profit, prices[i] - min_price)
#   END FOR
#   RETURN max_profit

class Solution:
    def maxProfit(self, prices):
        
        min_price = 10000
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

# 62. Unique Paths (Medium)
# Time Complextity: O(mn)
# Space Complexity: O(mn)
# Recurrence relation: dp[i][j] = dp[i-1][j] + dp[i][j-1]

# FUNCTION uniquePaths(m, n)
#   CREATE 2D array dp of size m x n
#   INITIALIZE all cells to 1
#   FOR i <- 1 TO m-1 DO
#       FOR j <- 1 TO n-1 DO
#           dp[i][j] <- dp[i-1][j] + dp[i][j-1]
#        END FOR
#   END FOR
#   RETURN dp[m-1][n-1]

class Solution:
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

# 322. Coin Change (Medium)
# Time Complexity: O(amount x k)
# Space Complexity: O(amount)
# Recurrence relation: dp[i] = min(dp[i], dp[i - coin] + 1)

#   FUNCTION coinChange(coins, amount)
#   CREATE 2D array dp of size m x n
#   INITIALIZE all cells to ∞
#   dp[0] <- 0
#   FOR i <- TO amount DO
#       FOR each coin IN coins DO
#           IF i - coin >= 0 THEN
#               dp[i] <- MIN(dp[i], dp[i-coin] +1)
#           END IF
#       END FOR
#   END FOR
#   IF dp[amount] == +∞ THEN RETURN -1
#   ELSE THEN dp[amount]
#   END IF
class Solution:
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1
    
# 300. Longest Increasing Subsequence (Medium)
# Recurrence:
# dp[i] = 1 + max(dp[j])
# where 0 <= j < i and nums[j] < nums[i]
class Solution(object):
    def lengthOfLIS(self, nums):

        tails = []
        for x in nums:
            i = bisect_left(tails, x)  # 첫 >= x 위치
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)




# 1143. Longest Common Subsequence (Medium)
# Time Complexity: O(mn)
# Space Complexity: O(mn)

#pseudo code
# m <- length(text1)
# n <- length(text2)
# dp <- array of size m x n, filled with 0
# For i = 1 TO m:
#   For j = 1 TO n+1:
#       IF text[i-1] == text[j-1] DO
#           dp[i][j] <- dp[i-1][j-1] + 1
#       ELSE:
#           dp[i][j] <- MAX(dp[i-1][j], dp[i][j-1])
#       END IF
#   END FOR
# END FOR
# RETURN dp[m][n]

#recurrence:
# If text1[i-1] == text2[j-1]:
#     dp[i][j] = dp[i-1][j-1] + 1
# Else:
#     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

# 139. Word Break (Medium)
class Solution(object):
    def wordBreak(self, s, wordDict):
        
        wordSet = set(wordDict)
        dp = [True]

        for i in range(1, len(s) + 1):
            dp.append(any(dp[j] and s[j:i] in wordSet for j in range(i)))

        return dp[-1]

# 198. House Robber (Medium)
class Solution(object):
    def rob(self, nums):

        bf2, adj = 0, 0
        for cur in nums:
            bf2, adj = adj, max(bf2 + cur, adj)

        return adj


# 213. House Robber II (Medium)
class Solution():
    def rob(self, nums):

        def simple(arr):
            prev2, prev1 = 0, 0
            for x in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1

        if len(nums) <= 1:
            return sum(nums)

        return max(simple(nums[1:]), simple(nums[:-1]))


# 91. Decode Ways (Medium)



# 55. Jump Game (Medium)