# 94. Binary Tree Inorder Traversal
# Inorder traversal-Left,root,right
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Recursive Approach

class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)


# Iterative Approach

def inorderTraversal(self,root):
    result=[]
    stack=[]
    if root is None:
        return []
    while root is not None or stack!=[]:
        while root is not None:
            stack.append(root)
            root=root.left
        root=stack.pop()
        result.append(root.val)
        root=root.right
