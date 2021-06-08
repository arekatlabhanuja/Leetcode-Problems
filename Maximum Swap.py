# 670. Maximum Swap
# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        l=list(num)
        new=0
        temp=0
        maxi=int(num)
        for i in range(len(l)):
            for j in range(len(l)):
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
                new=''.join(l)
                maxi=max(maxi,int(new))
                l=list(num)
        return(maxi)


