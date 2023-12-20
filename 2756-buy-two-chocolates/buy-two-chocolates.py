class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        return money-sum(heapq.nsmallest(2, prices)) if money-sum(heapq.nsmallest(2, prices))>= 0 else money