# 1827. Minimum Operations to Make the Array Increasing
# Example 1:

# Input: nums = [1,1,1]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[2], so nums becomes [1,1,2].
# 2) Increment nums[1], so nums becomes [1,2,2].
# 3) Increment nums[2], so nums becomes [1,2,3].

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        app=0
        for i in range(0,len(nums)-1):
            if nums[i]>=nums[i+1]:
                a=abs(nums[i]-nums[i+1])+1
                nums[i+1]+=a
                app+=a
        return app