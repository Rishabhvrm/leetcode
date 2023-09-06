def containsDuplicate(nums) -> bool:
    # new_nums = set()
    # for ele in nums:
    #     if ele in new_nums:
    #         return True
    #     else:
    #         new_nums.add(ele)
    # return False

    # revision
    s = set()
    for ele in nums:
        if ele not in s:
            s.add(ele)
        else:
            return True
    return False