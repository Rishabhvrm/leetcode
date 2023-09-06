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


n = [2,2,1]
print(singleNumber(n))

# d = {}
# for i in range(1,4):
#     d[i] += 1

# print(d)