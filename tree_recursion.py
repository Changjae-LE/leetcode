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
