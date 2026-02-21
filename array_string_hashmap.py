"""
- Array
- String
- Hashmap

"""
#from collections import Counter, defaultdict
#import re

# ========================================================
# Array : 5 questions
# ========================================================

# 1. Two Sum (Easy)
# Time Complexity: O(nlogn)

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
# Time Complexity: O(n)

class Solution:
    def removeDuplicates(self, nums):
        
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
                
        return count

# 121. Best Time to Buy and Sell Stock (Easy)
# Time Complexity: O(n)
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
# Time Complexity: O(n)
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
    
# 217. Contains Duplicate (Easy)

class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
    
# 238. Product of Array Except Self (Medium)

class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        rst = [1] * n

        for i in range(1, len(nums)):
            rst[i] *= rst[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            rst[i] *= suffix
            suffix *= nums[i]

        return rst

# 53. Maximum Subarray (Medium)

class Solution:
    def maxSubArray(self, nums):
        cur = max_v = nums[0]
        for num in nums[1:]:
            cur = max(num, cur+num)
            max_v = max(cur, max_v)
        return max_v


# 152. Maximum Product Subarray (Medium)

class Solution:
    def maxProduct(self, nums):

        cur_max = cur_min = max_val = nums[0]
        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            max_val = max(max_val, cur_max)
        return max_val

# 153. Find Minimum in Rotated Sorted Array (Medium)

class Solution:
    def findMin(self, nums):
        
        left = 0
        right = len(nums) - 1

        while left < right:#정렬이 되어 있는 곳을 버림
            mid = (right + left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# 33. Search in Rotated Sorted Array (Medium)

class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
    
# 15. 3Sum (Medium)
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # i 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 정렬되어 있으니 nums[i] > 0이면 이후는 전부 >0 => 합 0 불가
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # left 중복 제거
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # right 중복 제거
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res

# 11. Container With Most Water (Medium)

# ========================================================
# String : 4 questions
# ========================================================

# 125. Valid Palindrome (Easy)
# Time Complexity: O(n)

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
# Time Complexity: O(n)

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
    
# 242. Valid Anagram (Easy)
# Time Complexity: O(n)

class Solution(object):
  def isAnagram(self, s, t):

#        if len(s) != len(t):
#            return False

#        for char in set(s):
#            if s.count(char) != t.count(char):
#                return False
#        return True

    return Counter(s) == Counter(t)
  

# 20. Valid Parentheses (Easy)
# Time Complexity: O(n)

class Solution(object):
    def isValid(self, s):

        stk = []

        for c in s:
            if c in "{([":
                stk.append(c)
            else:
                if not stk\
                or stk[-1] == '{' and c != '}' \
                or stk[-1] == '[' and c != ']' \
                or stk[-1] == '(' and c != ')':
                    return False
                stk.pop()
        return not stk

# ========================================================
# Hashmap : 3 questions
# ========================================================

# 347. Top K Frequent Elements (Medium)
# Time Complexity: O(nlogn)

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
# Time Complexity: O(n)

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
# Time Complexity: O(n·mlogm)

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

# 819. Most Common Word (Medium)
# Time Complexity: O(n)

class Solution:
    def mostCommonWord(self, paragraph, banned):
        #banned = set(w.lower() for w in banned)
        words = re.findall("[a-z]+", paragraph.lower())
        counts = Counter(word for word in words if word not in banned)
        return counts.most_common(1)[0][0]


# ========================================================
# Linked List : 6 questions
# ========================================================

# 206. Reverse Linked List (Easy)

class Solution(object):
    def reverseList(self, head):

        prev = None
        while head:
            next_p = head.next
            head.next = prev
            prev = head
            head = next_p

        return prev


# 141. Linked List Cycle (Easy)

class Solution:
    def hasCycle(self, head):

        try:
            t = head
            r = head.next
            while t is not r:
                t = t.next
                r = r.next.next
            return True

        except:
            return False

# 21. Merge Two Sorted Lists (Easy)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        head = dummy = ListNode(-1)

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        dummy.next = list1 if list1 else list2

        return head.next