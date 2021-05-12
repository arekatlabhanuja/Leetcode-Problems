# Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes'
# values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

def levelOrder(self,root):
    if root is None:
        return []
    queue=[root]
    nextqueue=[]
    level=[]
    result=[]
    while queue!=[]:
        for root in queue:
            level.append(root.val)
            if root.left is not None:
                nextqueue.append(root.left)
            if root.right is not None:
                nextqueue.append(root.right)
        result.append(level)
        queue=nextqueue
        nextqueue=[]
        level=[]
    return result