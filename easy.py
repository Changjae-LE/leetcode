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

