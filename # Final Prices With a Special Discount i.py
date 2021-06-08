# Final Prices With a Special Discount in a Shop
# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
# For items 3 and 4 you will not receive any discount at all.

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>prices[j]:
                    prices[i]=prices[i]-prices[j]
                    break
        return prices
