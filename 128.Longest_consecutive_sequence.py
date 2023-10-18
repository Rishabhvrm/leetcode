
# def longestConsecutive(self, nums: List[int]) -> int:
def longestConsecutive(nums) -> int:
    
    if not nums: return 0

    # add element to set
    num_set = set(nums)
    max_len = 0

    for ele in num_set:
        # check if curr_num is start of sequence
        if ele - 1 not in num_set:
            curr_ele = ele
            curr_len = 1

            while curr_ele + 1 in num_set:
                curr_ele += 1
                curr_len += 1
            
            max_len = max(max_len, curr_len)
    
    return max_len
