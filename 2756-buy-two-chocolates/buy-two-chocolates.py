class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        m0 = float('inf')
        m1 = float('inf')

        for p in prices:
            if p < m1:
                if p < m0:
                    m1 = m0
                    m0 = p
                else:
                    m1 = p

        m = money - m0 - m1

        return m if m>=0 else money