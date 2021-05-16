# 1859. Sorting the Sentence
# Example 1:

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", 
# then remove the numbers.

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s[::-1].split()
        words.sort()
        result = [ word[1:][::-1] for word in words ]
        return ' '.join(result)