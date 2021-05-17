# 1464. Maximum Product of Two Elements in an Array
# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
# you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 0
        max1 = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                currMax = (nums[i]-1)*(nums[j]-1)
                max1 = max(currMax,max1)
        return max1