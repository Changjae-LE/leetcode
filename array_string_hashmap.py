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
# Time Complexity: O(n)
# Space Complexity: O(1)
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
        #c_dict = defaultdict(int)
        #for c in s:
        #    c_dict[c] += 1
        
        #for i in range(len(s)):
        #    if c_dict[s[i]] == 1:
        #        return i
        
        #return -1
    
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

# ========================================================
# String : 2 questions
# ========================================================

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

# 424. Longest Repeating Character Replacement (Medium)

class Solution:
    def characterReplacement(self, s, k):
        freq = {}
        l = 0
        max_freq = 0
        result = 0

        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0) + 1

            max_freq = max(max_freq, freq[c])

            while (r - l + 1) - max_freq > k:
                left_c = s[l]
                freq[left_c] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result

# ========================================================
# Hashmap : 3 questions
# ========================================================

# 347. Top K Frequent Elements (Medium)

class Solution:
    def topKFrequent(self, nums, k):
        #dic_nums = {}
        #for num in nums:
        #    if num not in dic_nums:
        #        dic_nums[num] = 1
        #    else:
        #        dic_nums[num] += 1


        #bucket = [[] for _ in range(len(nums)+1)]# 2. bucket <- value, frequency
        #for num, freq in dic_nums.items():
        #    bucket[freq].append(num)
        
        #res = []
        #for i in range(len(bucket)-1, 0, -1):
        #    for num in bucket[i]:
        #        res.append(num)
        #        if len(res) == k:
        #            return res

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]

        return [n[0] for n in freq][:k]

# 560. Subarray Sum Equals K (Medium)

class Solution:
    def subarraySum(slef, nums, k):
        #prefix_dict = {0: 1}
        #count = 0
        #prefix = 0

        #for i in range(len(nums)):
        #    prefix += nums[i]

        #    need = prefix - k
        #    if need in prefix_dict:
        #        count += prefix_dict[need]
        #    if prefix in prefix_dict:
        #        prefix_dict[prefix] += 1
        #    else:
        #        prefix_dict[prefix] = 1
        #return count
        
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # base case
        for num in nums:
            prefix += num
            count += freq[prefix - k]
            freq[prefix] += 1

        return count

# 49. Group Anagrams (Medium)

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