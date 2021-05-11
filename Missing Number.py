# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number 
# in the range that is missing from the array.
# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
# 1 is the missing number in the range since it does not appear in nums.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            if nums[0]==0:
                return 1
            else:
                return 0
            
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
