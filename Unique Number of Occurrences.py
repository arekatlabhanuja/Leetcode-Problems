# 1207. Unique Number of Occurrences
# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
       
        counts= Counter(arr)
        keys_count=len(set(counts.keys()))
        values_count=len(set(counts.values()))
        if keys_count==values_count:
            return True
        return False