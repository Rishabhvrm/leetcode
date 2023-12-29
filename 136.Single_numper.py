def singleNumber(nums):
    d = {}
    for ele in nums:
        # if ele not in d:
        #     d[ele] = 1
        # else:
        #     d[ele] += 1
        d[ele] = 1 + d.get(ele,0) if ele in nums else 1
    print(d)
    
    for k, v in d.items():
        if v == 1:
            return k
        
def single_number_xor(nums):
    # APPROACH: BIT MANIPULATION, XOR
    # TIME: O(n)
    # SPACE: O(1)
    res = 0
    for n in nums:
        res ^= n

    return res


n = [2,2,1]
print(singleNumber(n))
print(single_number_xor(n))
