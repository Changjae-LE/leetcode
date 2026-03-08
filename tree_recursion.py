"""
- Tree
- Recursion/DSF

"""


# ========================================================
# Tree : 5 questions
# ========================================================

# 94. Binary Tree Inorder Traversal (Easy)

#Time Complexity = O(n)
#Space Complexity = O(n)

# rst <- empty list
# inorder()
# return rst
#
#Function inorder
#   IF node is None: return 
#   visit node.left
#   rst <- append node.val
#   visit node.right

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
#Time complexity is O(n)
#Space complexity is O(n)

# Function maxDepth(node):
#   if node is None: return 0
# leftdepth <- maxDepth(node.left)
# rightdepth <- maxDepth(node.right)
# return max(leftdepth + rightdepth) + 1

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        right = self.maxDepth(root.left)
        left = self.maxDepth(root.right)
        return max(right, left)+1

# 100. Same Tree (Easy)
#Time complexity is O(n)
#Space complexity is O(n)

# Function isSameTree(tree_A, tree_B):
#  if tree_A is null and tree_B is null: return true
#  if tree_A is null or tree_B is null: return False
#    return tree_A.val == tree_B.val and isSameTree(tree_A.right, tree_B.right), isSameTree(tree_A.left, tree_B.left)
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
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
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

# 106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)

class Solution:
    def buildTree(self, inorder, postorder):

        if not inorder:
            return None

        root_val = postorder.pop()
        tree = TreeNode(root_val)
        mid = inorder.index(root_val)

        tree.right = self.buildTree(inorder[mid+1:], postorder)
        tree.left = self.buildTree(inorder[:mid], postorder)

        return tree

# 889. Construct Binary Tree from Preorder and Postorder Traversal (Medium)
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        left_root = preorder[1]
        idx = postorder.index(left_root)
        left_size = idx + 1

        root.left = self.constructFromPrePost(preorder[1:1 + left_size], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[1 + left_size:], postorder[left_size:-1])

        return root
    
# ========================================================
# Recursion/DFS : 5 questions
# ========================================================

# 112. Path Sum (Easy)

#Function hasPathSum(root, targetSum):
#   if root is empty: return False
#   if root.left is null and root.right is null: return targetSum == root.val
#   right <- haspathSum(root.right, targetSum - root.val)
#   left <- haspathSum(root.left, targetSum - root.val)
#   return right or left

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

# 572. Subtree of Another Tree (Easy)

class Solution:
    def isSubtree(self, root, subRoot):

        if not root:
            return False
        return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, root, subRoot):
        if root and subRoot:
            return root.val == subRoot.val and self.isSametree(root.right, subRoot.right) and self.isSametree(root.left, subRoot.left)
        return root is subRoot
    
#  98. Validate Binary Search Tree (Medium)

    #Inorder traversal of a BST is strictly increasing.
class Solution(object):
    def isValidBST(self, root):
        
        rst = []
        self.inOrder(root, rst)
        
        for i in range(1, len(rst)):
            if rst[i-1] >= rst[i]:
                return False
                
        return True

    def inOrder(self, root, rst):
        if not root:
            return
        self.inOrder(root.left, rst)
        rst.append(root.val)
        self.inOrder(root.right, rst)

# 236. Lowest Common Ancestor of a Binary Tree (Medium)

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right