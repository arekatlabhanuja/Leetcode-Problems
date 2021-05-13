# 1295. Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.
#  Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        str1=[]
        count=0
        # for i in nums:
        #     str1.append(str(i))
        str1=map(str,nums) #converts all the intergers into strings without using loop
        for i in str1:
            if len(i)%2==0:
                count+=1
        return count