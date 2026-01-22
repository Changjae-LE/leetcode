"""
- Array
- String
- Hashmap

"""


# ========================================================
# Array : 5 questions
# ========================================================

# 1. Two Sum (Easy)

class Solution:
    def twoSum(self, nums, target):
        
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
            
# 26. Remove Duplicates from Sorted Array (Easy)

class Solution:
    def removeDuplicates(self, nums):
        
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
                
        return count

# 121. Best Time to Buy and Sell Stock (Easy)

class Solution:
    def maxProfit(self, nums):
        
        min_price = 10000
        max_profit = 0

        for price in nums:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
    
# 209. Minimum Size Subarray Sum (Medium)

class Solution:
    def minSubArrayLen(self, nums, target):
        
        left = 0
        current_sum = 0
        window_min = 10000000

        for right in range(len(nums)):
            current_sum += nums[right]
            while target <= current_sum:
                window_min = min(window_min, right - left + 1)
                current_sum -= nums[left]
                left += 1


        if window_min ==  10000000:
            return 0
        
        
        return window_min

# 387. First Unique Character in a String (Easy)

class Solution:
    def firstUniqChar(self, s):
        dic_s={}
        dic_s = {}

        for c in s:
            if c in dic_s:
                dic_s[c] += 1
            else:
                dic_s[c] = 1

        for i, c in enumerate(s):
            if dic_s[c] == 1:
                return i

        return -1

# 125. Valid Palindrome (Easy)

class Solution:
    def isPalindrome(self, s):
        
        #filtered = []
        #for c in s:
        #    if c.isalnum():
        #        filtered.append(c.lower())

        #return filtered == filtered[::-1]


        s = s.lower()
        s = re.sub('[^0-9a-z]', "", s)
        return s == s[::-1]














