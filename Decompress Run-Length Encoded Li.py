# 1313. Decompress Run-Length Encoded List
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for k,v in enumerate(nums):
            if k==0 or k%2==0:
                res+=v*[nums[k+1]]
        return res