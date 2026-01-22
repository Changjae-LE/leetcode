# ========================================================
# Array : 5 questions
# ========================================================

# 1. Two Sum (Easy)

class Solution:
    def twoSum(self, nums, target):
        # Store the original index with each value as a tuple (value, index)
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort()

        l = 0
        r = len(arr)-1
        while 1:
            if arr[l][0] + arr[r][0] > target:
                r -= 1
            elif arr[l][0] + arr[r][0] < target:
                l += 1
            else:
                return [arr[l][1], arr[r][1]]