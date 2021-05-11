# 108. Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def bstfromarr(arr):
            if not arr:
                return None

            mid=len(arr)//2
            root=TreeNode(arr[mid])

            root.left=bstfromarr(arr[:mid])
            root.right=bstfromarr(arr[mid+1:])

            return root
        return bstfromarr(nums)