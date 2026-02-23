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
# Space Complexity: O(n)


# Pseudo code
# arr <- (value, index) pairs in nums
# arr.sort()
# right = len(nums) - 1, left = 0
# while left < right:
#   if sum of left and right == target: return original indices
#   if sum > target: right -= 1
#   if sum < target: left += 1


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
# Space Complexity: O(1)

# Pseudo code
# cnt = 1
# for from 1 to len(nums):
#   if nums[i] != nums[i-1]: nums[count] = nums[i], cnt += 1
# return cnt
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

# Pseudo Code
#for price in prices:
#   if price is low: update min_price
#   else price is high: Update max_profit(price - min_price)
#if min_price == original value: return 0
#return max_profit
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
# Space Complexity: O(n)

# Pseudo Code
# freq ← empty map
# for c in s: count frequency
# for from 0 to len(s): to find non-repeating character
#   if dic[s[i]] == 1: return i

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
    
        #cnt = Counter(s)
        #for i in range(len(s)):
        #    if cnt[s[i]] == 1:
        #        return i

        #return -1

    
# 217. Contains Duplicate (Easy)
# Time Complexity: O(n)
# Space Complexity: O(n)

# convert nums to a set
# compare the size of array with set(array)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
    
# 238. Product of Array Except Self (Medium)

class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        rst = [1] * n

        for i in range(1, len(nums)):
            rst[i] = rst[i-1] * nums[i-1]
        
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

        cur_max = nums[0]
        cur_min = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])
            best = max(best, cur_max)
        return best

# 153. Find Minimum in Rotated Sorted Array (Medium)

class Solution:
    def findMin(self, nums):
        
        left = 0
        right = len(nums) - 1

        while left < right:#정렬이 되어 있는 곳을 버림
            mid = (right + left)//2
            if nums[mid] > nums[right]:
                left = mid + 1#nums[mid] cannot be the min value
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

class Solution:
    def maxArea(self, height):

        right = len(height) - 1
        left = 0
        best = 0
        while left < right:
            width = right - left
            vol = min(height[right], height[left]) * width
            best = max(vol, best)
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1

        return best

# ========================================================
# String : 4 questions
# ========================================================

# 125. Valid Palindrome (Easy)
# Time Complexity: O(n)
# Space Complexity: O(n)

# s <- lowercase
# s <- remove special characters and empty space from s
# return s == s[::-1]
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

        freq = defaultdict(int)
        max_freq = 0
        left = 0
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
# 242. Valid Anagram (Easy)
# Time Complexity: O(n)
# Space Complexity: O(n)

# freq1 <- frequency map of s
# freq2 <- frequency map of t
# return freq1 == freq2

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
# Space Complexity: O(n)

# stack <- empty list
# for each character c in s:
#       if c is one of "({[":
#           push c onto stack 
#       else:
#           if stack is empty:
#               return False
#           if Top of the stack does not match c:
#               return False
#           pop from stack
# return stack is empty

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

# 3. Longest Substring Without Repeating Characters (Medium)
class Solution:
    def lengthOfLongestSubstring(self, s):

        max_len = 0
        idx = {}

        left = 0
        for right in range(len(s)):
            if s[right] in idx:
                left = max(left, idx[s[right]])
            max_len = max(max_len, right-left+1)
            idx[s[right]] = right+1

        return max_len
    
# 647. Palindromic Substrings (Medium)
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def countSubstrings(self, s):
        n = len(s)
        cnt = 0
        for i in range(len(s)):
            cnt += self.expend(s, i, i)#odd
            cnt += self.expend(s, i, i+1)#even
        return cnt

    def expend(self, s, left, right):
        cnt = 0
        while 0 <= left and right < len(s) and s[left] == s[right]:
            cnt += 1
            left -=1
            right +=1
        return cnt

# 5. Longest Palindromic Substring
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s

        best_l, best_r = 0, 0

        for i in range(n):
            # odd
            l1, r1 = self.expand(s, i, i)
            if r1 - l1 > best_r - best_l:
                best_l, best_r = l1, r1

            # even
            l2, r2 = self.expand(s, i, i + 1)
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2

        return s[best_l:best_r + 1]

    def expand(self, s, l, r):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1

        return l + 1, r - 1


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

        #words = re.findall("[a-z]+", paragraph.lower())
        #words = [word for word in words if word not in banned]
        #words_dict = Counter(words)
        #freq = [(v, i) for i, v in words_dict.items()]
        #freq.sort()
        #return freq[-1][1]
        
        words = re.findall("[a-z]+", paragraph.lower())
        counts = Counter(word for word in words if word not in banned)
        return counts.most_common(1)[0][0]

# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s, p):
        
        n = len(s)
        m = len(p)

        
        window = Counter(s[:m])
        need= Counter(p)
        rst = []

        if window == need:
            rst.append(0)

        for right in range(m, n):
            window[s[right]] += 1
            window[s[right-m]] -= 1
            if window[s[right-m]] == 0:
                del window[s[right-m]]

            if window == need:
                rst.append(right - m + 1)
        return rst


# ========================================================
# Linked List : 6 questions
# ========================================================

# 206. Reverse Linked List (Easy)
#Time Complexity = O(n)
#Space Complexity = O(1)

#prev ← null
#while head is not null:

#    next ← head.next
#    head.next ← prev
#    prev ← head
#    head ← next
#return prev

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