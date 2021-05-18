# 263. Ugly Number
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.
# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        
        s=[2,3,5]
        for i in s:
            while n%i==0:
                n=n//i
        return n==1

