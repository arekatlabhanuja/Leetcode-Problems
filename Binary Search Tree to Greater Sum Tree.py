# Binary Search Tree to Greater Sum Tree
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is
#  changed to the original key plus sum of all keys greater than the original key in BST.

# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum=0
        def helper(node):
            if node==None:
                return
            helper(node.right)
            sum+=node.val
            node.val=sum
            helper(node.left)
        helper(root)
        return root