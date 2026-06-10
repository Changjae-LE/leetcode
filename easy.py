# ======================================================================
# 1. Two Sum
# Topic : list
# ======================================================================
# Time Complexity = O(n), Space Complexity = O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[v] = i
        return False

# ======================================================================
# 13. Roman to Integer
# Topic : string
# ======================================================================
class Solution:
    def romanToInt(self, s):
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100,"D":500, "M":1000}
        rst = 0

        for i in range(0, len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                rst -= roman[s[i]]
            else:
                rst += roman[s[i]]

        rst += roman[s[-1]]
        return rst
    
# ======================================================================
# 9. Palindrome Number
# Topic : string
# ======================================================================

# Solution 1
class Solution:
    def isPalindrome(self, x):
        if x < 0 or ( x % 10 == 0 and x != 0):
            return False

        half_reverse = 0
        while x > half_reverse:
            half_reverse = half_reverse * 10 + x % 10
            x = x // 10

        return (x == half_reverse) or (x == half_reverse // 10) #discard mid

# Solution 2
#class Solution:
#    def isPalindrome(self, x):
#        return str(x) == str(x)[::-1]


# ======================================================================
# 14. Longest Common Prefix
# Topic : string, Trie
# ======================================================================

class Solution:
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 1: return strs[0]

        rst = strs[0]
        for word in strs[1:]:
            i = 0
            while len(word) > i and len(rst) > i:
                if rst[i] != word[i]:
                    break
                i += 1
            rst = rst[:i]
        return rst

# ======================================================================
# 20. Valid Parentheses
# Topic : string, brackets, stack
# ======================================================================

class Solution:
    def isValid(self, s):
        dict_parent = {"(": ")", "{":"}", "[":"]"}

        stk = []
        for c in s:
            if c in dict_parent:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    temp = stk.pop()

                if c == dict_parent[temp]:
                    continue
                else:
                    return False

        return True if len(stk) == 0 else False


# ======================================================================
# 21. Merge Two Sorted Lists
# Topic : LinkedList
# ======================================================================
# Time Complexity: O(n + m), Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1, list2):
        
        dummy = head = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        dummy.next = list1 if list1 else list2

        return head.next



# ======================================================================
# 26. Remove Duplicates from Sorted Array
# Topic : Array, two pointers
# ======================================================================

class Solution:
    def removeDuplicates(self, nums):
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count


# ======================================================================
# 27. Remove Element
# Topic : Array, two pointers
# ======================================================================

class Solution:
    def removeElement(self, nums, val):

        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


# ======================================================================
# 28. Find the Index of the First Occurrence in a String
# Topic : string, index
# ======================================================================

class Solution:
    def strStr(self, haystack, needle):
        
        n = len(needle) -1
        for i in range(len(haystack) - n):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# ======================================================================
# 415. Add Strings
# Topic : list, string
# ======================================================================

class Solution:
    def addStrings(self, num1, num2):
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        rst = []

        while i>=0 or j>=0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            rst.append(str(total%10))

            i-=1
            j-=1

        return "".join(rst[::-1])
# ======================================================================
# 66. Plus One
# Topic : list, plus
# ======================================================================

class Solution:
    def plusOne(self, digits):
        
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0 #All digits are 9

        return [1] + digits



# ======================================================================
# 706. Design HashMap
# Topic : hash map
# ======================================================================

class MyHashMap:

    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1

# ======================================================================
# 217. Contains Duplicate
# Topic : List
# ======================================================================
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# ======================================================================
# 226. Invert Binary Tree
# Topic : Tree
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(log n)
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root
    
# ======================================================================
# 141. Linked List Cycle
# Topic : Linked list
# ======================================================================
    # solution1: Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def hasCycle(self, head):
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False
    
    # solution2: Floyd’s Cycle Detection Algorithm
    # Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    

# ======================================================================
# 70. Climbing Stairs
# Topic : Dynamic Programming
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def climbStairs(self, n):
        stair_list = [0, 1, 2]
        if n <= 2:
            return stair_list[n]

        for i in range(3, n+1):
            stair_list.append(stair_list[i-1] + stair_list[i-2])
        return stair_list[n]

# ======================================================================
# 104. Maximum Depth of Binary Tree
# Topic : Binary Tree
# ======================================================================
# Time Complexity: O(log n), Space Complexity: O(1)
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)

        return max(right, left) + 1

# ======================================================================
# 191. Number of 1 Bits
# Topic : Bit Manipulation
# ======================================================================
# Time Complexity: O(log n), Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n):
        count = 0

        while n:
            n &= n - 1 #Clears the rightmost 1 bit
            count += 1

        return count

# Time Complexity: O(log n), Space Complexity: O(log n)
class Solution:
    def hammingWeight(self, n):
        return bin(n).count("1")
    

# ======================================================================
# 190. Reverse Bits
# Topic : Bit Manipulation
# ======================================================================
# Time Complexity: O(1), Space Complexity: O(1)
class Solution:
    def reverseBits(self, n):
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result

# ======================================================================
# 100. Same Tree
# Topic : Tree
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(h)
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
# ======================================================================
# 242. Valid Anagram
# Topic : String
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

# ======================================================================
# 125. Valid Palindrome
# Topic : String
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s=re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]

# ======================================================================
# 20. Valid Parentheses
# Topic : String
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(n)

class Solution:
    def isValid(self, s):
        stk = []
        
        for c in s:
            if c in "({[":
                if c == "(":
                    stk.append(")")
                if c == "{":
                    stk.append("}")
                if c == "[":
                    stk.append("]")
            else:
                if stk:
                    temp = stk.pop()
                    if temp != c:
                        return False
                else:
                    return False
        if not stk:
            return True
        else:
            return False

# ======================================================================
# 572. Subtree of Another Tree
# Topic : Tree
# ======================================================================
# Time Complexity: O(n * m), Space Complexity: O(h_root + h_subRoot)

class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ======================================================================
# 268. Missing Number
# Topic : Array
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def missingNumber(self, nums):
        result = len(nums)

        for i in range(len(nums)):
            result ^= i
            result ^= nums[i]

        return result

# ======================================================================
# 206. Reverse Linked List
# Topic : Linked List
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def reverseList(self, head):
        prev = None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

# ======================================================================
# 338. Counting Bits
# Topic : Dynamic Programming, bits
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

# ======================================================================
# 217. Contains Duplicate
# Topic : Array
# ======================================================================
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    
# ======================================================================
# 252. Meeting Rooms
# Topic : Greedy
# ======================================================================
# Time Complexity: O(nlogn), Space Complexity: O(1)
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True
# ======================================================================
# 253. Meeting Rooms II
# Topic : Greedy
# ======================================================================
# Time Complexity: O(nlogn), Space Complexity: O(n)
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        starts = []
        ends = []

        for start, end in intervals:
            starts.append(start)
            ends.append(end)
        
        starts.sort()
        ends.sort()

        rooms = 0
        idx = 0

        for start in starts:
            if start < ends[idx]:
                rooms += 1
            else:
                idx += 1
        return rooms

# ======================================================================
# 704. Binary Search
# Topic : Binary Search
# ======================================================================
# Time Complexity: O(log n), Space Complexity: O(1)
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return -1

# ======================================================================
# 35. Search Insert Position
# Topic : Binary Search(lower bound)
# ======================================================================
# Time Complexity: O(log n), Space Complexity: O(1)
class Solution:
    def searchInsert(self, nums, target):
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] >= target:#target하고 같으면 오른쪽을 버린다.
                right = mid - 1
        return left

# ======================================================================
# 744. Find Smallest Letter Greater Than Target
# Topic : Binary Search
# ======================================================================
# Time Complexity: O(log n), Space Complexity: O(1)
class Solution:
    def nextGreatestLetter(self, letters, target):
        #upper bound

        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left % len(letters)]