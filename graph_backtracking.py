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
        
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != '1':
                return
            
            grid[row][col] = '0'
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    cnt += 1

        return cnt

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

# ========================================================
# Backtracking : 5 questions
# ========================================================    

# 46. Permutations (Medium)
class Solution:
    def permute(self, nums):
        rst = []
        
        def backtrack(path):
            if len(path) == len(nums):
                rst.append(path[:])
                return
            
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                backtrack(path)
                path.pop()
        
        backtrack([])
        return rst