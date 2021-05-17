# 1844. Replace All Digits with Characters
# Example 1:

# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        for i in s:
            if not i.isdigit():
                res+=i
            else:
                res+=chr(ord(res[-1])+int(i))
        return res
        