# similar to 268.Missing Numbers
def findDisappearedNumbers(nums):
    
    set1, l = set(nums), len(nums)

    # create second set, the ideal set with no missing values
    set2 = set()
    for ele in range(1, l+1):
        set2.add(ele)

    # return set difference
    return list(set2-set1)

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))