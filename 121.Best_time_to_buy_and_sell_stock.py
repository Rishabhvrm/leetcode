def maxProfit(prices) -> int:

    ## BRUTE FORCE - raises TLE
    ## TIME COMPLEXITY - O(N * N)

    # length = len(prices)
    # # base cases
    # if length == 1:
    #     return 0

    # # if array is in descending order, no transactions
    # non_increasing = all(prices[i] >= prices[i+1] for i in range(length-1))
    # if non_increasing:
    #     return 0

    # # store difference btw current value and max value ahead
    # diff = []

    # # go from next index till second last index
    # for i in range(length-1):
    #     diff.append(max(prices[i+1:]) - prices[i])

    # # return 0 if all differences are negative
    # return 0 if max(diff) < 0 else max(diff)

    
    
    ## 2 POINTERS APPROACH

    # initialize buy and sell pointers
    b, s = 0, 1

    profit, l = 0, len(prices)

    # until sell pointer reaches end
    while s < l:
        
        # if selling price > buying price, calculate profit 
        # and point selling to next value
        if prices[s] > prices[b]:
            profit = max(profit, prices[s] - prices[b])

        # if selling price < buying price, 
        # point buying price to the new value
        # and point selling price to next value
        elif prices[s] < prices[b]:
            b = s

        s += 1

    return profit


p = [7,1,5,3,6,4]
p2 = [3,3]
p3 = [1]
print(maxProfit(p))
