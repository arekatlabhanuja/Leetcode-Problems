#Range Sum of BST
#Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
#Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans
