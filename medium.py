# ======================================================================
# 15. 3Sum
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans

# ======================================================================
# 79. Word Search
# Topic : DFS, Backtracking
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def exist(self, board, word):

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, idx):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False
        if board[i][j] != word[idx] or board[i][j] == '*':
            return False
        if idx == len(word) - 1:
            return True
        
        cache = board[i][j]
        board[i][j] = '*'
        rst = self.dfs(board, word, i+1, j, idx+1) or \
            self.dfs(board, word, i-1, j, idx+1) or \
            self.dfs(board, word, i, j+1, idx+1) or \
            self.dfs(board, word, i, j-1, idx+1)
        board[i][j] = cache
        return rst
    
# ======================================================================
# 139. Word Break
# Topic : DP
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]


# ======================================================================
# 98. Validate Binary Search Tree
# Topic : DFS, BST
# ======================================================================

# Solution1: DFS
# Time Complexity: O(), Space Complexity: O()
    def isValidBST(self, root):
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, node, lower, upper):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        left_valid = self.dfs(node.left, lower, node.val)
        right_valid = self.dfs(node.right, node.val, upper)

        return left_valid and right_valid

# Solution2: Inorder
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def isValidBST(self, root):
        rst = []
        self.inOrder(root, rst)

        for i in range(1, len(rst)):
            if rst[i-1] >= rst[i]:
                return False
        return True
        
        
    def inOrder(self, root, rst):
        if not root:
            return False
        self.inOrder(root.left, rst)
        rst.append(root.val)
        self.inOrder(root.right, rst)


# ======================================================================
# 36. Valid Sudoku
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution(object):
    def isValidSudoku(self, board):
        seen = []

        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value != '.':
                    seen += [
                        (value, col_index),
                        (row_index, value),
                        (row_index // 3, col_index // 3, value)
                    ]

        return len(seen) == len(set(seen))