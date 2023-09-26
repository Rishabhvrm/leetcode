
def sortedSquares(nums):
    
    ## BRUTE FORCE
    ## T(N): O(N LOG N)

    # r = []

    # for n in nums:
    #     r.append(n*n)

    # return sorted(r)


    ## T(N): O(N)
    ## 2 POINTERS

    l = len(nums)
    out = [0] * l                               # initialize output array
    left, right = 0, l - 1                      # initialize left and right pointers
    
    # range(start:stop:step)
    # start from end, go till start, with step of -1
    # so that output array is sorted
    for i in range(l-1, -1, -1):         

        left_square = nums[left] ** 2           # calculate left and right squares
        right_square = nums[right] ** 2

        if left_square <= right_square:         # compare, assign o/p and move pointers
            out[i] = right_square
            right -= 1
        else:
            out[i] = left_square
            left += 1

    return out

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))

