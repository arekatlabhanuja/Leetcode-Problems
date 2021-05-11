# 703. Kth Largest Element in a Stream

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element 
# in the sorted order, not the kth distinct element.

# Example 1:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums,val)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        