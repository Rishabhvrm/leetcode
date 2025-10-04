class Solution:
    '''
    TC: O(N)
    SC: O(1)
    '''
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        # dividend, divisor = numBottles, numExchange
        D, d = numBottles, numExchange

        while D // d:
            q = D // d      
            r = D % d       
            res += q        
            D = q + r           
        
        return res