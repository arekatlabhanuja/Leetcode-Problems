# Sum of All Odd Length Subarrays
# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        final_sum=0
        for i in range(0,len(arr),2):
            for j in range(len(arr)):
                if j + i < len(arr):
                    final_sum += sum(arr[j:j+i+1])
        return final_sum
