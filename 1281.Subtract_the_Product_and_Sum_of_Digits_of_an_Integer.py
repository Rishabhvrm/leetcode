class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1, 0

        while n:
            sum += n % 10
            prod *= n % 10
            
            n //= 10

        return prod - sum
    
obj = Solution()
n = 234
print(obj.subtractProductAndSum(n))