"""
- Tree
- Recursion

"""


# ========================================================
# Tree : 5 questions
# ========================================================

# 94. Binary Tree Inorder Traversal (Easy)



class Solution:
    def inorderTraversal(self, root):
        rst = []
        self.inorder(root, rst)
        return rst

    def inorder(self, root, rst):
        if not root:
            return
        self.inorder(root.left, rst)
        rst.append(root.val)
        self.inorder(root.right, rst)
        return rst

# 104. Maximum Depth of Binary Tree (Easy)

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        right = self.maxDepth(root.left)
        left = self.maxDepth(root.right)
        return max(right, left)+1

# 100. Same Tree (Easy)

class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
        
        return p is q
    
# 102. Binary Tree Level Order Traversal (Medium)

class Solution:
    def levelOrder(self, root):

        if not root:
            return []
        
        rst = []
        level = [root]
        while level:
            rst.append([node.val for node in level])
            pair = [(node.left, node.right) for node in level]
            level = [n for node in pair for n in node if n]
        return rst
    

        #if not root:
        #    return []
        #rst = []
        #level = [root]

        #while level:
        #    rst.append([node.val for node in level])
        #    pair = [(node.left, node.right) for node in level]
        #    next_level = []
        #    for left, right in pair:
        #        if left:
        #            next_level.append(left)
        #        if right:
        #            next_level.append(right)
        #    level = next_level
        #return rst

# 106. Construct Binary Tree from Inorder and Postorder Traversal

class Solution:
    def buildTree(self, inorder, postorder):
        #if inorder:
        #    idx = inorder.index(postorder.pop())
        #    root = TreeNode(inorder[idx])
        #    root.right = self.buildTree(inorder[idx+1:], postorder) ## right first!!!
        #    root.left = self.buildTree(inorder[:idx], postorder)
        #    return root



        idx = {v: i for i, v in enumerate(inorder)}
        post_i = len(postorder) - 1

        def helper(l, r):
            nonlocal post_i
            if l > r:
                return None

            root_val = postorder[post_i]
            post_i -= 1
            root = TreeNode(root_val)

            mid = idx[root_val]

            root.right = helper(mid + 1, r)
            root.left = helper(l, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
    
# 112. Path Sum (Easy)

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val

        right = self.hasPathSum(root.right, targetSum - root.val)
        left = self.hasPathSum(root.left, targetSum - root.val)

        return left or right

# 226. Invert Binary Tree (Easy)

class Solution:
    def invertTree(self, root):

        if not root:
            return
        #postorder
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root