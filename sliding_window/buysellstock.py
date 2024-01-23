class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        profit = 0
         
        while right < len(prices):
            current = prices[right] - prices[left]
            if current > profit:
                profit = current
            if prices[left] > prices[right]:
                left = right
            
            right += 1
         
        return profit



        