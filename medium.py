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
        return self.dfs(root, float("+inf"), float("-inf"))

    def dfs(self, root, upper, lower):
        if not root:
            return True
        
        if not lower < root.val < upper:
            return False

        return self.dfs(root.left, root.val, lower) and self.dfs(root.right, upper, root.val)

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


# ======================================================================
# 54. Spiral Matrix
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        res = []
        visited = set()

        y, x = 0, 0
        dy, dx = 0, 1

        for _ in range(R * C):
            res.append(matrix[y][x])
            visited.add((y, x))

            ny = y + dy
            nx = x + dx

            if not (0 <= ny < R and 0 <= nx < C) or (ny, nx) in visited:
                dy, dx = dx, -dy

            y += dy
            x += dx

        return res

# ======================================================================
# 73. Set Matrix Zeroes
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        row = [False] * R
        col = [False] * C
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        for i in range(R):
            for j in range(C):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# ======================================================================
# 48. Rotate Image
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# ======================================================================
# 19. Remove Nth Node From End of List
# Topic : Linked List
# ======================================================================
# Time Complexity: O(), Space Complexity: O()

class Solution:
    def removeNthFromEnd(self, head, n):

        fast = slow = head

        for _ in range(n): fast = fast.next 

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
    
# ======================================================================
# 238. Product of Array Except Self
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        
        #forward
        for i in range(1, len(nums)):
            ans[i] *= ans[i-1] * nums[i-1]


        #reverse
        reverse = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            ans[i] = ans[i] * reverse
            reverse = reverse * nums[i]
        return ans

# ======================================================================
# 200. Number of Islands
# Topic : Array
# ======================================================================
#DFS
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def numIslands(self, grid):

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt

    def dfs(self, grid, i, j):
        
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

#BFS
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def numIslands(self, grid):

        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    self.bfs(grid, i, j, len(grid), len(grid[0]))

        return cnt

    def bfs(self, grid, i, j, R, C):
        queue = [(i, j)]
        idx = 0
        grid[i][j] = "0"

        while idx < len(queue):
            y, x = queue[idx]
            idx += 1

            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = y + dy
                nx = x + dx

                if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == "1":
                    grid[ny][nx] = "0"
                    queue.append((ny, nx))

# ======================================================================
# 56. Merge Intervals
# Topic : Array
# ======================================================================
# Time Complexity: O(), Space Complexity: O()

#sort()
class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res

#sorted(intervals, key=lambda x: x[0])
class Solution():
    def merge(self, intervals):        
        itv = sorted(intervals, key=lambda x: x[0]) ###
        rst = []

        for arr in itv:
            if rst and arr[0] <= rst[-1][1]:
                rst[-1][1] = max(rst[-1][1], arr[1])
            else:
                rst += [arr]
        return rst

# ======================================================================
# 53. Maximum Subarray
# Topic : Dynamic Programming
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def maxSubArray(self, nums):
        cur = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)

        return best

# ======================================================================
# 3. Longest Substring Without Repeating Characters
# Topic : Sliding Window
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        last = {}

        left = 0

        for right in range(len(s)):
            if s[right] in last:
                left = max(left, last[s[right]])

            max_len = max(max_len, right-left+1)
            last[s[right]] = right+1

        return max_len

# ======================================================================
# 5. Longest Palindromic Substring
# Topic : Two Pointers
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)

            if len(odd) > len(ans):
                ans = odd

            if len(even) > len(ans):
                ans = even

        return ans

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

# ======================================================================
# 300. Longest Increasing Subsequence
# Topic : Dynamic Programming, Binary search
# ======================================================================

# DP
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Binary Search
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)#길이 i 짜리 증가 부분수열의 가장 작은 끝값을 저장하는 것
        
        size = 0

        for n in nums:
            left = 0
            right = size-1
            while left <= right:
                mid = (left + right) // 2
                
                if tails[mid] < n:
                    left = mid + 1
                else:
                    right = mid - 1
            tails[left] = n
            size = max(size, left + 1)# tails의 값을 교체했으면 size 그대로 탐색, 추가했으면 1개 늘어남
        return size
    
# ======================================================================
# 33. Search in Rotated Sorted Array
# Topic : Binary search
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:  # 닫힌 구간 [left, right]
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # 왼쪽 구간 [left, mid]가 정렬되어 있는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:# 오른쪽 구간 [mid, right]가 정렬되어 있는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# ======================================================================
# 230. Kth Smallest Element in a BST
# Topic : Binary search Tree
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def kthSmallest(self, root, k):
        stk = []
        cur = root

        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left

            cur = stk.pop()
            k -= 1

            if k == 0:
                return cur.val

            cur = cur.right #오른쪽의 가장 left도 탐색하기 위해


# ======================================================================
# 128. Longest Consecutive Sequence
# Topic : Array, Hash Table
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def longestConsecutive(self, nums):
        
        nums = set(nums)
        max_len = 0

        for n in nums:
            if n-1 not in nums:
                length = 1

                while n + length in nums:
                    length += 1
                max_len = max(max_len, length)
        return max_len

# ======================================================================
# 102. Binary Tree Level Order Traversal
# Topic : Tree
# ======================================================================
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return ans


# ======================================================================
# 133. Clone Graph
# Topic : Graph Theory
# ======================================================================

# DFS
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        clones = {}
        return self.dfs(node, clones)

    def dfs(self, cur, clones):
        if cur in clones:
            return clones[cur]

        cloned = Node(cur.val)
        clones[cur] = cloned

        for nxt in cur.neighbors:
            cloned.neighbors.append(self.dfs(nxt, clones))

        return cloned

# BFS
# Time Complexity: O(), Space Complexity: O()
class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        clones = {}
        clones[node] = Node(node.val)

        queue = [node]
        index = 0

        while index < len(queue):
            cur = queue[index]
            index += 1

            for nxt in cur.neighbors:
                if nxt not in clones:
                    clones[nxt] = Node(nxt.val)
                    queue.append(nxt)

                clones[cur].neighbors.append(clones[nxt])

        return clones[node]