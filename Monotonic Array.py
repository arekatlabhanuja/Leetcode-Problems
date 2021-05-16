# 896. Monotonic Array
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Example 1:

# Input: nums = [1,2,2,3]
# Output: true

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return (all(nums[i] <= nums[i+1] for i in range(len(nums) -1)) or
            all(nums[i] >= nums[i+1] for i in range(len(nums) -1)))