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