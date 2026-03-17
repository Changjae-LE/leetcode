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





# ======================================================================
# 27. Remove Element
# Topic : Array, two pointers
# ======================================================================




# ======================================================================
# 28. Find the Index of the First Occurrence in a String
# Topic : string, index
# ======================================================================




# ======================================================================
# 66. Plus One
# Topic : list, plus
# ======================================================================






