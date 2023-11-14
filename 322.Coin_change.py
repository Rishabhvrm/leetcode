def coinChange(coins, amount) -> int:
    # size = amount + 1 bcz 0 indexed
    # value = amount + 1, any value greater than amount ??
    dp = [amount + 1] * (amount + 1)      

    # base case
    dp[0] = 0           # if we wanna count to 0, it's gonna take 0 coins

    # computing values in dp
    # fill from 1 to amount
    # for every amount 'amt' in range 1 to amount
    for amt in range(1, amount+1):
        for coin in coins:
            # if amt is greater than the coin denomination
            # it's gonna require coins, also idx lies in the array
            if amt - coin >= 0:
                # recurrance relation
                dp[amt] = min(1 + dp[amt-coin], dp[amt])

    # if return value != default value during initialization, it means we couldn't find the solution
    return dp[amount] if dp[amount] != amount+1 else -1


def coinChange2(coins, amount):
    ## REVISIT
    def backtrack(curr_sum, steps):
        # base case
        if curr_sum == amount:
            res.append(steps)
            return

        if curr_sum > amount: return

        for coin in coins:
            curr_sum += coin
            backtrack(curr_sum, steps + 1)
            curr_sum -= coin

    res = []
    backtrack(0, 0)
    return min(res)
    

## value = amount + 1, any value greater than amount.
## bcs see the last return statement, it helps us find out if the 
## amount can be made using the coins or not, also see the dp[amt]
## statement, it updates the curr value and store the prev value of dp[amt]
## for next iteration of coin.
## It doesn't have to be amount + 1, could be any value, say inf

## TIME: O(amount * len(coin))
## SPACE: O(amount)


coins = [1,2,5]
# amount = 11
# coins = [1,3,4,5]
amount = 11
print(coinChange3(coins, amount))

