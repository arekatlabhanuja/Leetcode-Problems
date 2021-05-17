# 905. Sort Array By Parity
# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        res1=[]
        
        for i in range(len(nums)):
            if nums[i]%2==0:
                res.append(nums[i])
            if nums[i]%2==1:
                res1.append(nums[i])
        return res+res1
       
                