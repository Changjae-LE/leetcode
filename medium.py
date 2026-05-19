# ======================================================================
# 15. 3Sum
# Topic : Array
# ======================================================================
# Time Complexity: O(n^2), Space Complexity: O(1)
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        rst = []
        
        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    rst.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return rst