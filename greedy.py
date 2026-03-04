# 55. Jump Game (Medium)
class Solution:
    def canJump(self, nums):    
        last = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0

class Solution:
    def canJump(self, nums):
        farthest = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last:
                return True

        return True
# 435. Non-overlapping Intervals

# 253. Meeting Rooms II

# 134.