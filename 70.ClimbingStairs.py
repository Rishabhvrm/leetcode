def climbStairs(n) -> int:
        
    # # base case
    # if n == 0 or n == 1:
    #     return 1

    # # initialize table
    # dp = [0] * (n+1)
    # dp[0] = dp[1] = 1

    # # fibonnaci
    # for i in range(2, n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    #     # print(dp)

    # return dp[n]

    
    # initialize table
    dp = [0] * (n+1)

    # base case
    dp[0] = dp[1] = 1

    # current step is summation of ways till this step
    # fibonnaci
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def climb_stairs(n):
    a, b = 1, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

print(climbStairs(3))
print(climb_stairs(3))