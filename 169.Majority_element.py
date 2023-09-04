def majorityElement(nums) -> int:
    dict = {}
    n = len(nums)

    # traverse array
    for ele in nums:
        # add element in dict if not present
        if ele not in dict:
            dict[ele] = 1
        # increase count if encountered again
        else:
            dict[ele] = dict[ele] + 1
        
        # if count goes more than n//2, return ele
        if dict[ele] > n//2:
            print(dict)
            return ele
    

nums1 = [2,2,1,1,1,2,2]
nums = [3,2,3]
print(majorityElement(nums))

# print(3//2)