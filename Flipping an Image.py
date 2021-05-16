# 832. Flipping an Image
# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for i in image:
            s=i[::-1]
            for k in range(len(s)):
                if s[k]==1:
                    s[k]=0
                else:
                    s[k]=1
            res.append(s)
        return res
            
                