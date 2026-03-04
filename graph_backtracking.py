"""
- Graphs
- Backtracking

"""

# ========================================================
# Graphs : 5 questions
# ========================================================

# 200. Number of Islands (Medium)

class Solution(object):
    def numIslands(self, grid):
        
        raws = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(raws):
            for j in range(cols):
                if grid[i][j] == '1':
                    grid = self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
        return grid

# 994. Rotting Oranges (Medium)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = set()
        rotten = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        cnt = 0
        while fresh and rotten:
            for _ in range(len(rotten)):
                i, j = rotten.pop(0)
                for xy in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                    if xy in fresh:
                        fresh.remove(xy)
                        rotten.append(xy)
            cnt += 1

        return -1 if fresh else cnt
    
# 133. Clone Graph (Medium)

class Solution:
    def cloneGraph(self, node):

        if not node:
            return None
        
        clones = {}

        def dfs(cur):

            if cur in clones:
                return clones[cur]

            cloned = Node(cur.val)
            clones[cur] = cloned#1:1 between the original node and its deep-copied node.
            
            for nxt in cur.neighbors:
                cloned.neighbors.append(dfs(nxt))
            return cloned

        return dfs(node)

# 207. Course Schedule (Medium)

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)] # [[], []]
        visited = [0 for _ in range(numCourses)] # [0, 0]

        # create graph
        for x, y in prerequisites:
            graph[x].append(y)

        # visit each node
        for i in range(numCourses):
            if not self.dfs(i, graph, visited): 
                return False
        
        return True

    def dfs(self, i, graph, visited):

        # if the node is marked as being visited
        if visited[i] == -1:
            return False

        # if it's done visited
        if visited[i] == 1:
            return True

        # mark as visit
        visited[i] = -1

        # visit all the neighbors
        for j in graph[i]:
            if not self.dfs(j, graph, visited):
                return False
        
        # after visit all the neighbors, mark it as done
        visited[i] = 1
        return True

# 1971. Find if Path Exists in Graph
# Two approaches: DFS and Union-Find

# DFS
class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = [False] * n
        visited[source] = True

        while stack:
            cur = stack.pop()
            if cur == destination:
                return True
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)

        return False

# Union-Find
class Solution:
    def validPath(self, n, edges, source, destination):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
# ========================================================
# Backtracking : 6 questions
# ========================================================    

# 46. Permutations (Medium)
class Solution:
    def permute(self, nums):


    #    rst = [] 
    #    self.backtrack(nums, [], rst) 
    #    return rst 
        
    #def backtrack(self, nums, path, rst): 
        
    #    if len(path) == len(nums): 
    #        rst.append(path[:]) 
    #        return 
            
    #    for n in nums: 
    #        if n in path: 
    #            continue 
    #        path.append(n) 
    #        self.backtrack(nums, path, rst) 
    #        path.pop()
        
        rst = []
        self.dfs(nums, rst, [])
        return rst

    def dfs(self, nums, rst, path):
        if len(nums) == len(path):
            rst.append(path)
            return

        for i in range(len(nums)):
            if nums[i] not in path:
                self.dfs(nums, rst, path + [nums[i]])
    



    
# 47. Permutations II (Medium)

class Solution(object):
    def permuteUnique(self, nums):

        rst = []
        nums.sort()
        self.dfs(nums, [], rst)
        return rst

    def dfs(self, nums, path, rst):
        if not nums:
            rst.append(path)
            return

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], rst)


# 257. Binary Tree Paths (Easy)
class Solution:
    def binaryTreePaths(self, root):
        rst = []
        self.dfs(root, rst, "")
        return rst


    def dfs(self, node, rst, path):

        if not node:
            return

        if path == "":
            cur = str(node.val)
        else:
            cur = path + "->" + str(node.val)

        if not node.right and not node.left:
            rst.append(cur)
            return

        if node.right:
            self.dfs(node.right, rst, cur)
        if node.left:
            self.dfs(node.left, rst, cur)

# 78. Subsets (Medium)

class Solution:
    def subsets(self, nums):

        rst = []
        self.dfs(nums, rst, [], 0)
        return rst


    def dfs(self, nums, rst, path, idx):
        if idx == len(nums):
            rst.append(path[:])
            return


        path.append(nums[idx])
        self.dfs(nums, rst, path, idx+1)

        path.pop()
        self.dfs(nums, rst, path, idx+1)

# 17. Letter Combinations of a phone number (Medium)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        rst = []
        self.dfs(digits, "", rst, 0, dic)
        return rst

    def dfs(self, digits, path, rst, idx, dic):
        if idx == len(digits):
            rst.append(path)
            return

        string = dic[digits[idx]]
        for ch in string:
            self.dfs(digits, path + ch, rst, idx + 1, dic)

# 39. Combination Sum (Medium)

class Solution:
    def combinationSum(self, candidates, target):
        
        candidates.sort()
        rst = []
        self.dfs(candidates, target, rst, 0, [])
        return rst


    def dfs(self, candidates, target, rst, idx, path):
        if target < 0:
            return

        if target == 0:
            rst.append(path[:])

        for i in range(idx, len(candidates)):
            self.dfs(candidates, target-candidates[i], rst, i, path + [candidates[i]])


# 40. Combination Sum II (Medium)
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        rst = []
        self.dfs(candidates, target, 0, [], rst)
        return rst

    def dfs(self, candidates, target, idx, path, rst):
        if target < 0:
            return

        if target == 0:
            rst.append(path) #new array
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], rst)

# 79. Word Search (Medium)
class Solution:
    def exist(self, board, word):
        
        for i in range(len((board))):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, idx):

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] == '*' or board[i][j] != word[idx]:
            return False
        
        if idx == len(word) - 1:
            return True

        cache = board[i][j]
        board[i][j] = '*'
        rst = self.dfs(board, word, i-1, j, idx+1) or \
        self.dfs(board, word, i+1, j, idx+1) or \
        self.dfs(board, word, i, j+1, idx+1) or \
        self.dfs(board, word, i, j-1, idx+1)

        board[i][j] = cache
        return rst

# 417. Pacific Atlantic Water Flow (Medium)