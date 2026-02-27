"""
- binary
- Backtracking

"""

# ========================================================
# binary : 5 questions
# ========================================================

# 191. Number of 1 Bits (Easy)

class Solution(object):
    def hammingWeight(self, n):

        cnt = 0
        while n != 0:
            n &= (n-1)
            cnt += 1
        return cnt
    
# 268. Missing Number (Easy)

class Solution(object):
    def missingNumber(self, nums):

        sums = sum(range(len(nums)+1))
        return sums - sum(nums)

# 70. Climbing Stairs (Easy)

class Solution(object):
    def climbStairs(self, n):

        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)

        for i in range(3, n+1):
            dp.append(dp[i-2] + dp[i-1])
        return dp[n]
    

# ========================================================
# Interval : 5 questions
# ========================================================



# ========================================================
# Dynamic Programming : 5 questions
# ========================================================

class Solution(object):
    def climbStairs(self, n):

        if n <= 3:
            return n

        dp = [0,1,2]

        for i in range(3, n+1):
            dp.append(dp[i-2]+dp[i-1])

        return dp[-1]