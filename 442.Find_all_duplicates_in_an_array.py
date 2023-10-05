
def findDuplicates(nums):
    
    ## APPROACH 1: 
    # use hashset to store values, set doesn't allow duplicates
    # append to output if ele already present in set

    ## T(N): O(N)
    ## SPACE: O(N), set() of size almost N required and result[]
    
    # num_set = set()
    # output = []
    # for n in nums:
    #     # if ele present in set
    #     # add to output
    #     if n in num_set:
    #         output.append(n)     
    #     # traverse and add to set
    #     else:
    #         num_set.add(n)

    # return output

    ## APPROACH 2: 
    # visit an ele by marking its index as negative (one less than its actual index)
    # ele value -> go to this index 

    ## T(N): O(N)
    ## SPACE: constant, only result[] required

    result = []
    
    for ele in nums:
        # find idx by subtracting 1 from abs value of ele
        # arrays are 0 indexed
        idx = abs(ele) - 1
        
        # if element already visited (negative indicates visited)
        # add to result array
        if nums[idx] < 0: result.append(abs(ele))
        
        # if it's positive, it means it's yet to be visited
        # mark element at (idx - 1) negative indicating, it's visited now
        else: nums[idx] *= -1

    return result

    
