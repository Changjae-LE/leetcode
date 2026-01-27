"""
- Tree
- Recursion

"""


# ========================================================
# Tree : 5 questions
# ========================================================

# 94. Binary Tree Inorder Traversal (Easy)



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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

