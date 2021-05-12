# 103. Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes
# values. (i.e., from left to right, then right to left for the next level and alternate between).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Step 1:
        s1=[3]
        s2=[]
        level=[3]
        result=[[3]]
        Step 2:
        s1=[]
        s2=[20,9]
        level

        """
        if root is None:
            return []
        s1=[root]
        s2=[]
        level=[]
        result=[]
        while s1 or s2:
            while s1:
                root=s1.pop()
                level.append(root.val)
                if root.left:
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)
            result.append(level)
            level=[]
            while s2:
                root=s2.pop()
                level.append(root.val)
                if root.right:
                    s1.append(root.right)
                if root.left:
                    s1.append(root.left)
            if level!=[]:
                result.append(level)
                level=[]
        return result