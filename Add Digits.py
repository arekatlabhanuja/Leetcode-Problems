# 258. Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum=0
        while len(str(num))!=1:
            for i in str(num):
                sum+=int(i)
            
            if len(str(num))==1:
                return int(num)
            else:
                num=sum
                sum=0
        return int(num)