def climbStairs(n) -> int:
        
    # base case
    if n == 0 or n == 1:
        return 1

    # initialize table
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    # fibonnaci
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        # print(dp)

    return dp[n]

print(climbStairs(10))