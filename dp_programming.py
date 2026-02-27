"""
- Dynamic Programming

"""

# ========================================================
# Dynamic Programming : 5 questions
# ========================================================

# 70. Climbing Stairs (Easy)
# Time Complexity = O(n)
# Space Complexity = O(n)

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
    

