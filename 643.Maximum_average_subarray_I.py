def findMaxAverage(nums, k) -> float:
    
    ## APPROACH 1 
    ## T(N): O(N * N) - GIVES TLE
    ## SPACE: O(1)

    # initialize max_avg to lowest possible value
    # max_avg = float('-inf')

    # window moves in the whole array
    # for i in range(len(nums) - k + 1):
    #     # sum for elements in a window
    #     s = 0
        
    #     # for first k elements in the window, calculate average
    #     # for j in range(i, k+i):
    #     #     sum += nums[j]

    #     s = sum(nums[i:i+k])

    #     # calculate avg and update max_avg
    #     if s/k > max_avg:
    #         max_avg = s/k

    # return max_avg

    ## APPROACH 2: sum - a + d
    ## T(N): O(N)
    
    curr_sum = sum(nums[:k])
    max_avg = curr_sum/k

    for i in range(len(nums)-k):
        
        # add next element and remove first element in the sliding window
        curr_sum -= nums[i]
        curr_sum += nums[i+k]

        # update max_avg if current avg is greater
        max_avg = max(max_avg, curr_sum/k)

    return max_avg  


nums = [1,12,-5,-6,50,3]
k = 4
# nums = [5]
# k = 1
print(findMaxAverage(nums, k))