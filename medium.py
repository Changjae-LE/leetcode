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


# ======================================================================
# 79. Word Search
# Topic : DFS, Backtracking
# ======================================================================
# Time Complexity: O(n^2), Space Complexity: O(1)
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