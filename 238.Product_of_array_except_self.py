
def productExceptSelf(nums):
    
    ## APPROACH: calculate right and left products for each element in array
    ## T(N): O(N)
    ## SPACE: O(N)

    n = len(nums)
    left_product, right_product = 1, 1

    # initialize arrays
    prefix, suffix = [1] * n, [1] * n

    # calculate and store left products in prefix
    for i in range(n):
        prefix[i] = left_product
        left_product *= nums[i]

    # calculate and store right products in suffix
    for i in range(n-1, -1, -1):
        suffix[i] = right_product
        right_product *= nums[i]
    
    # use prefix and suffix to calculate result
    return [prefix[i] * suffix[i] for i in range(n)]