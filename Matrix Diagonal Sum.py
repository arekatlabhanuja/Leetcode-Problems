# 1572. Matrix Diagonal Sum
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n=len(mat)
        sum=0
        for i in range(n):
            sum+=mat[i][i]+mat[i][n-i-1]
        if n%2==1:
            sum-=mat[n//2][n//2]
        return sum